import React, { useState, useEffect } from 'react';
import ActiveRecallQuizzer from './components/ActiveRecallQuizzer';
import SpeakingMode from './components/SpeakingMode';
import ExamSimulator from './components/ExamSimulator';
import VocabLearner from './components/VocabLearner';



const API_BASE = import.meta.env.VITE_API_BASE || (
  (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
    ? 'http://localhost:3001'
    : ''
);

const LANG_CONFIG = {
  korean: { flag: '🇰🇷', name: 'TOPIK', label: '한국어', ttsLang: 'ko-KR' },
  english: { flag: '🇬🇧', name: 'IELTS', label: 'English', ttsLang: 'en-US' }
};

export default function App() {
  const [activeTab, setActiveTab] = useState('vocab');
  const [dueCards, setDueCards] = useState([]);
  const [sessionQueue, setSessionQueue] = useState([]);
  const [topics, setTopics] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState('');
  const [completedCount, setCompletedCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState('medium'); // medium or hard
  const [sessionFinished, setSessionFinished] = useState(false);
  const [currentLang, setCurrentLang] = useState(() => localStorage.getItem('study_lang') || 'korean');

  // Load due cards and topics on language switch or mount
  useEffect(() => {
    fetchDueCards();
    fetchTopics();
  }, [currentLang]);

  const fetchLanguage = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/language`);
      if (res.ok) {
        const data = await res.json();
        setCurrentLang(data.language || 'korean');
      }
    } catch (e) {
      console.error('Failed to fetch language:', e);
    }
  };

  const switchLanguage = async () => {
    const newLang = currentLang === 'korean' ? 'english' : 'korean';
    setCurrentLang(newLang);
    localStorage.setItem('study_lang', newLang);
    try {
      await fetch(`${API_BASE}/api/language/switch`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language: newLang })
      });
    } catch (e) {
      console.warn('Background language switch sync failed:', e);
    }
  };


  const fetchDueCards = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/cards/due?lang=${currentLang}`);
      if (res.ok) {
        const data = await res.json();
        setDueCards(data.cards || []);
        setSessionQueue(data.cards || []);
        setCompletedCount(0);
        setSessionFinished(data.cards.length === 0);
      }
    } catch (e) {
      console.error('Failed to fetch due cards:', e);
    } finally {
      setLoading(false);
    }
  };

  const fetchTopics = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/topics?lang=${currentLang}`);
      if (res.ok) {
        const data = await res.json();
        setTopics(data.topics || []);
      }
    } catch (e) {
      console.error('Failed to fetch topics:', e);
    }
  };

  const handleTopicChange = async (topicId) => {
    setSelectedTopic(topicId);
    if (!topicId) {
      fetchDueCards();
      return;
    }
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/cards/by-topic?topic=${topicId}&lang=${currentLang}`);
      if (res.ok) {
        const data = await res.json();
        setDueCards(data.cards || []);
        setSessionQueue(data.cards || []);
        setCompletedCount(0);
        setSessionFinished(data.cards.length === 0);
      }
    } catch (e) {
      console.error('Failed to fetch cards by topic:', e);
    } finally {
      setLoading(false);
    }
  };


  const handleReviewSubmitted = async (rating) => {
    if (sessionQueue.length === 0) return;

    const currentCard = sessionQueue[0];
    
    // Submit review to backend Express server
    try {
      const res = await fetch(`${API_BASE}/api/cards/review`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          filePath: currentCard.filePath,
          word: currentCard.word,
          rating: rating
        })
      });

      if (res.ok) {
        const data = await res.json();
        console.log(`Submitted review for ${currentCard.word}:`, data);
      }
    } catch (e) {
      console.error('Failed to submit review to server:', e);
    }

    // Update queues locally
    const updatedQueue = [...sessionQueue];
    const finishedCard = updatedQueue.shift(); // Remove current card

    if (rating === 'again') {
      // Re-add to the end of session queue for learning repeat
      updatedQueue.push(finishedCard);
      setSessionQueue(updatedQueue);
    } else {
      // Card successfully completed for this session
      setSessionQueue(updatedQueue);
      setCompletedCount(prev => prev + 1);
    }

    if (updatedQueue.length === 0) {
      setSessionFinished(true);
    }
  };

  const handleEndSession = async () => {
    try {
      const res = await fetch(`${API_BASE}/api/session/end`, {
        method: 'POST'
      });
      if (res.ok) {
        const data = await res.json();
        alert('Đã gộp và lưu toàn bộ tiến trình vào Git thành công!');
      }
    } catch (e) {
      console.error('Failed to end session:', e);
      alert('Không thể kết nối đến API Server để lưu Git.');
    }
  };

  return (
    <div className="container">
      {/* Header Banner */}
      <header>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
          <h1>{(LANG_CONFIG[currentLang]?.flag || '🌐')} {(LANG_CONFIG[currentLang]?.name || 'Language')} Learning Wiki</h1>
          <button 
            className="btn btn-secondary"
            onClick={switchLanguage}
            title="Chuyển ngôn ngữ học"
            style={{ 
              padding: '0.5rem 1rem', 
              fontSize: '0.85rem',
              display: 'flex', alignItems: 'center', gap: '0.4rem',
              borderRadius: '20px'
            }}
          >
            {currentLang === 'korean' ? '🇬🇧 English' : '🇰🇷 한국어'}
          </button>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap' }}>
          <button 
            className={`btn btn-secondary ${activeTab === 'vocab' ? 'active' : ''}`}
            style={{ borderColor: activeTab === 'vocab' ? 'var(--accent-color)' : 'transparent', borderStyle: 'solid', borderWidth: '1px' }}
            onClick={() => setActiveTab('vocab')}
          >
            📚 Học Từ Vựng
          </button>
          <button 
            className={`btn btn-secondary ${activeTab === 'flashcard' ? 'active' : ''}`}
            style={{ borderColor: activeTab === 'flashcard' ? 'var(--accent-color)' : 'transparent', borderStyle: 'solid', borderWidth: '1px' }}
            onClick={() => setActiveTab('flashcard')}
          >
            🗂️ Ôn Tập (Active Recall)
          </button>
          <button 
            className={`btn btn-secondary ${activeTab === 'speaking' ? 'active' : ''}`}
            style={{ borderColor: activeTab === 'speaking' ? 'var(--accent-color)' : 'transparent', borderStyle: 'solid', borderWidth: '1px' }}
            onClick={() => setActiveTab('speaking')}
          >
            🗣️ Luyện Nói (STT)
          </button>
          <button 
            className={`btn btn-secondary ${activeTab === 'exam' ? 'active' : ''}`}
            style={{ borderColor: activeTab === 'exam' ? 'var(--accent-color)' : 'transparent', borderStyle: 'solid', borderWidth: '1px' }}
            onClick={() => setActiveTab('exam')}
          >
            📝 Thi Thử (Exam Mode)
          </button>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="glass-panel">
        {activeTab === 'vocab' && (
          <VocabLearner currentLang={currentLang} />
        )}
        {activeTab === 'flashcard' && (
          <div className="fade-in">
            {loading ? (
              <div style={{ textAlign: 'center', padding: '3rem 0', color: 'var(--text-secondary)' }}>
                Đang tải danh sách từ vựng đến hạn ôn tập...
              </div>
            ) : sessionFinished ? (
              <div style={{ textAlign: 'center', padding: '3rem 0', display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center' }}>
                <span style={{ fontSize: '3rem' }}>🎉</span>
                <h3 style={{ fontFamily: 'var(--font-display)', fontSize: '1.5rem', fontWeight: 600 }}>
                  Bạn đã hoàn thành tất cả từ vựng hôm nay!
                </h3>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
                  Hẹn gặp lại bạn vào ngày mai để tiếp tục lộ trình ôn tập.
                </p>
                <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
                  <button className="btn" onClick={fetchDueCards}>Tải lại dữ liệu</button>
                  <button className="btn btn-secondary" onClick={handleEndSession}>Lưu tiến trình (Git Commit)</button>
                </div>
              </div>
            ) : (
              <div>
                {/* Topic Selector */}
                <div style={{ 
                  display: 'flex', 
                  flexWrap: 'wrap',
                  gap: '1rem', 
                  alignItems: 'center', 
                  marginBottom: '1.5rem', 
                  background: 'rgba(255,255,255,0.02)', 
                  padding: '1rem', 
                  borderRadius: '12px', 
                  border: '1px solid var(--border-color)' 
                }}>
                  <label style={{ fontSize: '0.9rem', fontWeight: '500', color: 'var(--text-secondary)' }}>
                    Chọn chủ đề học từ vựng:
                  </label>
                  <select
                    value={selectedTopic}
                    onChange={(e) => handleTopicChange(e.target.value)}
                    style={{
                      flex: 1,
                      minWidth: '250px',
                      background: 'rgba(0, 0, 0, 0.25)',
                      border: '1px solid var(--border-color)',
                      borderRadius: '8px',
                      padding: '0.6rem 1rem',
                      color: 'white',
                      outline: 'none',
                      cursor: 'pointer'
                    }}
                  >
                    <option value="">⏰ Từ đến hạn ôn tập hôm nay (Học cuốn chiếu)</option>
                    {topics.map(t => (
                      <option key={t.id} value={t.id}>📖 {t.title}</option>
                    ))}
                  </select>
                </div>

                {/* Stats row */}
                <div className="stats-grid">
                  <div className="stat-card">
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>ĐÃ THUỘC HÔM NAY</div>
                    <div className="stat-val" style={{ color: 'var(--success-color)' }}>
                      {completedCount} từ
                    </div>
                  </div>
                  <div className="stat-card">
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>CÒN LẠI TRONG QUEUE</div>
                    <div className="stat-val" style={{ color: 'var(--warning-color)' }}>
                      {sessionQueue.length} từ
                    </div>
                  </div>
                </div>

                {/* Main Quizzer Card */}
                {sessionQueue.length > 0 && (
                  <ActiveRecallQuizzer 
                    card={sessionQueue[0]} 
                    onReviewSubmitted={handleReviewSubmitted}
                    mode={mode}
                    setMode={setMode}
                    currentLang={currentLang}
                  />
                )}

                {/* Footer buttons */}
                <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '2rem', borderTop: '1px solid var(--border-color)', paddingTop: '1rem' }}>
                  <button className="btn btn-secondary" onClick={handleEndSession}>
                    💾 Ghi nhận tiến độ ngay (Commit)
                  </button>
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'speaking' && (
          <SpeakingMode currentLang={currentLang} />
        )}

        {activeTab === 'exam' && (
          <ExamSimulator />
        )}
      </main>
    </div>
  );
}
