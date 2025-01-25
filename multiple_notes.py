from datetime import datetime
print("==МЕНЕДЖЕР ЗАМЕТОК==")
# Создаём список для хранения заметок
notes = []
# Создаём цикл для создания заметок
while True: # Задём пользователю вопрос о создании заметки
    user_answer = input("Желаете создать новую заметку?(да/нет):")
# Отрицательный ответ выводит из программы/завершает ввод заметок
    if user_answer.lower().strip() == "нет":
        print("До новых встреч!")
        break
# Положительный ответ просит пользователя ввести данные
    elif user_answer.lower().strip() == "да":
        username = input("Введите имя пользователя: ")
        title = input("Введите заголовок: ")
        content = input("Введите описание: ")
        status = input("Введите статус (например, 'Активна', 'Выполнена'): ")
# Проверяем верен ли формат даты создания и истечения заметки
        while True:
            add_date = input("Введите дату создания заметки (дд.мм.гггг) ")
            try:
                add_date = datetime.strptime(add_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Неверный формат даты!")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова")
        while True:
            dead_date = input("Введите дату истечения заметки (дд.мм.гггг): ")
            try:
                dead_date = datetime.strptime(dead_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Неверный формат даты!")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {str(e)}")
                print("Пожалуйста, попробуйте снова")
# Создаём словарь для хранения данных заметки
        note = {
            "Имя пользователя": username,
            "Заголовок": title,
            "Описание заметки": content,
            "Статус": status,
            "Дата создания": add_date.strftime("%d.%m.%Y"),
            "Дата истечения срока": dead_date.strftime("%d.%m.%Y")
        }
# Сохраняем введенные данные в наш список заметок
        notes.append(note)
    else:
        print("Ошибка! Выберите да или нет")
# Выводим список сохраненных заметок
print("\nСобранная информация о заметках:")
for index, note in enumerate(notes, start=1):
    print(f"\nЗаметка {index}:")
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")
