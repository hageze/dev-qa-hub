try:
    # Уровень 1 (внутри try) — 4 пробела
    user_input = input("Введи свой нынешний возраст: ")
    current_age = int(user_input)
    goal_age = 18

    # Все условия if/elif/else на том же уровне, что и current_age!
    if current_age < goal_age:
        # Уровень 2 (внутри if) — 8 пробелов
        years_to_go = goal_age - current_age
        print(f"Статус: эволюция в процессе. {years_to_go} года до точки B.")
    elif current_age == goal_age:
        print("Статус: Точка B достигнута. Переходим к следующему этапу.")
    else:
        print("Статус: Ветеран. Продолжай в том же духе.")

except ValueError:
    # Уровень 0 (вровень с try)
    print("Ошибка. Нужно вводить только цифры. Запусти программу снова.")