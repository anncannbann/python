

todolist =[]

while True:
    user = input('Type add or show or exit:').strip()

    match user:
        case 'add':
            todo = input('Enter a task:')
            todolist.append(todo.capitalize())

        case 'show':
            for item in todolist:
                print(todolist)
        
        case 'exit':
            break



print("bub bye")