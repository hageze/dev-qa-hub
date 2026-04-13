def main():
    direction = input('Что делаем? (шифрование / дешифрование): ').lower()
    language = input('Выберите язык (русский / английский): ').lower()
    shift = int(input('Введите шаг сдвига (число): '))
    text = input('Введите текст: ')

    if language == 'русский':
        alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        n = 32
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        n = 26

    if direction == 'дешифрование':
        shift = -shift

    result = ''

    for char in text:
        if char.lower() in alphabet:
            index = alphabet.find(char.lower())

            new_index = (index + shift) % n

            new_char = alphabet[new_index]

            if char.isupper():
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    print(f'Результат: {result}')


if __name__ == '__main__':
    main()