<%*
// Название твоего дневного шаблона (убедись, что оно точное)
const dailyTemplateName = 'Daily Note Template'; 
// Путь к папке, где будут храниться дневные заметки
const dailyNotesFolderPath = '2.Journaling/Daily Journaling/2025'; // <-- ОБЯЗАТЕЛЬНО ИЗМЕНИ ЭТОТ ПУТЬ!

// Запрос даты начала недели (сегодняшний день, или можно изменить на начало недели)
// Здесь мы делаем его гибким: начнем с дня, в который ты запускаешь скрипт.
// Если ты запускаешь его в воскресенье, то он создаст заметки с Вс по Сб.
// Если в Пн, то с Пн по Вс.
let startDate = new Date(); // Сегодняшняя дата
// Если ты хочешь, чтобы всегда начиналось с понедельника, раскомментируй и измени:
// let today = new Date();
// let dayOfWeek = today.getDay(); // 0 = Sunday, 1 = Monday
// let diff = today.getDate() - dayOfWeek + (dayOfWeek === 0 ? -6 : 1); // Установить на понедельник текущей недели
// startDate = new Date(today.setDate(diff));

// Массив для хранения путей к созданным файлам
const createdFiles = [];

// Создаем заметки на 7 дней
for (let i = 0; i < 7; i++) {
    let currentDate = new Date(startDate);
    currentDate.setDate(startDate.getDate() + i);

    let year = currentDate.getFullYear();
    let month = String(currentDate.getMonth() + 1).padStart(2, '0');
    let day = String(currentDate.getDate()).padStart(2, '0');
    let fileName = `${year}-${month}-${day}`;
    let filePath = `${dailyNotesFolderPath}/${fileName}.md`;

    // Проверяем, существует ли файл
    let fileExists = app.vault.getAbstractFileByPath(filePath);

    if (fileExists) {
        console.log(`Файл уже существует: ${filePath}. Пропускаем.`);
        createdFiles.push(`[[${filePath}|${fileName}]] (уже был)`);
    } else {
        // Создаем файл из шаблона
        let templateContent = await tp.file.content(dailyTemplateName);
        let processedContent = await tp.templater.tokenizeAndEvaluate(templateContent);

        let newFile = await app.vault.create(filePath, processedContent);
        console.log(`Создан файл: ${filePath}`);
        createdFiles.push(`[[${filePath}|${fileName}]]`);
    }
}

// Выводим ссылки на созданные/существующие файлы
tR += `# Заметки на неделю, созданные ${tp.date.now("YYYY-MM-DD HH:mm")}\n\n`;
tR += `## Дни недели:\n`;
for (const fileLink of createdFiles) {
    tR += `- ${fileLink}\n`;
}

// Опционально: создаем или переходим к недельной заметке
// Эта часть потребует наличия твоего недельного шаблона (который я тебе дал ранее)
// и его правильного названия файла (например, YYYY-Www)
let currentWeekDateString = tp.date.now("gggg-[W]ww"); // например, 2024-W10
let weeklyNoteName = `${currentWeekWeekDateString}.md`; // или как ты называешь свой еженедельный файл
let weeklyNotePath = `${dailyNotesFolderPath}/WeeklyNotes/${weeklyNoteName}`; // <-- ИЗМЕНИ ПУТЬ К ТВОИМ НЕДЕЛЬНЫМ ЗАМЕТКАМ!
// Проверяем, существует ли недельная заметка
let weeklyNoteExists = app.vault.getAbstractFileByPath(weeklyNotePath);

if (!weeklyNoteExists) {
    tR += `\n## Недельная заметка не найдена/создана.\n`;
    tR += `[Создать недельную заметку для ${currentWeekDateString}](${weeklyNotePath}|Нажми для создания)`
    // Можно также автоматически создать недельную заметку, но пока пусть будет ссылка.
    // Если хочешь, чтобы она создавалась автоматически, можно добавить:
    // let weeklyTemplateContent = await tp.file.content('Weekly Template'); // Название твоего недельного шаблона
    // let processedWeeklyContent = await tp.templater.tokenizeAndEvaluate(weeklyTemplateContent);
    // await app.vault.create(weeklyNotePath, processedWeeklyContent);
    // tR += `\n**Недельная заметка для ${currentWeekDateString} создана: ** [[${weeklyNotePath}|Открыть]]`;
} else {
    tR += `\n**Недельная заметка для ${currentWeekDateString} существует:** [[${weeklyNotePath}|Открыть]]`;
}

%>