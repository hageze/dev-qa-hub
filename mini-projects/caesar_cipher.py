def caesar_cipher():
    # 1. Сбор вводных данных
    direction = input('Что делаем? (шифрование / дешифрование): ').lower()
    language = input('Выберите язык (русский / английский): ').lower()
    shift = int(input('Введите шаг сдвига (число): '))
    text = input('Введите текст: ')

    # 2. Настройка алфавитов
    if language == 'русский':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        n = 32
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        n = 26

    # Если дешифруем — просто меняем знак сдвига на минус
    if direction == 'дешифрование':
        shift = -shift

    result = ''

    # 3. Основной цикл обработки
    for char in text:
        if char.lower() in alphabet:
            # Находим индекс текущей буквы
            index = alphabet.find(char.lower())

            # Магия модульной арифметики (чтобы сдвиг зацикливался)
            new_index = (index + shift) % n

            # Получаем новую букву
            new_char = alphabet[new_index]

            # Возвращаем регистр (заглавная/строчная)
            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            # Если это пробел, цифра или знак — оставляем как есть
            result += char

    print(f'Результат: {result}')


if __name__ == '__main__':
    caesar_cipher()