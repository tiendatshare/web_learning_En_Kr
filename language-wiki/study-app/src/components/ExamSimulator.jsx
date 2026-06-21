import React, { useState, useEffect, useRef } from 'react';

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:3001';

export default function ExamSimulator() {
  const [questions, setQuestions] = useState([]);
  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState({}); // mapping questionId -> selectedOptionIdx
  const [timeLeft, setTimeLeft] = useState(1500); // 25 minutes in seconds
  const [isExamStarted, setIsExamStarted] = useState(false);
  const [isExamSubmitted, setIsExamSubmitted] = useState(false);
  const [resultData, setResultData] = useState(null);
  const [loading, setLoading] = useState(false);
  const timerRef = useRef(null);

  useEffect(() => {
    // Clean up timer on unmount
    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, []);

  const fetchQuestions = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/exams/questions`);
      if (res.ok) {
        const data = await res.json();
        setQuestions(data.questions || []);
      }
    } catch (e) {
      console.error('Failed to fetch exam questions:', e);
    } finally {
      setLoading(false);
    }
  };

  const startExam = async () => {
    await fetchQuestions();
    setIsExamStarted(true);
    setIsExamSubmitted(false);
    setResultData(null);
    setSelectedAnswers({});
    setTimeLeft(1500);

    // Start timer interval
    if (timerRef.current) clearInterval(timerRef.current);
    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          autoSubmit();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
  };

  const handleSelectOption = (questionId, optionIdx) => {
    if (isExamSubmitted) return;
    setSelectedAnswers(prev => ({
      ...prev,
      [questionId]: optionIdx
    }));
  };

  const autoSubmit = () => {
    submitExam();
  };

  const submitExam = async (e) => {
    if (e) e.preventDefault();
    if (timerRef.current) clearInterval(timerRef.current);
    
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/exams/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answers: selectedAnswers })
      });
      if (res.ok) {
        const data = await res.json();
        setResultData(data);
        setIsExamSubmitted(true);
      }
    } catch (e) {
      console.error('Failed to submit exam:', e);
    } finally {
      setLoading(false);
    }
  };

  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60).toString().padStart(2, '0');
    const s = (seconds % 60).toString().padStart(2, '0');
    return `${m}:${s}`;
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {!isExamStarted ? (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.25rem', padding: '2rem 0', textAlign: 'center' }}>
          <span style={{ fontSize: '2.5rem' }}>📝</span>
          <h3>Giả Lập Phòng Thi TOPIK Sơ Cấp (Kyung Hee 1)</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', maxWidth: '500px' }}>
            Đề thi gồm 5 câu trắc nghiệm ngữ pháp và cấu trúc câu đại diện, thời gian làm bài tối đa là 25 phút. Điểm số của bạn và lỗi sai sẽ được chẩn đoán liên kết trực tiếp với tri thức Obsidian.
          </p>
          <button className="btn" onClick={startExam}>
            Bắt đầu làm bài thi
          </button>
        </div>
      ) : (
        <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          
          {/* Header Row */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-color)', paddingBottom: '1rem' }}>
            <div>
              <h3 style={{ fontSize: '1.2rem', fontWeight: 600 }}>TOPIK Mock Exam Simulator</h3>
              {!isExamSubmitted && (
                <span style={{ fontSize: '0.85rem', color: timeLeft < 300 ? 'var(--error-color)' : 'var(--text-secondary)' }}>
                  Thời gian còn lại: <strong>{formatTime(timeLeft)}</strong>
                </span>
              )}
            </div>
            <button className="btn btn-secondary" onClick={() => {
              if (timerRef.current) clearInterval(timerRef.current);
              setIsExamStarted(false);
            }}>
              Thoát phòng thi
            </button>
          </div>

          {!isExamSubmitted ? (
            // Active test interface
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 250px', gap: '1.5rem' }}>
              
              {/* Question view */}
              {questions.length > 0 && (
                <div className="fade-in" style={{ background: 'rgba(255,255,255,0.02)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border-color)', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
                  
                  <div>
                    <span style={{ fontSize: '0.8rem', color: 'var(--accent-color)', fontWeight: 'bold' }}>
                      CÂU HỎI {currentIdx + 1} CỦA {questions.length}
                    </span>
                    <h3 style={{ fontSize: '1.15rem', marginTop: '0.5rem', fontWeight: 600, lineHeight: 1.5 }}>
                      {questions[currentIdx].question}
                    </h3>
                  </div>

                  {/* Multiple choice options */}
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                    {questions[currentIdx].options.map((opt, oIdx) => {
                      const isSelected = selectedAnswers[questions[currentIdx].id] === oIdx;
                      return (
                        <div 
                          key={oIdx}
                          onClick={() => handleSelectOption(questions[currentIdx].id, oIdx)}
                          style={{
                            padding: '1rem',
                            borderRadius: '10px',
                            border: `1.5px solid ${isSelected ? 'var(--accent-color)' : 'var(--border-color)'}`,
                            background: isSelected ? 'rgba(10, 132, 255, 0.08)' : 'rgba(0,0,0,0.15)',
                            cursor: 'pointer',
                            transition: 'all 0.2s ease',
                            display: 'flex',
                            alignItems: 'center',
                            gap: '0.75rem'
                          }}
                        >
                          <div style={{
                            width: '20px',
                            height: '20px',
                            borderRadius: '50%',
                            border: `2px solid ${isSelected ? 'var(--accent-color)' : 'var(--text-secondary)'}`,
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            fontSize: '0.7rem'
                          }}>
                            {isSelected && <div style={{ width: '10px', height: '10px', borderRadius: '50%', background: 'var(--accent-color)' }} />}
                          </div>
                          <span style={{ fontSize: '0.95rem' }}>{opt}</span>
                        </div>
                      );
                    })}
                  </div>

                  {/* Action row */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', borderTop: '1px solid var(--border-color)', paddingTop: '1rem' }}>
                    <button 
                      className="btn btn-secondary" 
                      disabled={currentIdx === 0} 
                      onClick={() => setCurrentIdx(prev => prev - 1)}
                    >
                      ◀ Câu trước
                    </button>
                    
                    {currentIdx < questions.length - 1 ? (
                      <button 
                        className="btn" 
                        onClick={() => setCurrentIdx(prev => prev + 1)}
                      >
                        Câu sau ▶
                      </button>
                    ) : (
                      <button 
                        className="btn" 
                        style={{ background: 'var(--success-color)' }} 
                        onClick={submitExam}
                      >
                        Nộp bài thi (Submit)
                      </button>
                    )}
                  </div>

                </div>
              )}

              {/* Sidebar navigator */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <h4 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                  Danh sách câu hỏi
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '0.5rem' }}>
                  {questions.map((q, idx) => {
                    const isAnswered = selectedAnswers[q.id] !== undefined;
                    const isActive = currentIdx === idx;
                    return (
                      <button
                        key={q.id}
                        onClick={() => setCurrentIdx(idx)}
                        style={{
                          width: '40px',
                          height: '40px',
                          borderRadius: '8px',
                          border: `1.5px solid ${isActive ? 'var(--accent-color)' : isAnswered ? 'rgba(255,255,255,0.3)' : 'var(--border-color)'}`,
                          background: isActive ? 'var(--accent-color)' : isAnswered ? 'rgba(255,255,255,0.08)' : 'rgba(0,0,0,0.1)',
                          color: 'white',
                          fontWeight: 'bold',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center'
                        }}
                      >
                        {idx + 1}
                      </button>
                    );
                  })}
                </div>
                
                <div style={{ marginTop: 'auto', background: 'rgba(255,255,255,0.02)', padding: '1rem', borderRadius: '10px', border: '1px solid var(--border-color)', fontSize: '0.8rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                  💡 Bạn có thể nhấp vào số thứ tự để chuyển nhanh giữa các câu hỏi trong đề thi.
                </div>
              </div>

            </div>
          ) : (
            // Results screen
            <div className="fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
              
              {/* Score card banner */}
              <div style={{ 
                background: 'rgba(255,255,255,0.02)', 
                border: '1px solid var(--border-color)', 
                borderRadius: '16px', 
                padding: '2rem', 
                textAlign: 'center', 
                display: 'flex', 
                flexDirection: 'column', 
                alignItems: 'center', 
                gap: '0.75rem' 
              }}>
                <span style={{ fontSize: '0.9rem', color: 'var(--text-secondary)' }}>KẾT QUẢ ĐẠT ĐƯỢC</span>
                <div style={{ 
                  fontSize: '4rem', 
                  fontWeight: 900, 
                  color: resultData.score >= 80 ? 'var(--success-color)' : resultData.score >= 50 ? 'var(--warning-color)' : 'var(--error-color)',
                  fontFamily: 'var(--font-display)'
                }}>
                  {resultData.score}%
                </div>
                <h4 style={{ fontSize: '1.1rem', fontWeight: 600 }}>
                  Đúng {resultData.correctCount} / {resultData.totalQuestions} câu hỏi.
                </h4>
                <button className="btn" style={{ marginTop: '1rem' }} onClick={startExam}>
                  🔁 Làm lại đề thi mới
                </button>
              </div>

              {/* Diagnostics and error mapping */}
              {resultData.diagnostics.length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                  <h4 style={{ fontSize: '1.05rem', color: 'var(--error-color)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    ⚠️ Chẩn Đoán Lỗ Hổng Kiến Thức (Error Diagnostics)
                  </h4>
                  <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                    Bản phân tích chỉ ra các ngữ pháp bạn bị hỏng kiến thức và cung cấp siêu liên kết Obsidian để bạn tra cứu sửa sai ngay:
                  </p>
                  
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
                    {resultData.diagnostics.map((d, index) => (
                      <div 
                        key={index} 
                        style={{ 
                          background: 'rgba(255,69,58,0.03)', 
                          border: '1px solid rgba(255,69,58,0.2)', 
                          borderRadius: '12px', 
                          padding: '1.25rem',
                          display: 'flex',
                          flexDirection: 'column',
                          gap: '0.5rem'
                        }}
                      >
                        <span style={{ fontSize: '0.8rem', color: 'var(--error-color)', fontWeight: 'bold' }}>
                          LỖI SAI #{(index + 1)} (Câu {d.questionId})
                        </span>
                        <p style={{ fontWeight: 600, fontSize: '0.95rem' }}>{d.question}</p>
                        
                        <div style={{ display: 'flex', gap: '1.5rem', fontSize: '0.85rem', margin: '0.25rem 0' }}>
                          <span>Lựa chọn của bạn: <strong style={{ color: 'var(--error-color)' }}>{d.userAnswer}</strong></span>
                          <span>Đáp án đúng: <strong style={{ color: 'var(--success-color)' }}>{d.correctAnswer}</strong></span>
                        </div>

                        <div style={{ background: 'rgba(0,0,0,0.2)', padding: '0.75rem', borderRadius: '6px', fontSize: '0.85rem' }}>
                          <strong>Giải thích sư phạm:</strong> {d.explanation}
                        </div>

                        <div style={{ marginTop: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                          <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Tệp tài liệu cần ôn tập lại trong Obsidian:</span>
                          <code style={{ 
                            background: 'rgba(10,132,255,0.1)', 
                            color: 'var(--accent-color)', 
                            padding: '0.25rem 0.5rem', 
                            borderRadius: '4px', 
                            fontSize: '0.85rem',
                            fontWeight: 'bold'
                          }}>
                            {d.grammarLink}
                          </code>
                        </div>
                      </div>
                    ))}
                  </div>

                </div>
              ) : (
                <div style={{ background: 'rgba(48, 209, 88, 0.1)', border: '1px solid var(--success-color)', borderRadius: '12px', padding: '1.5rem', textAlign: 'center', color: 'var(--success-color)', fontWeight: 'bold' }}>
                  ✓ Tuyệt vời! Bạn không sai câu nào. Bản đồ kiến thức của bạn hoàn toàn hoàn hảo 100%.
                </div>
              )}

            </div>
          )}

        </div>
      )}

    </div>
  );
}
