# Определяем текущую дату и формируем её на удобный формат
from datetime import datetime
data = datetime.now()
f_data = data.strftime('%d.%m.%Y')
print("Текущая дата :", f_data)
# Основной блок программы
while True:
    try:
        # Запрашиваем дату дедлайна у пользователя
        dead_data = input("Введите дату дедлайна в формате дд.мм.гггг: ")
        # Преобразуем строку с датой в объект datetime
        dead_data = datetime.strptime(dead_data, "%d.%m.%Y")
        # Вычисляем разницу между текущей датой и датой дедлайна
        dif_data = dead_data - data
        day_dif_data = dif_data.days
        # Проверяем статус дедлайна и выводим соответсвующий результат
        if day_dif_data < 0:
            print(f"Срок истёк {abs(day_dif_data):02d} дня назад")
        elif day_dif_data == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До истечения срока {day_dif_data:02d} дней")
        break
    # Обработка неверно введенного формата даты
    except ValueError:
        print("Ошибка! Введён неверный формат даты(дд.мм.гггг)")
    # Обработка прочих ошибок
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова")