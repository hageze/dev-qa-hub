import random

word_list = [
    'ПИТОН', 'ДЖАВА', 'ХАКЕР', 'МОНИТОР', 'КЛАВИАТУРА', 'ПРОЦЕССОР', 'БРАУЗЕР',
    'СКРИПТ', 'ИНТЕРФЕЙС', 'ТЕСТИРОВЩИК', 'АЛГОРИТМ', 'КОНСТАНТА', 'ФУНКЦИЯ'
]

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print('Давайте играть в угадайку слов!')

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_completion)
        print(f'Осталось попыток: {tries}')

        guess = input('Введите букву: ').upper()

        if not guess.isalpha() or len(guess) != 1:
            print('Ошибка! Введите одну букву.')
            continue

        if guess in guessed_letters:
            print('Вы уже вводили эту букву.')
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f'Отлично! Буква {guess} есть в слове.')

            new_completion = ""
            for char in word:
                if char in guessed_letters:
                    new_completion += char
                else:
                    new_completion += "_"
            word_completion = new_completion

        else:
            print(f'Увы, буквы {guess} нет.')
            tries -= 1

        if '_' not in word_completion:
            guessed = True

    if guessed:
        print(display_hangman(tries))
        print(word_completion)
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print(display_hangman(0))
        print(f'Вы проиграли. Загаданное слово было: {word}')

# Создаем точку входа
def main():
    word = get_word()
    play(word)

# Запускаем программу
if __name__ == "__main__":
    main()