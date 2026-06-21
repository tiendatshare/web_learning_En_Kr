import React, { useState, useEffect, useRef } from 'react';

const API_BASE = import.meta.env.VITE_API_BASE || (
  (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
    ? 'http://localhost:3001'
    : ''
);

export default function SpeakingMode() {
  const [situations, setSituations] = useState([]);
  const [selectedId, setSelectedId] = useState('');
  const [situationData, setSituationData] = useState(null);
  const [currentTurnIdx, setCurrentTurnIdx] = useState(0);
  const [userRole, setUserRole] = useState(''); // e.g. "Trí" or "지수 (Ji-xu)"
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [similarity, setSimilarity] = useState(null);
  const [history, setHistory] = useState([]); // List of completed turns with stats
  const [roles, setRoles] = useState([]);
  const recognitionRef = useRef(null);

  const [currentLang, setCurrentLang] = useState('korean');
  const [roleSelected, setRoleSelected] = useState(false);

  useEffect(() => {
    fetchSituations();
    fetch(`${API_BASE}/api/language`)
      .then(res => res.json())
      .then(data => setCurrentLang(data.language || 'korean'))
      .catch(() => {});
  }, []);

  const fetchSituations = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/situations`);
      if (res.ok) {
        const data = await res.json();
        setSituations(data.situations || []);
        if (data.situations.length > 0) {
          setSelectedId(data.situations[0].id);
        }
      }
    } catch (e) {
      console.error('Failed to fetch situations list:', e);
    }
  };

  const handleLoadSituation = async () => {
    if (!selectedId) return;
    try {
      const res = await fetch(`${API_BASE}/api/situations/${selectedId}`);
      if (res.ok) {
        const data = await res.json();
        setSituationData(data);
        setCurrentTurnIdx(0);
        setTranscript('');
        setSimilarity(null);
        setHistory([]);
        
        // Extract unique roles in this dialogue
        const uniqueRoles = [...new Set(data.turns.map(t => t.speaker))];
        setRoles(uniqueRoles);
        if (uniqueRoles.length > 0) {
          setUserRole(uniqueRoles[0]);
        }
        setRoleSelected(false);
      }
    } catch (e) {
      console.error('Failed to load situation content:', e);
    }
  };

  // Play standard TTS for a Korean or English text
  const playTTS = (text) => {
    const ttsLang = currentLang === 'english' ? 'english' : 'korean';
    const audioUrl = `${API_BASE}/api/tts?text=${encodeURIComponent(text)}&lang=${ttsLang}`;
    const audio = new Audio(audioUrl);
    audio.play().catch(err => {
      console.warn("Neural TTS play failed, falling back to Web Speech API:", err);
      if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = currentLang === 'english' ? 'en-US' : 'ko-KR';
        const voices = window.speechSynthesis.getVoices();
        const matchVoice = voices.find(v => v.lang.startsWith(utterance.lang.split('-')[0]));
        if (matchVoice) utterance.voice = matchVoice;
        window.speechSynthesis.speak(utterance);
      }
    });
  };

  // Levenshtein Similarity calculation with fuzzy normalization (Word-level)
  const computeSimilarity = (s1, s2) => {
    const clean = (str) => {
      if (!str) return "";
      return str
        .toLowerCase()
        .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"]/g, "") // remove punctuation
        .replace(/\b(i'm|im)\b/g, "i am")
        .replace(/\b(what's|whats)\b/g, "what is")
        .replace(/\b(he's|hes)\b/g, "he is")
        .replace(/\b(she's|shes)\b/g, "she is")
        .replace(/\b(it's|its)\b/g, "it is")
        .replace(/\b(we're|were)\b/g, "we are")
        .replace(/\b(they're|theyre)\b/g, "they are")
        .replace(/\s+/g, " ") // preserve single spaces for word splitting
        .trim();
    };
    const clean1 = clean(s1);
    const clean2 = clean(s2);
    
    if (clean1 === clean2) return 100;
    if (!clean1 || !clean2) return 0;

    const words1 = clean1.split(" ");
    const words2 = clean2.split(" ");
    
    const track = Array(words2.length + 1).fill(null).map(() => Array(words1.length + 1).fill(null));
    for (let i = 0; i <= words1.length; i += 1) track[0][i] = i;
    for (let j = 0; j <= words2.length; j += 1) track[j][0] = j;
    
    for (let j = 1; j <= words2.length; j += 1) {
      for (let i = 1; i <= words1.length; i += 1) {
        const indicator = words1[i - 1] === words2[j - 1] ? 0 : 1;
        track[j][i] = Math.min(
          track[j][i - 1] + 1, // deletion
          track[j - 1][i] + 1, // insertion
          track[j - 1][i - 1] + indicator // substitution
        );
      }
    }
    const dist = track[words2.length][words1.length];
    const maxLen = Math.max(words1.length, words2.length);
    return Math.round(((maxLen - dist) / maxLen) * 100);
  };

  // Start Speech-to-Text Recognition
  const startSTT = () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      alert("Trình duyệt của bạn chưa hỗ trợ nhận diện giọng nói (STT). Hãy thử trên Google Chrome.");
      return;
    }

    setTranscript('');
    setSimilarity(null);

    const recognition = new SpeechRecognition();
    recognition.lang = currentLang === 'english' ? 'en-US' : 'ko-KR';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = () => {
      setIsListening(true);
    };

    recognition.onend = () => {
      setIsListening(false);
    };

    recognition.onerror = (e) => {
      console.error(e);
      setIsListening(false);
    };

    recognition.onresult = (event) => {
      const resultText = event.results[0][0].transcript;
      setTranscript(resultText);
      
      const currentTurn = situationData.turns[currentTurnIdx];
      const score = computeSimilarity(currentTurn.korean, resultText);
      setSimilarity(score);
    };

    recognitionRef.current = recognition;
    recognition.start();
  };

  // Handle advancing the dialogue turns
  const handleNextTurn = () => {
    if (!situationData) return;
    
    // Add current completed turn to history logs
    const currentTurn = situationData.turns[currentTurnIdx];
    setHistory(prev => [...prev, {
      ...currentTurn,
      userSpoke: currentTurn.speaker === userRole,
      transcript: currentTurn.speaker === userRole ? transcript : null,
      similarity: currentTurn.speaker === userRole ? similarity : null
    }]);

    setTranscript('');
    setSimilarity(null);

    const nextIdx = currentTurnIdx + 1;
    setCurrentTurnIdx(nextIdx);

    // If next turn is not user role, trigger TTS automatically
    if (nextIdx < situationData.turns.length) {
      const nextTurn = situationData.turns[nextIdx];
      if (nextTurn.speaker !== userRole) {
        setTimeout(() => {
          playTTS(nextTurn.korean);
        }, 1000);
      }
    }
  };

  // Start the simulation roleplay loop
  const handleStartRoleplay = (selectedRole) => {
    setUserRole(selectedRole);
    setCurrentTurnIdx(0);
    setHistory([]);
    setTranscript('');
    setSimilarity(null);
    setRoleSelected(true);

    // If first turn is system's turn, speak it
    const firstTurn = situationData.turns[0];
    if (firstTurn.speaker !== selectedRole) {
      setTimeout(() => {
        playTTS(firstTurn.korean);
      }, 500);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {/* Selection Area */}
      {!situationData ? (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem', padding: '2rem 0' }}>
          <span style={{ fontSize: '2rem' }}>📖</span>
          <h3>Chọn tình huống giao tiếp để bắt đầu ôn nói:</h3>
          <div style={{ display: 'flex', gap: '0.5rem', width: '100%', maxWidth: '500px' }}>
            <select 
              value={selectedId} 
              onChange={(e) => setSelectedId(e.target.value)}
              style={{
                flex: 1,
                background: 'rgba(0, 0, 0, 0.25)',
                border: '1px solid var(--border-color)',
                borderRadius: '8px',
                padding: '0.75rem',
                color: 'white',
                outline: 'none'
              }}
            >
              {situations.map(s => (
                <option key={s.id} value={s.id} style={{ background: '#1c1c24' }}>
                  {s.title}
                </option>
              ))}
            </select>
            <button className="btn" onClick={handleLoadSituation}>
              Tải hội thoại
            </button>
          </div>
        </div>
      ) : (
        <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          
          {/* Situation info & Controls */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-color)', paddingBottom: '1rem' }}>
            <div>
              <h3 style={{ fontSize: '1.2rem', fontWeight: 600 }}>{situationData.id}</h3>
              <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                Số câu thoại: {situationData.turns.length} lượt
              </span>
            </div>
            <button className="btn btn-secondary" onClick={() => setSituationData(null)}>
              Quay lại danh sách
            </button>
          </div>

          {/* Role selector on start */}
          {!roleSelected ? (
            <div style={{ background: 'rgba(255,255,255,0.02)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border-color)', textAlign: 'center' }}>
              <p style={{ marginBottom: '1rem', fontWeight: 600 }}>Chọn nhân vật bạn muốn đóng vai:</p>
              <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem' }}>
                {roles.map(r => (
                  <button key={r} className="btn" onClick={() => handleStartRoleplay(r)}>
                    🎭 Đóng vai: {r}
                  </button>
                ))}
              </div>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
              
              {/* Dialogue History area */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {history.map((h, i) => (
                  <div key={i} style={{ 
                    padding: '1rem', 
                    borderRadius: '10px', 
                    background: h.userSpoke ? 'rgba(10, 132, 255, 0.05)' : 'rgba(255,255,255,0.02)',
                    border: `1px solid ${h.userSpoke ? 'rgba(10, 132, 255, 0.2)' : 'var(--border-color)'}`
                  }}>
                    <span style={{ fontSize: '0.75rem', fontWeight: 'bold', color: h.userSpoke ? 'var(--accent-color)' : 'var(--text-secondary)' }}>
                      {h.speaker} {h.userSpoke ? "(Bạn)" : "(Máy)"}
                    </span>
                    <p style={{ fontSize: '1rem', marginTop: '0.25rem', fontWeight: 500 }}>{h.korean}</p>
                    <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontStyle: 'italic' }}>{h.pronunciation}</p>
                    <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>{h.translation}</p>
                    {h.userSpoke && (
                      <div style={{ display: 'flex', gap: '1rem', marginTop: '0.5rem', fontSize: '0.8rem', background: 'rgba(0,0,0,0.15)', padding: '0.4rem', borderRadius: '4px' }}>
                        <span>Đã nói: "{h.transcript}"</span>
                        <span style={{ color: h.similarity >= 80 ? 'var(--success-color)' : h.similarity >= 60 ? 'var(--warning-color)' : 'var(--error-color)' }}>
                          Độ chính xác: {h.similarity}%
                        </span>
                      </div>
                    )}
                  </div>
                ))}
              </div>

              {/* Current Active Turn */}
              {currentTurnIdx < situationData.turns.length ? (
                <div className="fade-in" style={{ 
                  background: 'rgba(255, 255, 255, 0.04)', 
                  border: '1px solid var(--accent-color)', 
                  boxShadow: '0 0 15px var(--accent-glow)',
                  borderRadius: '12px', 
                  padding: '1.5rem',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '1rem'
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontSize: '0.8rem', color: 'var(--accent-color)', fontWeight: 'bold' }}>
                      LƯỢT THOẠI HIỆN TẠI (Lượt {currentTurnIdx + 1}/{situationData.turns.length})
                    </span>
                    <span style={{ fontSize: '0.85rem', background: 'rgba(255,255,255,0.08)', padding: '0.2rem 0.5rem', borderRadius: '4px' }}>
                      Nhân vật: <strong>{situationData.turns[currentTurnIdx].speaker}</strong>
                    </span>
                  </div>

                  <div style={{ padding: '0.5rem 0' }}>
                    <h3 style={{ fontSize: '1.3rem', fontWeight: 600 }}>
                      {situationData.turns[currentTurnIdx].korean}
                    </h3>
                    <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '0.25rem', fontStyle: 'italic' }}>
                      {situationData.turns[currentTurnIdx].pronunciation}
                    </p>
                    <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
                      {situationData.turns[currentTurnIdx].translation}
                    </p>
                  </div>

                  {/* Dialogue action area */}
                  <div style={{ display: 'flex', gap: '0.75rem', borderTop: '1px solid var(--border-color)', paddingTop: '1rem', alignItems: 'center' }}>
                    {situationData.turns[currentTurnIdx].speaker === userRole ? (
                      // User's Turn
                      <>
                        <button 
                          className="btn" 
                          onClick={startSTT}
                          disabled={isListening}
                          style={{ background: isListening ? 'var(--error-color)' : 'var(--accent-color)' }}
                        >
                          🎙️ {isListening ? "Đang lắng nghe..." : "Nhấp để luyện nói"}
                        </button>
                        <button className="btn btn-secondary" onClick={() => playTTS(situationData.turns[currentTurnIdx].korean)}>
                          🔊 Nghe mẫu
                        </button>
                        
                        {transcript && (
                          <div style={{ flex: 1, paddingLeft: '1rem' }}>
                            <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                              Ghi nhận: "{transcript}"
                            </p>
                            {similarity !== null && (
                              <p style={{ 
                                fontSize: '0.85rem', 
                                fontWeight: 'bold', 
                                color: similarity >= 80 ? 'var(--success-color)' : similarity >= 60 ? 'var(--warning-color)' : 'var(--error-color)' 
                              }}>
                                Khớp: {similarity}% {similarity >= 60 ? " (Đạt)" : " (Hãy thử lại)"}
                              </p>
                            )}
                          </div>
                        )}
                        
                        {(similarity >= 60 || transcript) && (
                          <button className="btn" style={{ marginLeft: 'auto', background: 'var(--success-color)' }} onClick={handleNextTurn}>
                            Tiếp tục ➔
                          </button>
                        )}
                      </>
                    ) : (
                      // System's Turn
                      <>
                        <button className="btn" onClick={() => playTTS(situationData.turns[currentTurnIdx].korean)}>
                          🔊 Phát giọng đọc mẫu
                        </button>
                        <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontStyle: 'italic' }}>
                          Lượt của máy... Nghe xong bấm tiếp tục.
                        </span>
                        <button className="btn" style={{ marginLeft: 'auto' }} onClick={handleNextTurn}>
                          Tiếp tục ➔
                        </button>
                      </>
                    )}
                  </div>

                </div>
              ) : (
                // Dialogue Finished
                <div style={{ background: 'rgba(48, 209, 88, 0.1)', border: '1px solid var(--success-color)', borderRadius: '12px', padding: '2rem', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem' }}>
                  <span style={{ fontSize: '2.5rem' }}>🏆</span>
                  <h3 style={{ color: 'var(--success-color)' }}>Hội thoại hoàn thành xuất sắc!</h3>
                  <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
                    Bạn đã thực hành luyện nói trôi chảy toàn bộ kịch bản đàm thoại của tình huống này.
                  </p>
                  <button className="btn" onClick={() => setSituationData(null)}>
                    Luyện tình huống khác
                  </button>
                </div>
              )}

            </div>
          )}

        </div>
      )}

    </div>
  );
}
