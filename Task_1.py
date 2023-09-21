
# print(f'{data} {task}')

value_dict = {}

for step in range(3):
    data = input("Введите дату: ")
    task = input("Введите задачу: ")
    value_dict[data] = task

print(value_dict)
