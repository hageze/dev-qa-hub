import random

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'

chars = ''

num_passwords = int(input('Количество паролей для генерации: '))
len_password = int(input('Длина одного пароля: '))

if input('Включать цифры? (д/н): ').lower() == 'д':
    chars += digits
if input('Включать прописные буквы? (д/н): ').lower() == 'д':
    chars += uppercase_letters
if input('Включать строчные буквы? (д/н): ').lower() == 'д':
    chars += lowercase_letters
if input('Включать символы !#$%&*+-=?@^_? (д/н): ').lower() == 'д':
    chars += punctuation
if input('Исключать неоднозначные символы il1Lo0O? (д/н): ').lower() == 'д':
    for c in ambiguous:
        chars = chars.replace(c, '')

if not chars:
    print('\nОшибка: Вы не выбрали ни одного набора символов!')
else:
    print('\nВаши сгенерированные пароли:')
    for _ in range(num_passwords):
        print(generate_password(len_password, chars))