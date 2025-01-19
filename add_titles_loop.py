# Запрашиваем у пользователя информацию
username = input("Введите имя пользователя: ")
# Создаём список заголовков заметки
titles = []
# Создаём цикл для ввода нескольких заголовков
while True:
    title = input("Введите заголовок заметки (или 'стоп' для завершения): ")
    if title.lower() == "стоп":
        break
# Проверяем пустой ли заголовок
    if title == "":
        print("Заголовок не может быть пустым")
    titles.append(title)
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
# Выводим все данные заметки. Дата выводится в формате дд-мм
print("Вы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметок:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date[0:5])
print("Дата истечения заметки:", issue_date[0:5])