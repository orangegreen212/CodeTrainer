// Internationalization - EN/UK translations

const translations = {
    en: {
        "header.title": "SQL & Python Interview Trainer",
        "header.subtitle": "Product Analyst & Data Science Interview Preparation",
        "hero.title": "Master Product Analytics Interviews",
        "hero.description": "Real tasks from top tech companies",
        "hero.cta": "Start Training →",
        "stats.sql": "SQL Tasks",
        "stats.sql_desc": "Product Analytics",
        "stats.python": "Python Tasks",
        "stats.python_desc": "Analytics & ML",
        "stats.free": "Free",
        "stats.free_desc": "Open Source",
        "features.title": "Why This Platform?",
        "features.schema.title": "Real Product Schema",
        "features.schema.desc": "users, events, orders - like real companies",
        "features.data.title": "Sample Data",
        "features.data.desc": "See table structure right in the task",
        "features.progress.title": "Track Progress",
        "features.progress.desc": "Mark completed tasks",
        "features.instant.title": "Instant Run",
        "features.instant.desc": "Write code and see results immediately",
        "features.levels.title": "Junior to Middle",
        "features.levels.desc": "Tasks of different difficulty",
        "features.ready.title": "Interview Ready",
        "features.ready.desc": "Practice DAU, ARPU, Retention, Cohorts",
        "footer.text": "Built for Product Analysts & Data Scientists",
        "problems.title": "All Tasks",
        "problems.filter.all": "All",
        "problems.filter.sql": "SQL",
        "problems.filter.python": "Python",
        "problems.th.number": "#",
        "problems.th.title": "Title",
        "problems.th.category": "Category",
        "problems.th.difficulty": "Difficulty",
        "problems.th.status": "Status",
        "problems.th.action": "Action",
        "problems.status.completed": "✓ Completed",
        "problems.status.not_started": "Start",
        "problems.action.solve": "Solve →",
        "problem.back": "← Back to Tasks",
        "problem.description": "Task Description",
        "problem.tables": "Available Tables",
        "problem.hint": "Hint",
        "problem.examples": "Data Examples",
        "problem.editor": "Code Editor",
        "problem.run": "Run",
        "problem.check": "Check Solution",
        "problem.output": "Output",
        "problem.placeholder": "Write code and click Run...",
        "problem.empty_code": "⚠️ Write code before running!",
        "problem.executing": "⏳ Executing...",
        "problem.success": "✅ Query executed successfully!",
        "problem.no_results": "Query returned no results.",
        "problem.error": "❌ Error:",
        "problem.mark_complete": "✓ Mark as Completed",
        "problem.mark_incomplete": "⟲ Mark as Incomplete",
    },
    uk: {
        "header.title": "SQL & Python Interview Trainer",
        "header.subtitle": "Підготовка до інтерв'ю Product Analyst & Data Science",
        "hero.title": "Майструй Product Analytics Інтерв'ю",
        "hero.description": "Реальні завдання з топових техкомпаній",
        "hero.cta": "Почати тренування →",
        "stats.sql": "SQL Задачі",
        "stats.sql_desc": "Product Analytics",
        "stats.python": "Python Задачі",
        "stats.python_desc": "Аналітика & ML",
        "stats.free": "Безкоштовно",
        "stats.free_desc": "Open Source",
        "features.title": "Чому ця платформа?",
        "features.schema.title": "Реальна Продуктова Схема",
        "features.schema.desc": "users, events, orders - як у реальних компаніях",
        "features.data.title": "Приклади Даних",
        "features.data.desc": "Бачте структуру таблиць прямо в задачі",
        "features.progress.title": "Відстежуй Прогрес",
        "features.progress.desc": "Відмічай виконані завдання",
        "features.instant.title": "Миттєвий Запуск",
        "features.instant.desc": "Пиши код і одразу бач результат",
        "features.levels.title": "Від Junior до Middle",
        "features.levels.desc": "Задачі різної складності",
        "features.ready.title": "Готовність до Інтерв'ю",
        "features.ready.desc": "Практикуй DAU, ARPU, Retention, Cohorts",
        "footer.text": "Створено для Product Analysts & Data Scientists",
        "problems.title": "Усі Задачі",
        "problems.filter.all": "Всі",
        "problems.filter.sql": "SQL",
        "problems.filter.python": "Python",
        "problems.th.number": "№",
        "problems.th.title": "Назва",
        "problems.th.category": "Категорія",
        "problems.th.difficulty": "Складність",
        "problems.th.status": "Статус",
        "problems.th.action": "Дія",
        "problems.status.completed": "✓ Виконано",
        "problems.status.not_started": "Почати",
        "problems.action.solve": "Розв'язати →",
        "problem.back": "← Назад до задач",
        "problem.description": "Опис Задачі",
        "problem.tables": "Доступні Таблиці",
        "problem.hint": "Підказка",
        "problem.examples": "Приклади Даних",
        "problem.editor": "Редактор Коду",
        "problem.run": "Запустити",
        "problem.check": "Перевірити Рішення",
        "problem.output": "Результат",
        "problem.placeholder": "Напиши код і натисни Запустити...",
        "problem.empty_code": "⚠️ Напиши код перед запуском!",
        "problem.executing": "⏳ Виконується...",
        "problem.success": "✅ Запит виконано успішно!",
        "problem.no_results": "Запит не повернув результатів.",
        "problem.error": "❌ Помилка:",
        "problem.mark_complete": "✓ Відмітити як Виконано",
        "problem.mark_incomplete": "⟲ Відмітити як Невиконано",
    }
};

// Get current language from localStorage or default to 'en'
function getCurrentLang() {
    return localStorage.getItem('lang') || 'en';
}

// Set language and save to localStorage
function setLanguage(lang) {
    localStorage.setItem('lang', lang);
    updatePageLanguage(lang);
}

// Update all elements with data-i18n attribute
function updatePageLanguage(lang) {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
    
    // Update active language button
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
}

// Initialize language on page load
document.addEventListener('DOMContentLoaded', () => {
    const currentLang = getCurrentLang();
    updatePageLanguage(currentLang);
    
    // Add click handlers to language buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;
            setLanguage(lang);
            
            // Track language change in GTM
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'language_change',
                    'language': lang
                });
            }
        });
    });
});

// Export for use in other scripts
window.i18n = {
    getCurrentLang,
    setLanguage,
    t: (key) => {
        const lang = getCurrentLang();
        return translations[lang]?.[key] || key;
    }
};

// Patch: add new keys for v4.0 index page
(function() {
    const extra_en = {
        "hero.badge": "97 Real Interview Problems",
        "hero.title1": "Crush your next",
        "hero.title2": "Data Analyst interview.",
        "hero.sub": "Practice real-world SQL and Python problems in an immersive environment. Get instant feedback and sharpen your analytical thinking.",
        "hero.cta": "Start Practicing",
        "hero.patterns": "View Patterns",
        "stats.problems": "Interview Problems",
        "stats.levels": "Skill Levels",
        "stats.patterns": "Core Patterns",
        "stats.quizzes": "Theory Quizzes",
        "stats.free": "Free Forever",
        "features.label": "WHAT YOU GET",
        "features.title": "Built for real interviews",
        "features.sub": "Every problem mirrors what top tech companies actually ask.",
        "feat1.title": "Real Product Schema",
        "feat1.desc": "Practice on tables like real companies — users, events, orders with sample data shown right in the task.",
        "feat2.title": "Instant Code Execution",
        "feat2.desc": "Write SQL or Python directly in the browser. See results instantly without any setup required.",
        "feat3.title": "Pattern Library",
        "feat3.desc": "12 core patterns explained step-by-step: Window Functions, Cohorts, A/B Tests, ML Pipelines and more.",
        "feat4.title": "Track Your Progress",
        "feat4.desc": "Mark problems as solved. See your progress across all difficulty levels from Junior to Middle.",
        "feat5.title": "Theory Quizzes",
        "feat5.desc": "Test your knowledge with multiple-choice questions on key concepts: DAU, ARPU, A/B Testing and more.",
        "feat6.title": "AI Tutor Chat",
        "feat6.desc": "Stuck? Ask the built-in AI assistant for hints and explanations. Available on every problem page.",
        "cats.label": "PROBLEM CATEGORIES",
        "cats.title": "From Junior to Middle",
        "cats.sub": "Structured progression to match your current skill level.",
        "cat1.desc": "Aggregates, filters, basic JOINs",
        "cat2.desc": "Window functions, retention, LTV",
        "cat3.desc": "Pandas, data cleaning, groupby",
        "cat4.desc": "Scikit-learn, ML pipelines",
        "cat5.desc": "Complex algorithms, cohort matrix",
        "cta.title": "Ready to level up?",
        "cta.sub": "Join hundreds of analysts preparing for their next interview. Start with task #1 and work your way up.",
        "cta.btn": "Start Practicing Free",
        "footer.patterns": "Patterns",
        "footer.quizzes": "Quizzes",
        "table.title": "Title",
        "table.category": "Category",
        "table.difficulty": "Difficulty",
        "table.status": "Status",
    };
    const extra_uk = {
        "hero.badge": "97 реальних задач для інтерв'ю",
        "hero.title1": "Підкори своє наступне",
        "hero.title2": "Data Analyst інтерв'ю.",
        "hero.sub": "Практикуй реальні SQL та Python задачі. Миттєвий зворотний зв'язок для загострення аналітичного мислення.",
        "hero.cta": "Почати тренування",
        "hero.patterns": "Дивитись патерни",
        "stats.problems": "Задач для інтерв'ю",
        "stats.levels": "Рівнів складності",
        "stats.patterns": "Базових патернів",
        "stats.quizzes": "Теоретичних квізів",
        "stats.free": "Безкоштовно",
        "features.label": "ЩО ВИ ОТРИМАЄТЕ",
        "features.title": "Створено для реальних інтерв'ю",
        "features.sub": "Кожна задача відображає те, що насправді запитують топ-компанії.",
        "feat1.title": "Реальна продуктова схема",
        "feat1.desc": "Практикуйся на таблицях як у реальних компаніях — users, events, orders з прикладами даних.",
        "feat2.title": "Миттєве виконання коду",
        "feat2.desc": "Пиши SQL або Python прямо в браузері. Бачиш результати одразу без налаштувань.",
        "feat3.title": "Бібліотека патернів",
        "feat3.desc": "12 базових патернів покроково: Window Functions, Когорти, A/B тести, ML пайплайни.",
        "feat4.title": "Відстеження прогресу",
        "feat4.desc": "Позначай вирішені задачі. Дивись прогрес по всіх рівнях від Junior до Middle.",
        "feat5.title": "Теоретичні квізи",
        "feat5.desc": "Перевір знання через тести: DAU, ARPU, A/B тестування та інше.",
        "feat6.title": "AI-асистент",
        "feat6.desc": "Застрягли? Запитайте вбудованого AI-тьютора за підказками на кожній сторінці задачі.",
        "cats.label": "КАТЕГОРІЇ ЗАДАЧ",
        "cats.title": "Від Junior до Middle",
        "cats.sub": "Структурований прогрес відповідно до вашого рівня.",
        "cat1.desc": "Агрегати, фільтри, базові JOIN",
        "cat2.desc": "Вікон. функції, retention, LTV",
        "cat3.desc": "Pandas, очищення даних, groupby",
        "cat4.desc": "Scikit-learn, ML пайплайни",
        "cat5.desc": "Складні алгоритми, когортна матриця",
        "cta.title": "Готові до наступного рівня?",
        "cta.sub": "Починайте з задачі #1 та просувайтесь вперед.",
        "cta.btn": "Почати практику безкоштовно",
        "footer.patterns": "Патерни",
        "footer.quizzes": "Квізи",
        "table.title": "Назва",
        "table.category": "Категорія",
        "table.difficulty": "Складність",
        "table.status": "Статус",
    };
    if (typeof translations !== 'undefined') {
        Object.assign(translations.en, extra_en);
        Object.assign(translations.uk, extra_uk);
    }
})();
