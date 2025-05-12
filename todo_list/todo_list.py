print('\n' + ' TO-DO LIST '.center(50, '*'))
print('-'*50 +'\n')

while True:
    try:
        with open('todo_list_textfile.txt','r') as todo_list_file:
            tasks_list = [line.strip() for line in todo_list_file.readlines()]
    except:
        open('todo_list_textfile.txt','a')
        continue
    tasks_list = [task for task in tasks_list if task]
    user_input = input('''
Choose from the following operation:-

add    : Add a task to the list
remove : Remove a task from the list
view   : View all tasks
exit   : Exit the application
                        
=> ''').strip().lower()
    print('\n'+'-'*50)
    
    if user_input not in ['add','remove','view','exit']:
        print('Invalid input! Please enter a valid input.')
        continue

    if user_input == "exit":
        print("\nThanks for using To-Do List! 👋\n")
        break
    
    elif user_input == "view":
        print('\n' + 'Task'.center(50))
        print(('*'*4).center(50) + '\n')
        if len(tasks_list) == 0:
            print("You haven't added any task yet.\nPlease add a task First.")
        for index,task in enumerate(tasks_list):
            print(f'{index+1}.) {task}')
    
    elif user_input == 'add':
        add_task = input('\nEnter tasks to add\n=> ').strip()
        tasks_list.append(add_task)
    
    elif user_input == 'remove':
        try:
            remove_task_input = int(input('\nEnter the serial number of the task to remove (one at a time)\n=> ').strip())
            tasks_list.pop(remove_task_input - 1)
        except ValueError:
            print('\nInvalid input! Please enter a valid input.')
        except IndexError:
            print(f"\nThere is no such task with serial number {remove_task_input}.")

    with open('todo_list_textfile.txt','w') as todo_list_file:
        for task in tasks_list:
            todo_list_file.write(task + '\n')
            todo_list_file.flush()

    print('\n' + '-'*50 + '\n')