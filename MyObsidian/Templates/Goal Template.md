---
noteType: goal
area: ""
tags: goal
progress: 0
target: 100
startDate: ""
deadline: ""
completionDate: ""
completed: false
banner: https://github.com/NazariiPalahnii/Wallpapers/blob/main/a_close_up_of_a_bird's_back.jpeg?raw=true
created_at: <% tp.file.creation_date("YYYY-MM-DDTHH:mm:ssZ") %>
---
<br>

> [!multi-column]
>
>> [!blank-container]
>> **Start Date**  
>> `INPUT[date:startDate]`
>
>> [!blank-container]
>> **Deadline**  
>> `INPUT[date:deadline]`
>
>> [!blank-container]
>> **Completion Date**  
>> `INPUT[date:completionDate]`

<br>

> [!multi-column]
>
>> [!blank-container]
>> **Completed**  
>> `INPUT[toggle:completed]` 
>
>> [!blank-container]
>> **Area**  
>> `INPUT[text:area]`

```meta-bind
INPUT[progressBar(title('Progress'), minValue(0), maxValue(100)):progress]
```
> [!info] Why is this goal important to me?
> 1. 

> [!success]- What would I gain by achieving this goal?
> 1. 

> [!failure]- What are the possible risks and obstacles?
> 1. 

## Sub Goals:


## Related:


<% await tp.file.move("/1.Life/" + tp.file.title) %>
