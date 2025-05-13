import time

print('\n' + ' TO-DO LIST '.center(50, '*'))
print('-'*50 +'\n')

while True:
    try:
        with open('todo_list_textfile.txt','r') as todo_list_file:
            tasks_list = [line.strip() for line in todo_list_file.readlines()]
    except FileNotFoundError:
        open('todo_list_textfile.txt','a')
        continue
    tasks_list = [task for task in tasks_list if task]
    time.sleep(1.5)
    user_input = input('''
Choose from the following operations:

add    : Add a task to the list
remove : Remove a task from the list
view   : View all tasks
exit   : Exit the application
                        
=> ''').strip().lower()
    print('\n'+'-'*50)
    time.sleep(1)

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
            print("You haven't added any task yet.\nPlease add a task first.")
        for index,task in enumerate(tasks_list):
            print(f'{index+1}.) {task}')
    
    elif user_input == 'add':
        add_task = input('\nEnter a task to add\n=> ').strip()
        if add_task:
            tasks_list.append(add_task)
            time.sleep(1)
            print('\nadding task...')
            time.sleep(1)
            print('\nTask added successfully.\n')
        else:
            print('\nEmpty task not added.')
    
    elif user_input == 'remove':
        try:
            remove_task_input = int(input('\nEnter the serial number of the task to remove (one at a time)\n=> ').strip())
            removed = tasks_list.pop(remove_task_input - 1)
            time.sleep(1)
            print('removing task...')
            time.sleep(1)
            print(f"\nTask '{removed}' removed successfully.")
        except ValueError:
            print('\nInvalid input! Please enter a valid input.')
        except IndexError:
            print(f"\nThere is no such task with serial number {remove_task_input}.")

    with open('todo_list_textfile.txt','w') as todo_list_file:
        for task in tasks_list:
            todo_list_file.write(task + '\n')

    print('\n' + '-'*50 + '\n')