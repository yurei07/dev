tasks = ["to do homework", "buy food", "to clean my room"]
while True:
    print('\n=== Menu TODO list ===')
    print('1. List of tasks')
    print('2. Add task')
    print('3. Delete task')
    print('4. Exit')

    choice = input('Choice an action: ')
    point = 1

    if choice == '4':
        break

    elif choice == '1':
        print('\n=== Your tasks ===')
        for i in tasks:
            print(f'{point}. {i}')
            point +=1
    elif choice == '2':
        task = input('\nWhat do you want to add in your list?: ')
        tasks.append(task)
        print(f"Added: {task}")
        print(f"Updated list:")
        for i in tasks:
            print(f'{point}. {i}')
            point += 1
    elif choice == '3':
        print('\n=== Delete tasks ===')
        for task in tasks:
            print(f'{point}. {task}')
            point += 1
        task_delete = input('Enter the number of the task to delete: ')
        if task_delete.isdigit():
            i = int(task_delete) -1
            if 0 <= i < len(tasks):
                deleted_task = tasks.pop(i)
                print(f'\nDeleted task: {deleted_task}')
                for task in tasks:
                    print(f'{point}. {task}')
                    point += 1
            else:
                print('Invalid task number.')
        else:
            print('Please enter a valid number.')

