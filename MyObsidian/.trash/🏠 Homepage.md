---
created_at: 2024-01-30T11:38:56+05:30
modified_at: 2025-10-03T10:44:06+02:00
tags:
  - homepage
  - followup
banner: https://i.imgur.com/9ZJBvN8.jpg
banner_y: 0.446
cssclasses:
modified: 2025-07-10T17:26:42+02:00
---
### Life 
- [[Personal Financing]]
- [[My goals to 15.07.2026]]
- [[Sleep & Routine]]
### Journal
- [[2025-07-10]]
- [[2.Journaling/Monthly breafing/March - April|March - April]]
- [[2.Journaling/Weekly Breifing/March - April|March - April]]
### Teaching 
- [[12 week of EN & GE]]
- [[12 week python]]


## Goals

 ```dataviewjs
 let goals = dv.pages('"1. Life/Home/Progress Goals"');
 dv.table(["Goal", "Deadline", "Progress"],
 goals.map(goal => [
 `<span style="font-size: 1.2em;">${goal.file.link}</span>`,
 goal.deadline,
 `<progress value="${goal.progress}" max="${goal.target}"></progress><br>${Math.round((goal.progress / goal.target) * 100)}% completed`
 ])
 );
```

## Daily Habit Tracker
```dataviewjs
const pages = dv.pages('#journal/dailynote')
.where((p) => "Meditation" in p || "Exercise" in p)
.sort((p) => p.file.day, "desc")
.map((p) =>
Object.create({
link: p.file.link,
day: p.file.day,
Meditation: p.Meditation,
Exercise: p.Exercise,
})
);
function getStreak(validate) {
let count = 0;
for (const note of pages) {
if (validate(note)) count++;
else break;
}
return count;
}
function getRecord(validate) {
let record = 0;
let count = 0;
for (const note of pages) {
if (validate(note)) {
count++;
record = Math.max(record, count);
} else {
count = 0;
}
}
return record;
}
const done = "✅";
const skip = "❌";
const fileRows = pages
.filter((p) => p.day >= moment().subtract(1, "w"))
.sort((p) => p.day)
.map((note) => [
note.link,
note.Meditation ? done : skip,
note.Exercise ? done : skip,
]);
const meditation = [
getStreak((note) => note.Meditation),
getRecord((note) => note.Meditation),
];
const workout = [
getStreak((note) => note.Exercise),
getRecord((note) => note.Exercise),
];
dv.table(
["Habits", "🧘", "💪🏼"],
[
...fileRows,
["‎"],
["**Streak**", meditation[0], workout[0]],
["**Record**", meditation[1], workout[1]],
]
);
```

