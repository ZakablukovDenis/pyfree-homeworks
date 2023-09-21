import random

HELP = """
Список основных команд:
'add' - добавить задачу в список (навание 
задачи запрашиваем у пользователя).
'show' - вывод всех добавленных задач на экран.
'help' - вывод справки по программе.
'random' - добавление случайной задачи на дату 'Today'
"""

task_list = {}
RANDOM_TASKS = ["Отремонтировать смеситель", "Написать письмо Гвидо", "Покормить хомяка", "Помыть машину"]


def check_date(date, title):
    if date in task_list:
        task_list[date].append(title)
    else:
        task_list[date] = [title]
    print(f"Задача '{title}' добавлена на дату {date}")


run = True
while run:
    command = input('Введите команду: ')
    if command == "add":
        date_task = input("Введите дату задачи: ")
        task_title = input("Введите название задачи: ")
        check_date(date_task, task_title)
    elif command == "show":
        date_task = input("Введите дату для отображения списка задач: ")
        if date_task in task_list:
            for task in task_list[date_task]:
                print(f"- {task}")
        else:
            print(f"Такой даты: {date_task} нет")
    elif command == "help":
        print(HELP)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    elif command == "random":
        random_task = random.choice(RANDOM_TASKS)
        check_date("today", random_task)
    else:
        print("Unknown command")


