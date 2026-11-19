/**
 * AceSAT Vocabulary Engine for Digital SAT Practice Platform
 * Integrated for Vinschool SAT Team (Mike Pham Bá Hong Son)
 * 100 Word Lists • 1,000 High-Yield SAT Words
 */

(function () {
  'use strict';
  if (window.__ACESAT_INITIALIZED__) return;
  window.__ACESAT_INITIALIZED__ = true;

  const STORAGE_KEY_ACED = 'vinschool_sat_aced_lists_v1';
  const STORAGE_KEY_ACTIVE_LIST = 'vinschool_sat_active_vocab_list_v1';
  const STORAGE_KEY_MASTERED = 'vinschool_sat_mastered_words_v1';

  let rawWordLists = [];
  let allWordsFlat = [];
  let currentListIndex = 0;
  let acedLists = new Set();
  let masteredWords = new Set();

  // Practice state
  let practiceWords = [];
  let currentCardIndex = 0;
  let isCardFlipped = false;

  // Quiz state
  let currentQuiz = null;
  let currentQuizQIndex = 0;

  // Cache DOM
  let el = {};

  function initAceSAT() {
    // 1. Load data
    if (window.ACESAT_VOCAB_DATA && Array.isArray(window.ACESAT_VOCAB_DATA)) {
      rawWordLists = window.ACESAT_VOCAB_DATA.map((dict, listIdx) => {
        const list = [];
        for (const [w, d] of Object.entries(dict)) {
          const item = { word: w.trim(), definition: d.trim(), listIndex: listIdx };
          list.push(item);
          allWordsFlat.push(item);
        }
        return list;
      });
    }

    // 2. Load LocalStorage
    try {
      const savedAced = localStorage.getItem(STORAGE_KEY_ACED);
      if (savedAced) acedLists = new Set(JSON.parse(savedAced));

      const savedMastered = localStorage.getItem(STORAGE_KEY_MASTERED);
      if (savedMastered) masteredWords = new Set(JSON.parse(savedMastered));

      const savedIdx = localStorage.getItem(STORAGE_KEY_ACTIVE_LIST);
      if (savedIdx !== null) currentListIndex = parseInt(savedIdx, 10) || 0;
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }

    if (currentListIndex < 0 || currentListIndex >= rawWordLists.length) {
      currentListIndex = 0;
    }

    cacheDOM();
    bindEvents();
    populateListPicker();
    updateAcedCounterDisplay();
    initPracticeCards();
  }

  function cacheDOM() {
    el = {
      modal: document.getElementById('modal-acesat-vocab'),
      btnClose: document.getElementById('btn-close-acesat-vocab'),
      listPicker: document.getElementById('acesat-list-picker'),
      btnPrevList: document.getElementById('acesat-prev-list-btn'),
      btnNextList: document.getElementById('acesat-next-list-btn'),
      acedIndicator: document.getElementById('acesat-list-aced-indicator'),
      globalSearchInput: document.getElementById('acesat-global-search-input'),
      btnClearSearch: document.getElementById('acesat-clear-search'),
      tabs: document.querySelectorAll('.acesat-tab-btn'),
      panels: document.querySelectorAll('.acesat-tab-panel'),

      // Practice
      practiceTitle: document.getElementById('acesat-practice-list-title'),
      cardCurrentNum: document.getElementById('acesat-card-current-num'),
      cardPosIndicator: document.getElementById('card-pos-indicator'),
      cardStepper: document.getElementById('acesat-card-stepper'),
      flashcard: document.getElementById('acesat-flashcard'),
      cardWordFront: document.getElementById('acesat-card-word-front'),
      frontSpeak: document.getElementById('acesat-front-speak'),
      cardWordBack: document.getElementById('acesat-card-word-back'),
      cardDefBack: document.getElementById('acesat-card-def-back'),
      backSpeak: document.getElementById('acesat-back-speak'),
      btnShuffleCards: document.getElementById('acesat-shuffle-cards-btn'),
      btnFlip: document.getElementById('acesat-flip-btn'),
      btnPrevCard: document.getElementById('acesat-prev-card-btn'),
      btnNextCard: document.getElementById('acesat-next-card-btn'),
      masteryToggleBtn: document.getElementById('acesat-mastery-toggle-btn'),
      masteryStarIcon: document.getElementById('mastery-star-icon'),
      masteryStarText: document.getElementById('mastery-star-text'),

      // Test Quiz
      testQuestionView: document.getElementById('acesat-test-question-view'),
      testResultsView: document.getElementById('acesat-test-results-view'),
      testTitle: document.getElementById('acesat-test-list-title'),
      testQNum: document.getElementById('acesat-test-q-num'),
      testAnsweredBadge: document.getElementById('acesat-test-answered-badge'),
      testProgressFill: document.getElementById('acesat-test-progress-fill'),
      quizTargetWord: document.getElementById('acesat-quiz-target-word'),
      quizSpeakBtn: document.getElementById('acesat-quiz-speak-btn'),
      quizOptions: document.getElementById('acesat-quiz-options'),
      btnQuizPrev: document.getElementById('acesat-quiz-prev-btn'),
      btnQuizNext: document.getElementById('acesat-quiz-next-btn'),

      // Quiz Results
      scoreRing: document.getElementById('acesat-score-ring'),
      resPercent: document.getElementById('acesat-res-percent'),
      resRatio: document.getElementById('acesat-res-ratio'),
      acedCelebration: document.getElementById('acesat-aced-celebration'),
      resNormalMsg: document.getElementById('acesat-res-normal-msg'),
      btnViewWrong: document.getElementById('acesat-btn-view-wrong-answers'),
      wrongCountText: document.getElementById('acesat-wrong-count-text'),
      btnRetake: document.getElementById('acesat-btn-retake-test'),
      btnNextListTest: document.getElementById('acesat-btn-next-list-test'),
      quizBreakdown: document.getElementById('acesat-quiz-review-breakdown'),

      // Search Tab
      searchResultsList: document.getElementById('acesat-search-results-list'),
      searchCountBadge: document.getElementById('acesat-search-count'),

      // External Triggers
      btnOpenVocab: document.getElementById('btn-open-vocab'),
      btnHomeOpenVocab: document.getElementById('btn-home-open-vocab'),
      btnHeroLaunchVocab: document.getElementById('btn-hero-launch-vocab'),
      btnHeroVocabFlashcard: document.getElementById('btn-hero-vocab-flashcard'),
      homeAcedCount: document.getElementById('home-aced-count')
    };
  }

  function saveAcedState() {
    try {
      localStorage.setItem(STORAGE_KEY_ACED, JSON.stringify([...acedLists]));
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
    updateAcedCounterDisplay();
  }

  function saveActiveList() {
    try {
      localStorage.setItem(STORAGE_KEY_ACTIVE_LIST, currentListIndex.toString());
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
  }

  function updateAcedCounterDisplay() {
    if (el.homeAcedCount) {
      el.homeAcedCount.textContent = acedLists.size;
    }
    const badgeStats = document.getElementById('badge-vocab-stats');
    if (badgeStats) {
      const isEn = (window.App && window.App.currentLang === "en");
      badgeStats.textContent = isEn
        ? `${acedLists.size}/100 Lists Aced ★ • 1,000 Words`
        : `${acedLists.size}/100 Lists Aced ★ • 1,000 Từ`;
    }
  }

  function populateListPicker() {
    if (!el.listPicker) return;
    el.listPicker.innerHTML = '';
    rawWordLists.forEach((_, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      const isAced = acedLists.has(idx);
      opt.textContent = `List ${idx + 1} (${idx * 10 + 1}–${idx * 10 + 10})${isAced ? ' ★ Aced' : ''}`;
      el.listPicker.appendChild(opt);
    });
    el.listPicker.value = currentListIndex;
    updateListMetaUI();
  }

  function updateListMetaUI() {
    saveActiveList();
    const isAced = acedLists.has(currentListIndex);
    if (el.acedIndicator) {
      el.acedIndicator.classList.toggle('hidden', !isAced);
    }
    const listTitle = `List ${currentListIndex + 1}`;
    if (el.practiceTitle) el.practiceTitle.textContent = listTitle;
    if (el.testTitle) el.testTitle.textContent = listTitle;
  }

  function switchList(newIdx) {
    if (newIdx < 0) newIdx = rawWordLists.length - 1;
    if (newIdx >= rawWordLists.length) newIdx = 0;
    currentListIndex = newIdx;
    if (el.listPicker) el.listPicker.value = currentListIndex;
    updateListMetaUI();
    initPracticeCards();
    startTestQuiz();
  }

  // --- AUDIO SYNTHESIS ---
  function speakWord(text, onEnd) {
    if (!('speechSynthesis' in window)) return;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'en-US';
    u.rate = 0.95;
    if (onEnd) u.onend = onEnd;
    window.speechSynthesis.speak(u);
  }

  // --- TAB NAVIGATION ---
  function switchTab(tabId) {
    el.tabs.forEach(t => {
      t.classList.toggle('active', t.getAttribute('data-tab') === tabId);
    });
    el.panels.forEach(p => {
      p.classList.toggle('active', p.id === `acesat-tab-${tabId}`);
    });

    if (tabId === 'practice') {
      initPracticeCards();
    } else if (tabId === 'test') {
      if (!currentQuiz || currentQuiz.listIndex !== currentListIndex) {
        startTestQuiz();
      }
    } else if (tabId === 'search') {
      runSearch(el.globalSearchInput ? el.globalSearchInput.value : '');
    }
  }

  // --- 1. 3D FLASHCARDS (GOOGLE MATERIAL DESIGN 3) ---
  function initPracticeCards(shouldShuffle = true) {
    practiceWords = [...(rawWordLists[currentListIndex] || [])];
    if (shouldShuffle) {
      practiceWords.sort(() => Math.random() - 0.5);
    }
    currentCardIndex = 0;
    isCardFlipped = false;
    renderCard();
  }

  function renderStepper() {
    if (!el.cardStepper) return;
    el.cardStepper.innerHTML = '';
    const isEn = (window.App && window.App.currentLang === "en");
    practiceWords.forEach((item, idx) => {
      const chip = document.createElement('div');
      chip.className = 'stepper-chip';
      if (idx === currentCardIndex) chip.classList.add('active');
      const isMastered = masteredWords.has(item.word);
      if (isMastered) chip.classList.add('is-mastered');

      chip.textContent = idx === currentCardIndex ? `• ${idx + 1} •` : (idx + 1);
      chip.title = isEn
        ? `Word ${idx + 1}: ${item.word}${isMastered ? ' (Mastered ★)' : ''}`
        : `Từ ${idx + 1}: ${item.word}${isMastered ? ' (Đã thuộc ★)' : ''}`;

      chip.addEventListener('click', (e) => {
        e.stopPropagation();
        currentCardIndex = idx;
        renderCard();
      });

      el.cardStepper.appendChild(chip);
    });
  }

  function renderCard() {
    if (!practiceWords.length) return;
    const isEn = (window.App && window.App.currentLang === "en");
    const c = practiceWords[currentCardIndex];
    if (el.cardCurrentNum) el.cardCurrentNum.textContent = currentCardIndex + 1;
    if (el.cardPosIndicator) el.cardPosIndicator.textContent = isEn
      ? `Word ${currentCardIndex + 1}/10`
      : `Từ ${currentCardIndex + 1}/10`;

    if (el.cardWordFront) el.cardWordFront.textContent = c.word;
    if (el.cardWordBack) el.cardWordBack.textContent = c.word;
    if (el.cardDefBack) el.cardDefBack.textContent = c.definition;

    // Check Mastery State
    const isMastered = masteredWords.has(c.word);
    if (el.masteryToggleBtn) {
      el.masteryToggleBtn.classList.toggle('is-active', isMastered);
    }
    if (el.masteryStarIcon) {
      el.masteryStarIcon.textContent = isMastered ? '★' : '☆';
    }
    if (el.masteryStarText) {
      el.masteryStarText.textContent = isEn
        ? (isMastered ? 'Mastered' : 'Mark as Mastered')
        : (isMastered ? 'Đã thuộc từ này' : 'Đánh dấu đã thuộc');
    }

    renderStepper();

    // Reset flip smoothly
    isCardFlipped = false;
    if (el.flashcard) el.flashcard.classList.remove('is-flipped');
  }

  function toggleMastery() {
    if (!practiceWords.length) return;
    const c = practiceWords[currentCardIndex];
    if (masteredWords.has(c.word)) {
      masteredWords.delete(c.word);
    } else {
      masteredWords.add(c.word);
    }
    try {
      localStorage.setItem(STORAGE_KEY_MASTERED, JSON.stringify([...masteredWords]));
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
    renderCard();
  }

  function toggleFlipCard() {
    isCardFlipped = !isCardFlipped;
    if (el.flashcard) el.flashcard.classList.toggle('is-flipped', isCardFlipped);
  }

  function nextCard() {
    if (currentCardIndex < practiceWords.length - 1) {
      currentCardIndex++;
    } else {
      currentCardIndex = 0;
    }
    renderCard();
  }

  function prevCard() {
    if (currentCardIndex > 0) {
      currentCardIndex--;
    } else {
      currentCardIndex = practiceWords.length - 1;
    }
    renderCard();
  }

  function shufflePracticeCards() {
    practiceWords.sort(() => Math.random() - 0.5);
    currentCardIndex = 0;
    renderCard();
  }

  // --- 2. TEST QUIZ (Matching Test.swift) ---
  function generateQuiz(listIdx) {
    const list = rawWordLists[listIdx];
    if (!list || !list.length) return null;

    const shuffled = [...list].sort(() => Math.random() - 0.5);
    const questions = shuffled.map(item => {
      const distractors = [];
      const used = new Set([item.definition]);
      let tries = 0;
      while (distractors.length < 3 && tries < 200) {
        tries++;
        const r = allWordsFlat[Math.floor(Math.random() * allWordsFlat.length)];
        if (r.listIndex !== listIdx && !used.has(r.definition)) {
          distractors.push(r.definition);
          used.add(r.definition);
        }
      }
      const opts = [item.definition, ...distractors].sort(() => Math.random() - 0.5);
      return {
        word: item.word,
        correct: item.definition,
        options: opts,
        userSelected: null
      };
    });

    return { listIndex: listIdx, questions: questions };
  }

  function startTestQuiz() {
    currentQuiz = generateQuiz(currentListIndex);
    if (!currentQuiz) return;
    currentQuizQIndex = 0;

    if (el.testQuestionView) el.testQuestionView.classList.remove('hidden');
    if (el.testResultsView) el.testResultsView.classList.add('hidden');
    if (el.quizBreakdown) el.quizBreakdown.classList.add('hidden');

    renderQuizQuestion();
  }

  function renderQuizQuestion() {
    const q = currentQuiz.questions[currentQuizQIndex];
    if (!q) return;

    if (el.testQNum) el.testQNum.textContent = currentQuizQIndex + 1;
    if (el.quizTargetWord) el.quizTargetWord.textContent = q.word;

    const isEn = (window.App && window.App.currentLang === "en");
    const answeredCount = currentQuiz.questions.filter(item => item.userSelected !== null).length;
    if (el.testAnsweredBadge) el.testAnsweredBadge.textContent = isEn ? `${answeredCount}/10 Answered` : `${answeredCount}/10 Đã trả lời`;

    if (el.testProgressFill) {
      el.testProgressFill.style.width = `${((currentQuizQIndex + 1) / currentQuiz.questions.length) * 100}%`;
    }

    if (el.quizOptions) {
      el.quizOptions.innerHTML = '';
      const letters = ['A', 'B', 'C', 'D'];
      q.options.forEach((optText, i) => {
        const btn = document.createElement('button');
        btn.className = 'quiz-opt-btn';
        if (q.userSelected === optText) btn.classList.add('selected');

        btn.innerHTML = `
          <span class="quiz-opt-tag">${letters[i]}</span>
          <span class="quiz-opt-label">${optText}</span>
        `;

        btn.addEventListener('click', () => {
          q.userSelected = optText;
          renderQuizQuestion();
          setTimeout(() => {
            if (currentQuizQIndex < currentQuiz.questions.length - 1) {
              currentQuizQIndex++;
              renderQuizQuestion();
            } else {
              const allAnswered = currentQuiz.questions.every(item => item.userSelected !== null);
              if (allAnswered) finishQuiz();
            }
          }, 200);
        });

        el.quizOptions.appendChild(btn);
      });
    }

    if (el.btnQuizPrev) {
      el.btnQuizPrev.style.visibility = currentQuizQIndex === 0 ? 'hidden' : 'visible';
    }
    if (el.btnQuizNext) {
      el.btnQuizNext.textContent = currentQuizQIndex === currentQuiz.questions.length - 1
        ? (isEn ? 'Finish Quiz ✓' : 'Hoàn thành bài kiểm tra ✓')
        : (isEn ? 'Next Question ›' : 'Câu Kế Tiếp ›');
    }
  }

  function finishQuiz() {
    if (!currentQuiz) return;
    const isEn = (window.App && window.App.currentLang === "en");
    let correct = 0;
    currentQuiz.questions.forEach(q => {
      if (q.userSelected === q.correct) correct++;
    });

    const total = currentQuiz.questions.length;
    const percent = Math.round((correct / total) * 100);

    if (correct === total) {
      acedLists.add(currentQuiz.listIndex);
      saveAcedState();
      populateListPicker();
    }

    if (el.testQuestionView) el.testQuestionView.classList.add('hidden');
    if (el.testResultsView) el.testResultsView.classList.remove('hidden');

    if (el.resPercent) el.resPercent.textContent = `${percent}%`;
    if (el.resRatio) el.resRatio.textContent = isEn ? `${correct} / ${total} Correct` : `${correct} / ${total} Câu Đúng`;
    if (el.wrongCountText) el.wrongCountText.textContent = total - correct;

    // Animate circular ring (r=75 => C = 2*PI*75 = 471.24)
    const C = 2 * Math.PI * 75;
    const offset = C - (percent / 100) * C;
    if (el.scoreRing) {
      el.scoreRing.style.strokeDashoffset = offset;
      if (correct === total) {
        el.scoreRing.classList.add('aced-ring');
      } else {
        el.scoreRing.classList.remove('aced-ring');
      }
    }

    if (correct === total) {
      if (el.acedCelebration) el.acedCelebration.classList.remove('hidden');
      if (el.resNormalMsg) el.resNormalMsg.classList.add('hidden');
      if (el.btnViewWrong) el.btnViewWrong.style.display = 'none';
      speakWord('Congratulations! You aced this vocabulary list!');
    } else {
      if (el.acedCelebration) el.acedCelebration.classList.add('hidden');
      if (el.resNormalMsg) el.resNormalMsg.classList.remove('hidden');
      if (el.btnViewWrong) el.btnViewWrong.style.display = 'inline-flex';
    }
  }

  function toggleQuizBreakdown() {
    if (!el.quizBreakdown || !currentQuiz) return;
    el.quizBreakdown.classList.toggle('hidden');
    if (el.quizBreakdown.classList.contains('hidden')) return;

    const isEn = (window.App && window.App.currentLang === "en");
    el.quizBreakdown.innerHTML = '';
    currentQuiz.questions.forEach((q, i) => {
      const isRight = q.userSelected === q.correct;
      const box = document.createElement('div');
      box.className = `quiz-breakdown-card ${isRight ? 'is-right' : 'is-wrong'}`;
      const badgeText = isRight
        ? (isEn ? '✓ Correct' : '✓ Chính xác')
        : (q.userSelected ? (isEn ? '✕ Incorrect' : '✕ Sai') : (isEn ? 'Unanswered' : 'Chưa trả lời'));
      const pickLabel = isEn ? 'Your pick:' : 'Em đã chọn:';
      const noPick = isEn ? '<em>Not selected</em>' : '<em>Chưa chọn</em>';
      const ansLabel = isEn ? 'Correct answer:' : 'Đáp án đúng:';
      box.innerHTML = `
        <div class="q-bk-header">
          <strong>${i + 1}. ${q.word}</strong>
          <span class="q-bk-badge ${isRight ? 'right' : 'wrong'}">
            ${badgeText}
          </span>
        </div>
        <div class="q-bk-ans"><strong>${pickLabel}</strong> ${q.userSelected || noPick}</div>
        ${!isRight ? `<div class="q-bk-ans correct"><strong>${ansLabel}</strong> ${q.correct}</div>` : ''}
      `;
      el.quizBreakdown.appendChild(box);
    });
  }

  // --- 3. GLOBAL SEARCH ---
  function runSearch(query) {
    query = (query || '').toLowerCase().trim();
    if (!el.searchResultsList) return;
    const isEn = (window.App && window.App.currentLang === "en");

    if (!query) {
      renderSearchBatch(allWordsFlat.slice(0, 30), isEn ? 'Showing first 30 words. Type to search vocabulary...' : 'Hiển thị 30 từ đầu tiên. Hãy gõ từ cần tra cứu...');
      return;
    }

    const matches = allWordsFlat.filter(item =>
      item.word.toLowerCase().includes(query) || item.definition.toLowerCase().includes(query)
    );

    renderSearchBatch(matches.slice(0, 50), isEn ? `Found ${matches.length} words matching "${query}":` : `Tìm thấy ${matches.length} từ phù hợp với "${query}":`);
  }

  function renderSearchBatch(items, infoText) {
    const isEn = (window.App && window.App.currentLang === "en");
    el.searchResultsList.innerHTML = `<div class="search-info-bar">${infoText}</div>`;
    if (!items.length) {
      el.searchResultsList.innerHTML += `<div class="search-no-result">${isEn ? 'No vocabulary words found.' : 'Không tìm thấy từ vựng nào phù hợp.'}</div>`;
      return;
    }

    items.forEach(item => {
      const row = document.createElement('div');
      row.className = 'search-vocab-row';
      row.innerHTML = `
        <div class="sr-word-row">
          <span class="sr-word"><strong>${item.word}</strong></span>
          <span class="sr-list-tag" title="Mở danh sách này">List ${item.listIndex + 1}</span>
        </div>
        <div class="sr-def">${item.definition}</div>
      `;

      row.addEventListener('click', () => {
        switchList(item.listIndex);
        const cardIdx = practiceWords.findIndex(w => w.word.toLowerCase() === item.word.toLowerCase());
        if (cardIdx !== -1) {
          currentCardIndex = cardIdx;
        }
        switchTab('practice');
        renderCard();
        speakWord(item.word);
      });

      el.searchResultsList.appendChild(row);
    });
  }

  // --- MODAL CONTROLLER & HOOKS ---
  function openModal(defaultTab = 'practice') {
    if (window.pauseTimer) window.pauseTimer();
    if (el.modal) el.modal.classList.remove('hidden');

    // On every modal open, pick a random list and shuffle flashcards
    // so the student is greeted with a fresh SAT word instead of always starting on "Abhor"
    if (rawWordLists && rawWordLists.length > 0) {
      const randomListIdx = Math.floor(Math.random() * rawWordLists.length);
      currentListIndex = randomListIdx;
      if (el.listPicker) el.listPicker.value = currentListIndex;
      updateListMetaUI();
    }

    switchTab(defaultTab);
  }

  function closeModal() {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (el.modal) el.modal.classList.add('hidden');
    if (window.syncTimerState) window.syncTimerState();
  }

  // --- EVENT BINDINGS ---
  function bindEvents() {
    if (el.btnClose) el.btnClose.addEventListener('click', closeModal);
    if (el.modal) {
      el.modal.addEventListener('click', (e) => {
        if (e.target === el.modal) closeModal();
      });
    }

    if (el.listPicker) {
      el.listPicker.addEventListener('change', (e) => {
        switchList(parseInt(e.target.value, 10) || 0);
      });
    }
    if (el.btnPrevList) el.btnPrevList.addEventListener('click', () => switchList(currentListIndex - 1));
    if (el.btnNextList) el.btnNextList.addEventListener('click', () => switchList(currentListIndex + 1));

    // Tabs
    el.tabs.forEach(t => {
      t.addEventListener('click', () => switchTab(t.getAttribute('data-tab')));
    });

    // Practice Tab
    if (el.flashcard) el.flashcard.addEventListener('click', toggleFlipCard);
    if (el.btnFlip) el.btnFlip.addEventListener('click', toggleFlipCard);
    if (el.btnNextCard) el.btnNextCard.addEventListener('click', nextCard);
    if (el.btnPrevCard) el.btnPrevCard.addEventListener('click', prevCard);
    if (el.btnShuffleCards) el.btnShuffleCards.addEventListener('click', shufflePracticeCards);
    if (el.masteryToggleBtn) el.masteryToggleBtn.addEventListener('click', toggleMastery);

    if (el.frontSpeak) {
      el.frontSpeak.addEventListener('click', (e) => {
        e.stopPropagation();
        const c = practiceWords[currentCardIndex];
        if (c) speakWord(c.word);
      });
    }
    if (el.backSpeak) {
      el.backSpeak.addEventListener('click', (e) => {
        e.stopPropagation();
        const c = practiceWords[currentCardIndex];
        if (c) speakWord(`${c.word}: ${c.definition}`);
      });
    }

    // Test Tab
    if (el.quizSpeakBtn) {
      el.quizSpeakBtn.addEventListener('click', () => {
        const q = currentQuiz.questions[currentQuizQIndex];
        if (q) speakWord(q.word);
      });
    }
    if (el.btnQuizPrev) {
      el.btnQuizPrev.addEventListener('click', () => {
        if (currentQuizQIndex > 0) {
          currentQuizQIndex--;
          renderQuizQuestion();
        }
      });
    }
    if (el.btnQuizNext) {
      el.btnQuizNext.addEventListener('click', () => {
        if (currentQuizQIndex < currentQuiz.questions.length - 1) {
          currentQuizQIndex++;
          renderQuizQuestion();
        } else {
          finishQuiz();
        }
      });
    }
    if (el.btnViewWrong) el.btnViewWrong.addEventListener('click', toggleQuizBreakdown);
    if (el.btnRetake) el.btnRetake.addEventListener('click', startTestQuiz);
    if (el.btnNextListTest) {
      el.btnNextListTest.addEventListener('click', () => {
        switchList(currentListIndex + 1);
        switchTab('test');
      });
    }

    // Search Tab
    if (el.globalSearchInput) {
      el.globalSearchInput.addEventListener('input', (e) => {
        const val = e.target.value;
        if (el.btnClearSearch) el.btnClearSearch.classList.toggle('hidden', !val);
        switchTab('search');
        runSearch(val);
      });
    }
    if (el.btnClearSearch) {
      el.btnClearSearch.addEventListener('click', () => {
        if (el.globalSearchInput) {
          el.globalSearchInput.value = '';
          el.btnClearSearch.classList.add('hidden');
          runSearch('');
        }
      });
    }

    // External Open Triggers
    if (el.btnOpenVocab) el.btnOpenVocab.addEventListener('click', () => openModal('practice'));
    if (el.btnHomeOpenVocab) el.btnHomeOpenVocab.addEventListener('click', () => openModal('practice'));
    if (el.btnHeroLaunchVocab) el.btnHeroLaunchVocab.addEventListener('click', () => openModal('practice'));
    if (el.btnHeroVocabFlashcard) el.btnHeroVocabFlashcard.addEventListener('click', () => openModal('practice'));

    // Global Keyboard Shortcuts when modal is open
    window.addEventListener('keydown', (e) => {
      if (!el.modal || el.modal.classList.contains('hidden')) return;
      if (e.key === 'Escape') {
        closeModal();
        return;
      }

      // In Practice Flashcards Tab
      const practiceTab = document.getElementById('acesat-tab-practice');
      if (practiceTab && practiceTab.classList.contains('active')) {
        if (e.code === 'Space' || e.key === 'Enter') {
          e.preventDefault();
          toggleFlipCard();
        } else if (e.key === 'ArrowRight') {
          e.preventDefault();
          nextCard();
        } else if (e.key === 'ArrowLeft') {
          e.preventDefault();
          prevCard();
        } else if (e.key === 's' || e.key === 'S') {
          e.preventDefault();
          const c = practiceWords[currentCardIndex];
          if (c) speakWord(isCardFlipped ? `${c.word}: ${c.definition}` : c.word);
        } else if (e.key === 'm' || e.key === 'M') {
          e.preventDefault();
          toggleMastery();
        }
      }
    });
  }

  // Expose global controller
  window.openAceSATVocabModal = openModal;
  window.closeAceSATVocabModal = closeModal;

  document.addEventListener('DOMContentLoaded', initAceSAT);
})();
