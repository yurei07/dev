<% "---" %>
tags: journal/weeklynote
id: journal-<% tp.file.title %>
week: <% tp.file.title %>
aliases: []
Mood: 
Why: 
banner: https://github.com/NazariiPalahnii/Wallpapers/blob/main/b-139.jpg?raw=true
banner_y: 0.8
banner_icon: 📅
created_at: <% tp.file.creation_date('YYYY-MM-DD[T]HH:mm:ssZ') %>
modified_at: <% tp.file.last_modified_date('YYYY-MM-DD[T]HH:mm:ssZ') %>
<% "---" %>

↑ `$=dv.pages().where(b => b.id == 'journal-<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>')[0].file.link`
<-<- [[<% moment(tp.file.title, "gggg-[W]ww").subtract(1, 'weeks').format("gggg-[W]ww") %>]] <- <% tp.file.title %> -> [[<% moment(tp.file.title, "gggg-[W]ww").add(1, 'weeks').format("gggg-[W]ww") %>]] ->->
M [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("DD") %>]] • T [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("DD") %>]] • W [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("DD") %>]] • T [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("DD") %>]] • F [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("DD") %>]] • S [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("DD") %>]] • S [[<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("YYYY-MM-DD") %>|<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("DD") %>]]

<% tp.web.daily_quote() %>

---

> [!info]+ Mood
> ```meta-bind
> INPUT[progressBar(minValue(0), maxValue(10)):Mood]
> ```
>  **Why:** `INPUT[text:why]`

>[!tip]+ Health
> ```meta-bind
> INPUT[progressBar(minValue(0), maxValue(10)):Health]
> ```

---
## 🗓 Weekly Planner
*Пиши задачу после значка календаря. Дата уже стоит правильная!*

### Monday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(1).format("YYYY-MM-DD") %>

### Tuesday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(2).format("YYYY-MM-DD") %>

### Wednesday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(3).format("YYYY-MM-DD") %>

### Thursday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(4).format("YYYY-MM-DD") %>

### Friday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(5).format("YYYY-MM-DD") %>

### Saturday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(6).format("YYYY-MM-DD") %>

### Sunday (<% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("YYYY-MM-DD") %>)
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("YYYY-MM-DD") %>
- [ ]  📅 <% moment(tp.file.title, "gggg-[W]ww").isoWeekday(7).format("YYYY-MM-DD") %>

---

## What is worth remembering about this week?
- 

## What am I grateful for this week?
- 

## What is your Goal for this week?
- [ ]  

## What did I accomplish this week?
- 

## What could I have done better?
- 

## What I want to achieve next week?
-