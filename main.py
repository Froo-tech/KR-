# Vodopianov Aleksandr AI-71 LEVEL HARD

# Функция для преобразования килобайт в мегабайты и бит
def kb():
    try:
        # Ввод данных от пользователя
        kb = int(input("Введите количество килобайт: "))

        # Преобразование в мегабайты
        mb = kb / 1024
        print(f'{kb} KB = {mb:.2f} MB')
        # Преобразование в байт
        bit = kb * 1024
        print(f'{kb} KB = {bit} бит')
        # Преобразование в биты
        bits = kb * 1024 * 8
        print(f'{kb} KB = {bits} бит')

    except ValueError:
        print('Ошибка: Введите корректное целое число.')


# Функция для подсчета бит информации
def bits():
    try:
        # Ввод данных от пользователя
        lines = int(input("Введите количество строк: "))
        chars = int(input("Введите количество символов: "))
        alphabet_size = int(input("Введите размер алфавита: "))

        # Общий размер символов
        tot_chars = lines * chars

        # Подсчет бит информации
        bits = tot_chars * 5

        # Вывод результата
        print(f'Общее количество бит: {int(bits)}')

    except ValueError:
        print("Ошибка: Введите корректное целое число.")
    except Exception:
        print('Ошибка:')


# Функция для определения подходящей одежды по погоде
def check():
    try:
        ans1 = input("Хорошая погода? (да/нет) \n").strip().lower()

        if ans1 in ["да", "yes"]:
            ans2 = input("Тепло? (да/нет) \n").strip().lower()
            if ans2 in ["да", "yes"]:
                print("Надеть шорты и майку.")
            elif ans2 in ["нет", "no"]:
                print("Надеть кофту.")
            else:
                print("Вы ввели что-то не то.")
        elif ans1 in ["нет", "no"]:
            ans2 = input("Идет дождь? (да/нет) \n").strip().lower()
            if ans2 in ["да", "yes"]:
                print("Взять зонт.")
            elif ans2 in ["нет", "no"]:
                ans3 = input("Холодно? (да/нет) \n").strip().lower()
                if ans3 in ["да", "yes"]:
                    print("Надеть куртку.")
                elif ans3 in ["нет", "no"]:
                    print("Не могу понять.")
                else:
                    print("Вы ввели что-то не то.")
            else:
                print("Вы ввели что-то не то.")
        else:
            print("Вы ввели что-то не то.")
    except Exception:
        print('Ошибка:')

# Пример использования функций (раскомментируйте, чтобы использовать)
kb()
# bits()
# check()
