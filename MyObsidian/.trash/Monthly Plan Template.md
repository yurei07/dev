---
banner: "Attachments/Pasted image 20260122173509.png" # Placeholder, can be changed
tags:
  - monthly-plan
  - <% tp.date.now("YYYY-MM") %>
month: <% tp.date.now("YYYY-MM") %>
---
# Monthly Plan for <% tp.date.now("MMMM YYYY") %>

> [!summary] Main Focus for this Month
> *Your main focus here...*

## ✅ Key Goals
- [ ] 
- [ ] 
- [ ] 

## 💡 Secondary Objectives
- [ ] 
- [ ] 

## 🧠 Learning/Skills Focus
- [ ] 

## Habits to Build
- [ ] 
- [ ] 

<% await tp.file.move("/1.Life/Monthly Plans/" + tp.file.title) %>