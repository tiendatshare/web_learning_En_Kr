import React, { useState, useEffect, useRef } from 'react';

export default function ActiveRecallQuizzer({ card, onReviewSubmitted, mode, setMode, currentLang }) {
  const [typedAnswer, setTypedAnswer] = useState('');
  const [isChecked, setIsChecked] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [showHint, setShowHint] = useState(false);
  const inputRef = useRef(null);

  useEffect(() => {
    // Reset state for new card
    setTypedAnswer('');
    setIsChecked(false);
    setIsCorrect(false);
    setShowHint(false);
    if (inputRef.current) inputRef.current.focus();

    // Auto-play default TTS when card load
    playTTS(card.word, false);
  }, [card]);

  // Keyboard shortcuts for ratings (1-4 keys)
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (isChecked) {
        if (e.key === '1') {
          handleRating('again');
        } else if (e.key === '2') {
          handleRating('hard');
        } else if (e.key === '3') {
          handleRating('good');
        } else if (e.key === '4') {
          handleRating('easy');
        }
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isChecked, card]);

  const playTTS = (text, phoneticMode = false) => {
    let textToSpeak = text;
    if (phoneticMode && card.cognitiveData && card.cognitiveData.phonetics) {
      // Extract Korean phonetic transcription from brackets e.g. [책쌍]
      const match = card.cognitiveData.phonetics.match(/\[([^\]]+)\]/);
      if (match) {
        textToSpeak = match[1];
      }
    }

    const ttsLang = currentLang === 'english' ? 'english' : 'korean';
    const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:3001';
    const audioUrl = `${API_BASE}/api/tts?text=${encodeURIComponent(textToSpeak)}&lang=${ttsLang}`;
    const audio = new Audio(audioUrl);
    audio.play().catch(err => {
      console.warn("Neural TTS play failed, falling back to Web Speech API:", err);
      if (window.speechSynthesis) {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(textToSpeak);
        utterance.lang = currentLang === 'english' ? 'en-US' : 'ko-KR';
        window.speechSynthesis.speak(utterance);
      }
    });
  };

  const normalizeText = (str) => {
    if (!str) return '';
    // Strip parentheses and their contents (e.g. "nhất (so sánh nhất)" -> "nhất")
    const cleanStr = str.replace(/\([^)]*\)/g, "");
    return cleanStr
      .toLowerCase()
      .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()?"]/g, "") // remove punctuation
      .replace(/\b(i'm|im)\b/g, "i am")
      .replace(/\b(what's|whats)\b/g, "what is")
      .replace(/\b(he's|hes)\b/g, "he is")
      .replace(/\b(she's|shes)\b/g, "she is")
      .replace(/\b(it's|its)\b/g, "it is")
      .replace(/\b(we're|were)\b/g, "we are")
      .replace(/\b(they're|theyre)\b/g, "they are")
      .replace(/\s+/g, " ")
      .trim();
  };

  const handleCheck = (e) => {
    if (e) e.preventDefault();
    if (!typedAnswer.trim()) return;

    const correct = normalizeText(typedAnswer) === normalizeText(card.word);
    setIsCorrect(correct);
    setIsChecked(true);
  };

  const handleRating = (rating) => {
    onReviewSubmitted(rating);
  };

  // Helper to generate Medium Mode hints (e.g. 책상 -> _ _ )
  const renderHint = () => {
    const chars = card.word.split('');
    return chars.map((char, index) => {
      // Keep spaces as empty elements
      if (char === ' ') return <span key={index} style={{ width: '1rem' }} />;
      return (
        <span key={index} className="hint-char">
          {showHint ? char : '_'}
        </span>
      );
    });
  };

  return (
    <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {/* Target Word and Mode selection */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: '0.85rem', background: '#0a84ff', padding: '0.3rem 0.6rem', borderRadius: '4px', fontWeight: 'bold' }}>
          ACTIVE RECALL QUIZZER
        </span>
        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button 
            className={`btn btn-secondary ${mode === 'medium' ? 'active' : ''}`} 
            style={{ padding: '0.2rem 0.5rem', fontSize: '0.75rem', border: mode === 'medium' ? '1px solid #0a84ff' : 'none' }}
            onClick={() => setMode('medium')}
          >
            Medium (Gợi ý)
          </button>
          <button 
            className={`btn btn-secondary ${mode === 'hard' ? 'active' : ''}`} 
            style={{ padding: '0.2rem 0.5rem', fontSize: '0.75rem', border: mode === 'hard' ? '1px solid #0a84ff' : 'none' }}
            onClick={() => setMode('hard')}
          >
            Hard (Không gợi ý)
          </button>
        </div>
      </div>

      {/* Prompts */}
      <div style={{ textAlignment: 'center', padding: '1rem 0', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '0.5rem' }}>
        <span style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>{currentLang === 'english' ? 'Dịch từ này sang tiếng Anh:' : 'Dịch từ này sang tiếng Hàn:'}</span>
        <h2 style={{ fontSize: '2.2rem', fontWeight: 'bold', fontFamily: 'var(--font-display)' }}>
          "{card.meaning}"
        </h2>
        
        {/* Dual Loa TTS buttons */}
        <div className="audio-contrast">
          <button className="speaker-btn" title="Phát âm chuẩn (Standard spelling)" onClick={() => playTTS(card.word, false)}>
            🔊
          </button>
          <button className="speaker-btn" title="Phát âm thực tế (Phonetic assimilation)" onClick={() => playTTS(card.word, true)}>
            🗣️
          </button>
        </div>
      </div>

      {/* Hints for Medium Mode */}
      {mode === 'medium' && (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '0.5rem' }}>
          <div className="hint-container">
            {renderHint()}
          </div>
          <button 
            className="btn btn-secondary" 
            style={{ padding: '0.2rem 0.6rem', fontSize: '0.75rem' }} 
            onClick={() => setShowHint(!showHint)}
          >
            {showHint ? "Ẩn gợi ý" : "Hiện gợi ý chữ cái"}
          </button>
        </div>
      )}

      {/* Spelling input */}
      <form onSubmit={handleCheck} style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
        <input
          ref={inputRef}
          type="text"
          value={typedAnswer}
          onChange={(e) => setTypedAnswer(e.target.value)}
          disabled={isChecked}
          placeholder={currentLang === 'english' ? "Gõ chữ tiếng Anh ở đây..." : "Gõ chữ tiếng Hàn ở đây (ví dụ: 책상)..."}
          autoFocus
        />
        
        {!isChecked && (
          <button type="submit" className="btn" style={{ width: '100%' }}>
            Kiểm tra (Enter)
          </button>
        )}
      </form>

      {/* Check details & rating buttons */}
      {isChecked && (
        <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem', marginTop: '0.5rem' }}>
          
          {/* Result Banner */}
          <div style={{ 
            padding: '1rem', 
            borderRadius: '10px', 
            textAlign: 'center', 
            fontWeight: 'bold',
            background: isCorrect ? 'rgba(48, 209, 88, 0.15)' : 'rgba(255, 69, 58, 0.15)',
            border: `1px solid ${isCorrect ? 'var(--success-color)' : 'var(--error-color)'}`,
            color: isCorrect ? 'var(--success-color)' : 'var(--error-color)'
          }}>
            {isCorrect ? "✓ Trả lời chính xác!" : `✗ Sai rồi! Đáp án đúng: "${card.word}"`}
          </div>

          {/* Sped repetition ratings */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', textAlign: 'center' }}>
              Hãy tự đánh giá mức độ ghi nhớ để lên lịch ôn tập:
            </span>
            <div className="rating-group">
              <button className="btn-rating again" onClick={() => handleRating('again')}>🔴 Again</button>
              <button className="btn-rating hard" onClick={() => handleRating('hard')}>🟡 Hard</button>
              <button className="btn-rating good" onClick={() => handleRating('good')}>🟢 Good</button>
              <button className="btn-rating easy" onClick={() => handleRating('easy')}>🔵 Easy</button>
            </div>
          </div>

          {/* Cognitive Context Section */}
          <div style={{ 
            background: 'rgba(255,255,255,0.02)', 
            border: '1px solid var(--border-color)', 
            borderRadius: '12px', 
            padding: '1.25rem',
            display: 'flex',
            flexDirection: 'column',
            gap: '1rem'
          }}>
            <h4 style={{ fontSize: '0.95rem', color: 'var(--accent-color)', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.4rem' }}>
              🧠 Gợi ý liên tưởng & Ngữ cảnh Sư phạm
            </h4>
            
            {/* Phonetic guide */}
            <div>
              <span style={{ fontWeight: '600', fontSize: '0.85rem', display: 'block', color: 'var(--text-secondary)' }}>
                {currentLang === 'english' ? 'Phiên âm & Phát âm gợi ý:' : 'Bẫy biến âm:'}
              </span>
              <p style={{ fontSize: '0.9rem', marginTop: '0.25rem' }}>
                {card.cognitiveData && card.cognitiveData.phonetics ? card.cognitiveData.phonetics : (currentLang === 'english' ? "Không có phiên âm." : "Không có lưu ý biến âm.")}
              </p>
            </div>

            {/* Hanja / Word Family */}
            <div>
              <span style={{ fontWeight: '600', fontSize: '0.85rem', display: 'block', color: 'var(--text-secondary)' }}>
                {currentLang === 'english' ? 'Mạng Liên tưởng Nơ-ron (Word Family / Synonyms / Antonyms):' : 'Gốc Hán-Hàn (Hanja Root Tree):'}
              </span>
              <p style={{ fontSize: '0.9rem', marginTop: '0.25rem', whiteSpace: 'pre-wrap' }}>
                {card.cognitiveData && card.cognitiveData.hanja ? card.cognitiveData.hanja : (currentLang === 'english' ? "Không có phân tích từ vựng liên tưởng." : "Không có phân tích gốc Hán.")}
              </p>
            </div>

            {/* Dialogue / Chunking */}
            <div>
              <span style={{ fontWeight: '600', fontSize: '0.85rem', display: 'block', color: 'var(--text-secondary)' }}>
                {currentLang === 'english' ? 'Phát triển Cụm từ (Chunking Progression):' : 'Độc thoại Phản xạ (Output Shadowing Scenario):'}
              </span>
              <p style={{ fontSize: '0.9rem', marginTop: '0.25rem', whiteSpace: 'pre-wrap', fontStyle: 'italic', color: '#ffd60a' }}>
                {card.cognitiveData && card.cognitiveData.dialogue ? card.cognitiveData.dialogue : (currentLang === 'english' ? "Không có kịch bản cụm từ." : "Không có kịch bản hội thoại.")}
              </p>
            </div>

          </div>

        </div>
      )}

    </div>
  );
}
