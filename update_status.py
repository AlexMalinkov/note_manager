# Запрашиваем у пользователя текущий статус заметки
status = input("Введите статус заметки (например 'активна')")
print(f"Текущий статус заметки: {status}")
while True:
# Спрашиваем желает ли изменить статус
    answer = input("Желаете изменить статус заметки? (да/нет)")
    if answer.lower() == "нет":
        print(f"Статус заметки не изменён. Текущий статутс: {status}")
        break
# Если желает, то предлагаем варианты изменения
    elif answer.lower() == "да":
        print("Выберите новый статус:\n1.Завершена \n2.Отложена \n3.Отменена")
        pick = input("Выберите вариант (1,2 или 3)")
        if pick == "1":
            new_status = "Завершена"
        elif pick == "2":
            new_status = "Отложена"
        elif pick == "3":
            new_status = "Отменена"
        else:
            print("Выберите один из предложенных вариантов")
            continue
        status = new_status
        print(f"Новый статус заметки: {status}")
        break
    else:
        print("Выберите 'да' или 'нет'")




