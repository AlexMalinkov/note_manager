from datetime import datetime
print("==МЕНЕДЖЕР ЗАМЕТОК==")
# Определяем текущую дату и формируем в удобный формат
date = datetime.now().strftime("%d.%m.%Y")
# Создаём список для хранения заметок
notes = []
# Создаём функцию для создания заметок
def create_note():
    username = input("Введите имя: ").strip()
    # Проверяем является ли поле пустым, просим заполнить
    while not username:
        print("Поле не может быть пустым")
        username = input("Введите имя: ").strip()
    title = input("Введите заголвок: ").strip()
    while not title:
        print("Поле не может быть пустым")
        title = input("Введите заголвок: ").strip()
    content = input("Введите описание: ").strip()
    while not content:
        print("Поле не может быть пустым")
        content = input("Введите описание: ").strip()
    status = input("Введите статус(например активна)").strip()
    while not status:
        print("Поле не может быть пустым")
        status = input("Введите статус(например активна)").strip()
    # Дату заполнения автоматически заполняем текущей датой
    created_date = date
    # Проверяем на нужный нам формат дату дедлайна
    while True:
        try:
            issue_date_as_str = input("Введите дату дедлайна(формат дд.мм.гггг): ").strip()
            issue_date = datetime.strptime(issue_date_as_str, "%d.%m.%Y")
            break
        except ValueError:
            print("Ошибка в формате даты")
    # Заносим собранные данные в словарь
    note = {"Username": username,
            "Title": title,
            "Content": content,
            "Status": status,
            "Created date": created_date,
            "Issue date": issue_date.strftime("%d.%m.%Y")
            }
    # Добавляем словарь с заметкой в список заметок
    notes.append(note)
    print("\nЗаметка создана")
    return note
# Создаём функцию для вывода на экран доступных заметок(если такие имеются)
def notes_list():
    if not notes:
        print("Нет доступных заметок")
    else:
        print("\nСобранная информация о заметках:")
        for index, note in enumerate(notes, start=1):
            print(f"\nЗаметка {index}:")
            for key, value in note.items():
                print(f"{key.capitalize()}: {value}")
# Добавляем блок взаимодействия с программой
while True:
    print("\nВыберите действие:\n1.Создать заметку"
                       "\n2.Вывести список доступных заметок\n3.Выход из программы")
    select = input("Ваш выбор: ").strip()
    if select == "1":
        create_note()
    elif select == "2":
        notes_list()
    elif select == "3":
        print("До новых встреч!")
        break
    else:
        print("Ошибка выбора")