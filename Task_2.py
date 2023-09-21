HELP = """
Список основных команд:
'add' - добавить задачу в список (навание 
задачи запрашиваем у пользователя).
'show' - вывод всех добавленных задач на экран.
'help' - вывод справки по программе.
"""

task_list = []
# ==============================
today = []
tomorrow = []
other = []

run = True
while run:
    command = input('Введите команду: ')
    if command == "add":
        task = input("Введите название задачи: ")
        if task == "today":
            today.append(task)
        elif task == "tomorrow":
            tomorrow.append(task)
        else:
            task_list.append(other)
        print(f"Задача {task} добавлена")
    elif command == "show":
        print("today", today)
        print("tomorrow", tomorrow)
        print("other", other)
    elif command == "help":
        print(HELP)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
