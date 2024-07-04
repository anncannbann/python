

todolist =[]

while True:
    user = input('Type add or show:')

    match user:
        case 'add':
            todo = input('Enter a task:')
            todolist.append(todo.capitalize())

        case 'show':
            print(todolist)



