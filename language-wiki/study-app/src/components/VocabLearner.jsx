import React, { useState, useEffect, useRef } from 'react';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:3001';

export default function VocabLearner() {
  const [topics, setTopics] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState('');
  const [cards, setCards] = useState([]);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [showMeaning, setShowMeaning] = useState(false);
  const [showPronunciation, setShowPronunciation] = useState(false);
  const [learnedWords, setLearnedWords] = useState(new Set());
  const [loading, setLoading] = useState(false);
  const [studyMode, setStudyMode] = useState('browse'); // 'browse' | 'test'
  const [testInput, setTestInput] = useState('');
  const [testResult, setTestResult] = useState(null);
  const [currentLang, setCurrentLang] = useState('korean');
  const inputRef = useRef(null);

  useEffect(() => {
    fetchTopics();
    // Fetch current language
    fetch(`${API_BASE}/api/language`)
      .then(res => res.json())
      .then(data => setCurrentLang(data.language || 'korean'))
      .catch(() => {});
  }, []);

  const fetchTopics = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/topics`);
      if (res.ok) {
        const data = await res.json();
        setTopics(data.topics || []);
      }
    } catch (e) {
      console.error('Failed to fetch topics:', e);
    }
  };

  const loadTopicCards = async (topicId) => {
    setSelectedTopic(topicId);
    if (!topicId) {
      setCards([]);
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/cards/by-topic?topic=${topicId}`);
      if (res.ok) {
        const data = await res.json();
        setCards(data.cards || []);
        setCurrentIdx(0);
        setShowMeaning(false);
        setShowPronunciation(false);
        setLearnedWords(new Set());
        setTestInput('');
        setTestResult(null);
      }
    } catch (e) {
      console.error('Failed to load topic cards:', e);
    } finally {
      setLoading(false);
    }
  };

  const playWordTTS = (word) => {
    const ttsLang = currentLang === 'english' ? 'english' : 'korean';
    const audioUrl = `${API_BASE}/api/tts?text=${encodeURIComponent(word)}&lang=${ttsLang}`;
    const audio = new Audio(audioUrl);
    audio.play().catch(err => {
      console.warn("Neural TTS play failed, falling back to Web Speech API:", err);
      if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(word);
        utterance.lang = currentLang === 'english' ? 'en-US' : 'ko-KR';
        utterance.rate = 0.85; // Slightly slower for learning
        window.speechSynthesis.speak(utterance);
      }
    });
  };

  const handleNext = () => {
    if (currentIdx < cards.length - 1) {
      setCurrentIdx(prev => prev + 1);
      setShowMeaning(false);
      setShowPronunciation(false);
      setTestInput('');
      setTestResult(null);
    }
  };

  const handlePrev = () => {
    if (currentIdx > 0) {
      setCurrentIdx(prev => prev - 1);
      setShowMeaning(false);
      setShowPronunciation(false);
      setTestInput('');
      setTestResult(null);
    }
  };

  const handleMarkLearned = () => {
    const currentWord = cards[currentIdx]?.word;
    if (currentWord) {
      setLearnedWords(prev => {
        const next = new Set(prev);
        if (next.has(currentWord)) {
          next.delete(currentWord);
        } else {
          next.add(currentWord);
        }
        return next;
      });
    }
  };

  const handleTestCheck = (e) => {
    if (e) e.preventDefault();
    if (!testInput.trim()) return;
    const correct = testInput.trim() === cards[currentIdx].word.trim();
    setTestResult(correct);
  };

  const currentCard = cards[currentIdx];
  const progress = cards.length > 0 ? Math.round((learnedWords.size / cards.length) * 100) : 0;

  return (
    <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {/* Topic Selector */}
      <div style={{
        display: 'flex', flexWrap: 'wrap', gap: '1rem', alignItems: 'center',
        background: 'rgba(255,255,255,0.02)', padding: '1rem', borderRadius: '12px',
        border: '1px solid var(--border-color)'
      }}>
        <label style={{ fontSize: '0.9rem', fontWeight: '500', color: 'var(--text-secondary)' }}>
          📖 Chọn chủ đề học:
        </label>
        <select
          value={selectedTopic}
          onChange={(e) => loadTopicCards(e.target.value)}
          style={{
            flex: 1, minWidth: '250px',
            background: 'rgba(0, 0, 0, 0.25)',
            border: '1px solid var(--border-color)',
            borderRadius: '8px', padding: '0.6rem 1rem',
            color: 'white', outline: 'none', cursor: 'pointer'
          }}
        >
          <option value="">-- Chọn chủ đề từ vựng --</option>
          {topics.map(t => (
            <option key={t.id} value={t.id}>📖 {t.title}</option>
          ))}
        </select>
      </div>

      {/* Mode Toggle */}
      {cards.length > 0 && (
        <div style={{ display: 'flex', gap: '0.5rem', justifyContent: 'center' }}>
          <button 
            className={`btn ${studyMode === 'browse' ? '' : 'btn-secondary'}`}
            style={{ padding: '0.4rem 1rem', fontSize: '0.85rem' }}
            onClick={() => setStudyMode('browse')}
          >
            👁️ Xem từ (Browse)
          </button>
          <button 
            className={`btn ${studyMode === 'test' ? '' : 'btn-secondary'}`}
            style={{ padding: '0.4rem 1rem', fontSize: '0.85rem' }}
            onClick={() => { setStudyMode('test'); setTestInput(''); setTestResult(null); }}
          >
            ✍️ Viết từ (Test)
          </button>
        </div>
      )}

      {/* Loading */}
      {loading && (
        <div style={{ textAlign: 'center', padding: '2rem', color: 'var(--text-secondary)' }}>
          Đang tải từ vựng...
        </div>
      )}

      {/* No topic selected */}
      {!selectedTopic && !loading && (
        <div style={{ textAlign: 'center', padding: '3rem 0', color: 'var(--text-secondary)' }}>
          <span style={{ fontSize: '2.5rem', display: 'block', marginBottom: '1rem' }}>📚</span>
          <p>Hãy chọn một chủ đề ở trên để bắt đầu học từ vựng.</p>
        </div>
      )}

      {/* Empty topic */}
      {selectedTopic && !loading && cards.length === 0 && (
        <div style={{ textAlign: 'center', padding: '2rem', color: 'var(--warning-color)' }}>
          Không tìm thấy từ vựng trong chủ đề này.
        </div>
      )}

      {/* Main Card Area */}
      {currentCard && !loading && (
        <>
          {/* Progress Bar */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <div style={{
              flex: 1, height: '6px', background: 'rgba(255,255,255,0.08)',
              borderRadius: '3px', overflow: 'hidden'
            }}>
              <div style={{
                height: '100%', width: `${progress}%`,
                background: 'linear-gradient(90deg, var(--accent-color), var(--success-color))',
                borderRadius: '3px', transition: 'width 0.3s ease'
              }} />
            </div>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', minWidth: '80px' }}>
              {learnedWords.size}/{cards.length} thuộc
            </span>
          </div>

          {/* Word Card */}
          <div className="fade-in" style={{
            background: 'rgba(255, 255, 255, 0.04)',
            border: `1px solid ${learnedWords.has(currentCard.word) ? 'var(--success-color)' : 'var(--accent-color)'}`,
            boxShadow: `0 0 20px ${learnedWords.has(currentCard.word) ? 'rgba(48,209,88,0.15)' : 'var(--accent-glow)'}`,
            borderRadius: '16px', padding: '2rem',
            display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.25rem',
            position: 'relative'
          }}>
            {/* Card counter */}
            <span style={{
              position: 'absolute', top: '1rem', right: '1rem',
              fontSize: '0.75rem', color: 'var(--text-secondary)',
              background: 'rgba(255,255,255,0.06)', padding: '0.2rem 0.6rem', borderRadius: '4px'
            }}>
              {currentIdx + 1} / {cards.length}
            </span>

            {/* Learned badge */}
            {learnedWords.has(currentCard.word) && (
              <span style={{
                position: 'absolute', top: '1rem', left: '1rem',
                fontSize: '0.7rem', color: 'var(--success-color)',
                background: 'rgba(48,209,88,0.1)', padding: '0.2rem 0.5rem', borderRadius: '4px',
                fontWeight: 600
              }}>
                ✓ Đã thuộc
              </span>
            )}

            {/* Korean Word — BIG */}
            <div style={{ textAlign: 'center' }}>
              <h2 style={{
                fontSize: '3rem', fontWeight: 700,
                fontFamily: 'var(--font-display)',
                background: 'linear-gradient(135deg, #f5f5f7, #d1d1d6)',
                WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent'
              }}>
                {currentCard.word}
              </h2>
            </div>

            {/* TTS Button for single word */}
            <button
              onClick={() => playWordTTS(currentCard.word)}
              style={{
                background: 'var(--accent-color)', border: 'none',
                width: '56px', height: '56px', borderRadius: '50%',
                cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
                fontSize: '1.5rem', color: 'white',
                transition: 'all 0.2s ease', boxShadow: '0 4px 15px var(--accent-glow)'
              }}
              title="Nghe phát âm từ này"
            >
              🔊
            </button>

            {/* Pronunciation reveal */}
            <div style={{ textAlign: 'center' }}>
              {showPronunciation ? (
                <p className="fade-in" style={{ fontSize: '1.1rem', color: 'var(--warning-color)', fontStyle: 'italic' }}>
                  ({currentCard.pronunciation})
                </p>
              ) : (
                <button
                  className="btn btn-secondary"
                  style={{ padding: '0.3rem 1rem', fontSize: '0.8rem' }}
                  onClick={() => setShowPronunciation(true)}
                >
                  Xem phiên âm
                </button>
              )}
            </div>

            {/* Test Mode: Spelling input */}
            {studyMode === 'test' && (
              <form onSubmit={handleTestCheck} style={{
                width: '100%', maxWidth: '400px',
                display: 'flex', flexDirection: 'column', gap: '0.5rem'
              }}>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', textAlign: 'center' }}>
                  {currentLang === 'english' ? 'Gõ lại từ tiếng Anh:' : 'Gõ lại từ tiếng Hàn:'}
                </p>
                <input
                  ref={inputRef}
                  type="text"
                  value={testInput}
                  onChange={(e) => setTestInput(e.target.value)}
                  disabled={testResult !== null}
                  placeholder={currentLang === 'english' ? 'Gõ từ tiếng Anh...' : 'Gõ từ tiếng Hàn...'}
                  autoFocus
                  style={{ fontSize: '1.1rem' }}
                />
                {testResult === null && (
                  <button type="submit" className="btn" style={{ width: '100%' }}>Kiểm tra</button>
                )}
                {testResult !== null && (
                  <div className="fade-in" style={{
                    padding: '0.75rem', borderRadius: '8px', textAlign: 'center', fontWeight: 'bold',
                    background: testResult ? 'rgba(48,209,88,0.15)' : 'rgba(255,69,58,0.15)',
                    border: `1px solid ${testResult ? 'var(--success-color)' : 'var(--error-color)'}`,
                    color: testResult ? 'var(--success-color)' : 'var(--error-color)'
                  }}>
                    {testResult ? '✓ Chính xác!' : `✗ Sai. Đáp án: ${currentCard.word}`}
                  </div>
                )}
              </form>
            )}

            {/* Meaning reveal */}
            <div style={{ textAlign: 'center', minHeight: '50px', display: 'flex', alignItems: 'center' }}>
              {showMeaning ? (
                <div className="fade-in">
                  <p style={{ fontSize: '1.4rem', fontWeight: 600, color: 'var(--accent-color)' }}>
                    {currentCard.meaning}
                  </p>
                  {currentCard.cognitiveData?.hanja && currentCard.cognitiveData.hanja !== "Không tìm thấy thông tin gốc Hán-Hàn." && (
                    <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                      🏛️ {currentCard.cognitiveData.hanja}
                    </p>
                  )}
                </div>
              ) : (
                <button className="btn" onClick={() => setShowMeaning(true)} style={{ fontSize: '1rem' }}>
                  🔓 Xem nghĩa
                </button>
              )}
            </div>

            {/* Mark learned button */}
            <button
              className={`btn ${learnedWords.has(currentCard.word) ? '' : 'btn-secondary'}`}
              style={{
                padding: '0.4rem 1rem', fontSize: '0.8rem',
                background: learnedWords.has(currentCard.word) ? 'var(--success-color)' : undefined
              }}
              onClick={handleMarkLearned}
            >
              {learnedWords.has(currentCard.word) ? '✓ Đã thuộc' : '☐ Đánh dấu thuộc'}
            </button>
          </div>

          {/* Navigation buttons */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <button
              className="btn btn-secondary"
              onClick={handlePrev}
              disabled={currentIdx === 0}
              style={{ opacity: currentIdx === 0 ? 0.4 : 1 }}
            >
              ← Từ trước
            </button>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
              Dùng phím ← → để chuyển từ
            </span>
            <button
              className="btn"
              onClick={handleNext}
              disabled={currentIdx >= cards.length - 1}
              style={{ opacity: currentIdx >= cards.length - 1 ? 0.4 : 1 }}
            >
              Từ tiếp →
            </button>
          </div>
        </>
      )}
    </div>
  );
}
