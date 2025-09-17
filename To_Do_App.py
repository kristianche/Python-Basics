import time

print('### Welcome to the To Do List Console App                         ###')

time.sleep(1.5)

print('### Here you can modify the task which you need to do for the day ###')
time.sleep(2)

print('### Here are the possible operations:                             ###')
time.sleep(2)

print('### Add -> add a task                                             ###')
print('### View -> view all the tasks                                    ###')
print('### Edit -> edit a task (point out the position of the task)      ###')
print('### Delete -> delete a task (point out the position of the task)  ###')
print('### Stop -> stop the program                                      ###')


def add(task, tasks):
    tasks.append(task)
    print(f'Added {task} successfully to the list!')


def view(tasks):
    print(', '.join(tasks))


def edit(index, edited_task, tasks):
    tasks[index] = edited_task
    print('Edit was successful!')


def delete(index, tasks):
    task_for_delete = tasks[index]
    tasks.remove(task_for_delete)
    print(f'Task {task_for_delete} was deleted!')


def main():
    tasks = []
    command = input('Type your command: ')

    while True:

        if command == 'Stop':
            break

        if command == 'Add':
            task = input('Insert your task: ')
            add(task, tasks)

        elif command == 'View':
            view(tasks)

        elif command == 'Edit':
            position = int(input('Choose the position of the task which you want to edit: '))

            if position - 1 >= len(tasks):
                print('No task at this position')

            else:
                index = position - 1
                new_task = input('Insert the edited task: ')
                edit(index, new_task, tasks)

        elif command == 'Delete':
            position = int(input('Choose the position of the task which you want to delete: '))

            if position - 1 >= len(tasks):
                print('No task at this position')
            else:
                index = position - 1
                delete(index, tasks)
        else:
            print('Invalid Input( Add, View, Edit, Delete, Stop )')

        command = input('Type your command: ')

    print('Thanks for using my simple app')


main()