import sys

filename = "todo_task.txt"
todo_task = []


with open(filename, 'r') as f:
    for line in f:
        todo_task.append(line.strip())


def print_application_usage():

    print("""
        Command line arguments:
            -l   Lists all the cli_task
            -a   Adds a new task
            -r   Removes an task
            -c   Completes an task
    """)


def add_task(item):
    """
    When we type a command -a then this method called
    which add the new task in the todo_task.txt file
    """
    todo_task.append(item)

    with open(filename, 'w') as file:
        for items in todo_task:
            file.write(f'{items}\n')


def remove_task():
    pass


def check_todo_list():
    pass


def todo_list_content():
    """
    This method is used to return the list
    of tasks that are available in the todo_task.txt file
    """
    if not todo_task:
        print('No todos task in the list')
    else:
        for i, items in enumerate(todo_task):
            print(f'{i + 1} - {items}')


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print_application_usage()
    elif len(sys.argv) == 3 and sys.argv[1] == '-a':
        add_task(sys.argv[2])
        print(f"Task Added successfully : {sys.argv[2]}")
    elif len(sys.argv) == 2 and sys.argv[1] == '-l':
        todo_list_content()
    elif sys.argv[1] == '-c' and len(sys.argv) == 3:
        check_todo_list()
    elif sys.argv[1] == '-r' and len(sys.argv) == 3:
        remove_task()
    else:
        print('Please verify your arguments feels incorrect')
        print('Usage: todo [-l | -a <description> | -r <index>]')


main()
