from random import randint

def is_valid(text, max_limit):
    if text.isdigit() and 1 <= int(text) <= int(max_limit):
        return True
    return False

print('Добро пожаловать в числовую угадайку')

while True:
    while True:
        limit_input = input('До какого числа будем угадывать? ')
        if limit_input.isdigit() and int(limit_input) > 0:
            limit = int(limit_input)
            break
        print('Введите целое положительное число для границы.')

    secret_number = randint(1, limit)
    counter = 0

    while True:
        print(f'Введите число от 1 до {limit}')
        num = input()

        if not is_valid(num, limit):
            print(f'А может быть все-таки введем целое число от 1 до {limit}?')
            continue

        num = int(num)
        counter += 1

        if num < secret_number:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif num > secret_number:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Число было угадано за {counter} попыток')
            break

    while True:
        again = input('Хотите сыграть еще раз? (д/н): ').lower()
        if again == 'д':
            play_again = True
            break
        elif again == 'н':
            play_again = False
            break
        else:
            print('Введи "д", если хочешь продолжить, или "н", если хочешь выйти.')

    if not play_again:
        print('Спасибо за игру! До встречи.')
        break