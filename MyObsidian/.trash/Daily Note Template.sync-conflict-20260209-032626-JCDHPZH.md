<% "---" %>
<%* let aliases = await tp.system.prompt('Enter the sentence of the day:') 
tR += "aliases: " + aliases %>
id: journal-<% tp.file.title %>
tags: journal/dailynote
Mood: 
Why: 
Meditation: false
Exercise: false
Study: 
Ultradian_Cycles: 
banner: https://github.com/NazariiPalahnii/Wallpapers/blob/main/i3-arch-mazda-ricing-and-a-buttload-of-4k-wallpapers-v0-vywtlpn835qf1.webp?raw=true
banner_icon: 📅
banner_y: 0.68
created_at: <% tp.file.creation_date() %>
modified_at: <% tp.file.last_modified_date() %>
date: <% tp.file.title %>
<% "---" %>

↑ `$=dv.pages().where(b => b.id == 'journal-<% tp.date.now("gggg-[W]ww",0, tp.file.title, "YYYY-MM-DD") %>')[0].file.link`
<-<-  [[<% tp.date.now("YYYY-MM-DD",-1, tp.file.title, "YYYY-MM-DD") %>]]  <-  <% tp.file.title %>  ->  [[<% tp.date.now("YYYY-MM-DD",+1, tp.file.title, "YYYY-MM-DD") %>]]   ->->

<% tp.web.daily_quote() %>

---
# `=this.aliases`

> [!todo]- Study & Habits
> ```meta-bind
>INPUT[progressBar(title('Study Rating'), minValue(0), maxValue(10)):Study]
>```
> ```meta-bind
>INPUT[progressBar(title('Ultradian Cycles'), stepSize(0.2), minValue(0), maxValue(5)):Ultradian_Cycles]
>```
> **Words learning:** `INPUT[toggle:Meditation]` | **Work out:** `INPUT[toggle:Exercise]` 

> [!info]- Mood
> ```meta-bind
> INPUT[progressBar(minValue(0), maxValue(10)):Mood]
> ```
> **Why:** `INPUT[text:Why]`

---
## 🔥 Priority Tasks (From Weekly Plan)
*Задачи, запланированные на этот день в других заметках:*
<% "```tasks" %>
not done
due <% tp.file.title %>
<% "```" %>

## Day Planner & Routine
- [ ] 06:00 - 07:00 🌅 Wake up, water, breakfast, plan the day 🔼
- [ ] 07:40 - 13:00 🏫 School ⏫
- [ ] Break 1 hour 🔼
- [ ] Homework (90 mins) 🔼
- [ ] Gym (Mon/Tue/Thu/Fri) ⏫
- [ ] IT / Code 🔼
- [ ] 21:30 - 22:00 📔 Diary & Reflection 🔼

## Things I am grateful for:
- 

## Glimpse of the day

**Dear Diary**,

_Palahnii Nazari_