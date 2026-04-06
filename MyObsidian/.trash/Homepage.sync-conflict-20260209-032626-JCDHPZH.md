---
banner: https://github.com/NazariiPalahnii/Wallpapers/blob/main/b-453.jpg?raw=true  
pythonProgress: 0
booksProgress: 0
---

```search-bar
show recent files
```

***

> [!dashboard] Dashboard
> > [!stats]
> > > [!stat] Tasks Completed
> > >
> > > ```dataviewjs
> > > const allTasks = dv.pages().file.tasks;
> > > const completedTasks = allTasks.filter(t => t.completed);
> > > dv.paragraph(`**${completedTasks.length}**`);
> > > ```
> >
> > > [!stat] Total Notes
> > >
> > > ```dataviewjs
> > > dv.paragraph(`**${dv.pages("").where(p => p.file.ext === "md").length}**`);
> > > ```
> >
> > > [!stat] Today's Progress
> > >
> > > ```dataviewjs
> > > // Function to extract date from task text
> > > function extractDate(taskText) {
> > >   const match = taskText.match(/📅\s*(\d{4}-\d{2}-\d{2})/);
> > >   return match ? dv.date(match[1]) : null;
> > > }
> > > 
> > > // Find all tasks for today
> > > const today = dv.date('today');
> > > let allTodayTasks = [];
> > > 
> > > // Daily note for today
> > > const dailyNotes = dv.pages('"2.Journaling/Daily Journaling"')
> > >   .where(p => p.file.day && p.file.day.toISODate() === today.toISODate());
> > > 
> > > if (dailyNotes.length > 0) {
> > >   const dailyTasks = dailyNotes[0].file.tasks;
> > >   allTodayTasks.push(...dailyTasks);
> > > }
> > > 
> > > // Weekly note for the current week
> > > const monday = dv.date('monday');
> > > const sunday = dv.date('sunday');
> > > const weeklyNotes = dv.pages('"2.Journaling/Weekly Breifing"')
> > >   .where(p => p.file.day && p.file.day >= monday && p.file.day <= sunday);
> > > 
> > > if (weeklyNotes.length > 0) {
> > >   const weeklyTasks = weeklyNotes[0].file.tasks;
> > >   const todayWeeklyTasks = weeklyTasks.filter(t => {
> > >     const taskDate = extractDate(t.text);
> > >     return taskDate && taskDate.toISODate() === today.toISODate();
> > >   });
> > >   allTodayTasks.push(...todayWeeklyTasks);
> > > }
> > > 
> > > // Calculate progress
> > > const totalTasks = allTodayTasks.length;
> > > const completedTasks = allTodayTasks.filter(t => t.completed).length;
> > > 
> > > if (totalTasks === 0) {
> > >   dv.paragraph(`**0/0**<br><small>No tasks today</small>`);
> > > } else {
> > >   const percentage = Math.round((completedTasks / totalTasks) * 100);
> > >   
> > >   // Determine emoji based on progress
> > >   let emoji;
> > >   if (percentage === 0) emoji = "😴";
> > >   else if (percentage < 30) emoji = "🐌";
> > >   else if (percentage < 50) emoji = "🚶";
> > >   else if (percentage < 80) emoji = "🏃";
> > >   else if (percentage < 100) emoji = "⚡";
> > >   else emoji = "🎯";
> > >   
> > >   dv.paragraph(`**${completedTasks}/${totalTasks}** ${emoji}<br><small>${percentage}% completed</small>`);
> > > }
> > > ```
>
> > [!main]
> > >[!left-column,]
> > > >[!box] Quick Links
> > > > [Github](https://github.com/NazariiPalahnii)
> > > >
> > > > [MyBook](http://www.stolyarov.info/books/pdf/progintro_e2v1.pdf)
> > > >
> > > > [DeepSeek](https://chat.deepseek.com/)
> > > >
> > > > [MyServer](http://192.168.178.95/prizrak/)
> > >
> > > > [!box] Goals & Plans
> > > > ```dataviewjs
> > > > // Long-term Goals - searching in '1.Life' folder
> > > > const goals = dv.pages('"1.Life"').where(p => p.noteType === "goal" && !p.completed);
> > > > if (goals.length > 0) {
> > > >   dv.header(3, "🎯 Long-term Goals");
> > > >   dv.list(goals.file.link);
> > > > } else {
> > > >   dv.paragraph("No active long-term goals found.");
> > > > }
> > > > 
> > > > // Current Month Goals
> > > > const currentMonth = dv.date('today').startOf('month');
> > > > const nextMonth = dv.date('today').plus({ months: 1 }).startOf('month');
> > > > const monthlyGoals = dv.pages('"1.Life"')
> > > >   .where(p => p.noteType === "goal" && !p.completed && p.deadline && dv.date(p.deadline) >= currentMonth && dv.date(p.deadline) < nextMonth);
> > > > 
> > > > if (monthlyGoals.length > 0) {
> > > >   dv.header(3, "📅 This Month's Goals");
> > > >   dv.list(monthlyGoals.map(p => p.file.link + " (due: " + p.deadline + ")"));
> > > > }
> > > >
> > > > // Upcoming Deadlines (next 14 days)
> > > > const upcomingTasks = dv.pages().file.tasks
> > > >   .where(t => !t.completed && t.due && t.due <= dv.date('today+14'))
> > > >   .sort(t => t.due)
> > > >   .limit(5);
> > > >   
> > > > if (upcomingTasks.length > 0) {
> > > >   dv.header(3, "⏰ Upcoming Deadlines");
> > > >   dv.taskList(upcomingTasks, false);
> > > > }
> > > > ```
> >
> > > [!right-column]
> > > > [!box] Todo [[TODO|→]]
> > > >
> > > > ~~~tabs
> > > > tab: 🔥 Today
> > > > ```dataviewjs
> > > > // Function to extract date from task text
> > > > function extractDate(taskText) {
> > > >   const match = taskText.match(/📅\s*(\d{4}-\d{2}-\d{2})/);
> > > >   return match ? dv.date(match[1]) : null;
> > > > }
> > > > 
> > > > // Find current daily note in '2.Journaling/Daily Journaling' folder
> > > > const today = dv.date('today');
> > > > const dailyNotes = dv.pages('"2.Journaling/Daily Journaling"')
> > > >   .where(p => p.file.day && p.file.day.toISODate() === today.toISODate());
> > > > 
> > > > // Find current weekly note (the one whose file day falls within the current week)
> > > > const monday = dv.date('monday');
> > > > const sunday = dv.date('sunday');
> > > > const weeklyNotes = dv.pages('"2.Journaling/Weekly Breifing"')
> > > >   .where(p => p.file.day && p.file.day >= monday && p.file.day <= sunday);
> > > > 
> > > > let tasks = [];
> > > > 
> > > > // Tasks from daily note
> > > > if (dailyNotes.length > 0) {
> > > >   const dailyTasks = dailyNotes[0].file.tasks;
> > > >   tasks.push(...dailyTasks.filter(t => !t.completed));
> > > > }
> > > > 
> > > > // Tasks from weekly note with today's date
> > > > if (weeklyNotes.length > 0) {
> > > >   const weeklyTasks = weeklyNotes[0].file.tasks;
> > > >   const todayWeeklyTasks = weeklyTasks.filter(t => {
> > > >     if (t.completed) return false;
> > > >     const taskDate = extractDate(t.text);
> > > >     return taskDate && taskDate.toISODate() === today.toISODate();
> > > >   });
> > > >   tasks.push(...todayWeeklyTasks);
> > > > }
> > > > 
> > > > if (tasks.length > 0) {
> > > >   dv.taskList(tasks, false);
> > > > } else {
> > > >   dv.paragraph("No tasks for today");
> > > > }
> > > > ```
> > > > 
> > > > tab: 📅 This Week
> > > > ```dataviewjs
> > > > // Find current weekly note
> > > > const monday = dv.date('monday');
> > > > const sunday = dv.date('sunday');
> > > > const weeklyNotes = dv.pages('"2.Journaling/Weekly Breifing"')
> > > >   .where(p => p.file.day && p.file.day >= monday && p.file.day <= sunday);
> > > > 
> > > > if (weeklyNotes.length > 0) {
> > > >   const weeklyTasks = weeklyNotes[0].file.tasks;
> > > >   const notCompleted = weeklyTasks.filter(t => !t.completed);
> > > >   if (notCompleted.length > 0) {
> > > >     dv.taskList(notCompleted, false);
> > > >   } else {
> > > >     dv.paragraph("No tasks for this week");
> > > >   }
> > > > } else {
> > > >   dv.paragraph("No weekly note found for this week");
> > > > }
> > > > ```
> > > > 
> > > > tab: ⏳ Overdue
> > > > ```dataviewjs
> > > > const today = dv.date('today');
> > > > 
> > > > // Function to extract date from task text
> > > > function extractDate(taskText) {
> > > >   const match = taskText.match(/📅\s*(\d{4}-\d{2}-\d{2})/);
> > > >   return match ? dv.date(match[1]) : null;
> > > > }
> > > > 
> > > > // Search in all weekly and daily notes
> > > > const dailyPages = dv.pages('"2.Journaling/Daily Journaling"');
> > > > const weeklyPages = dv.pages('"2.Journaling/Weekly Breifing"');
> > > > let overdueTasks = [];
> > > > 
> > > > // Check daily notes
> > > > for (let page of dailyPages) {
> > > >   const tasks = page.file.tasks;
> > > >   for (let task of tasks) {
> > > >     if (task.completed) continue;
> > > >     const taskDate = extractDate(task.text);
> > > >     if (taskDate && taskDate < today) {
> > > >       overdueTasks.push(task);
> > > >     }
> > > >   }
> > > > }
> > > > 
> > > > // Check weekly notes
> > > > for (let page of weeklyPages) {
> > > >   const tasks = page.file.tasks;
> > > >   for (let task of tasks) {
> > > >     if (task.completed) continue;
> > > >     const taskDate = extractDate(task.text);
> > > >     if (taskDate && taskDate < today) {
> > > >       overdueTasks.push(task);
> > > >     }
> > > >   }
> > > > }
> > > > 
> > > > if (overdueTasks.length > 0) {
> > > >   dv.taskList(overdueTasks, false);
> > > > } else {
> > > >   dv.paragraph("No overdue tasks");
> > > > }
> > > > ```
> > > > ~~~
> > >
> > >
> >
>

***

<iframe src="https://jandee.vercel.app/NazariiPalahnii" width="80%" height="275px" style="display: block; margin: 0 auto;"></iframe>
