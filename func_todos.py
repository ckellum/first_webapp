def get_todos():
    with open('todos.txt', 'r') as todos_file:
        todos_local = todos_file.readlines()
    return todos_local


def write_todos(todos_arg):
    with open('todos.txt', 'w') as todos_file:
        todos_local = todos_file.writelines(todos_arg)
    return todos_local

