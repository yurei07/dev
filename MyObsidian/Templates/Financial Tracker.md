---
noteType: finance
tags:
  - finance
  - money
month: <% tp.date.now("YYYY-MM") %>
income: 0
expenses: 0
savings: 0
banner: https://github.com/NazariiPalahnii/Wallpapers/blob/main/a_close_up_of_a_bird's_back.jpeg?raw=true
created_at: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ssZ") %>
---
<br>

> [!multi-column]
>
>> [!blank-container]
>> **Total Income**  
>> `INPUT[number:income]`
>
>> [!blank-container]
>> **Total Expenses**  
>> `INPUT[number:expenses]`
>
>> [!blank-container]
>> **Savings**  
>> `INPUT[number:savings]`

<br>

---

## 📈 Transactions

Here you can log all your income and expenses.
**Tip:** To automatically calculate and create reports in the future, I recommend looking into the `Dataview` plugin.

**Example Entry:**
- **Income:** `[[<% tp.date.now("YYYY-MM-DD") %>]] - Salary - 50000`
- **Expense:** `[[<% tp.date.now("YYYY-MM-DD") %>]] - Groceries - 3000`

### Income
- 

### Expenses
- 

---

## 💡 Investment Ideas

This section is for brainstorming and analyzing potential investment ideas. It will help you grow financially.

### Stocks
- **Name/Ticker:** 
  - **Risk:** (Low/Medium/High)
  - **Potential:** 
  - **Notes:** 

### Crypto
- **Name/Ticker:** 
  - **Risk:** (Low/Medium/High)
  - **Potential:** 
  - **Notes:** 

### Other (Real Estate, ETFs, etc.)
- **Name/Type:** 
  - **Risk:** (Low/Medium/High)
  - **Potential:** 
  - **Notes:** 

---

## 🎯 Financial Goals

Write down your short-term and long-term financial goals.

### Short-Term (up to 1 year)
- [ ] 
- [ ] 

### Long-Term (1+ year)
- [ ] 
- [ ] 

<% await tp.file.move("/1.Life/Finance/" + tp.file.title) %>
