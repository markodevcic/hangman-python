import getpass
import os
import sys
from time import sleep


def hangman_0():
    print('_______')
    print('       ')
    print('       ')
    print('       ')


def hangman_1():
    print('_______')
    print('   O   ')
    print('       ')
    print('       ')


def hangman_2():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('       ')


def hangman_3():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('  /    ')


def hangman_4():
    print('_______')
    print('   O   ')
    print('   |   ')
    print('  / \  ')


def hangman_5():
    print('_______')
    print('  \O   ')
    print('   |   ')
    print('  / \  ')


def hangman_6():
    print('_______')
    print('  \O/  ')
    print('   |   ')
    print('  / \  ')


def hangman_7():
    print('_______')
    print('   O_| ')
    print('  /|\  ')
    print('  / \  ')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def esc_quit_game(key):
    quit_on = True

    while quit_on:
        if key == '\x1b':
            quit = input(
                'Završi igru? (DA->Enter, NE->Esc)\nQuit game? (YES->Enter, NO->Esc)'
            )
            if quit == '\x1b':
                clear()
                break
            elif quit == '':
                clear()
                print('Igra završava...\nThe game is quitting...',
                      end=' ',
                      flush=True)
                sleep(2)
                clear()
                sys.exit()
        else:
            quit_on = False


def set_language_intro():
    language_index = input('1. Hrvatski\n2. English\n\n')
    esc_quit_game(language_index)

    while True:

        if language_index not in ['1', '2']:
            language_index = input(
                'Izaberi jezik (1 ili 2)\nChoose a language (1 or 2)\n')
        elif language_index == '':
            language_index = input(
                'Prije Entera izaberi jezik (1 ili 2)\nBefore Enter choose a language (1 or 2)\n'
            )
        else:
            break

    language_index = int(language_index) - 1

    clear()

    print('\n')
    hello = ['    V J E Š A L A   ', '    H A N G M A N   ']
    for i in range(20):
        print(hello[language_index][i], end=' ', flush=True)
        sleep(0.2)

    return language_index


game = True

while game:

    clear()
    language_index = set_language_intro()

    while True:
        clear()
        term = list(
            getpass.getpass(
                ['Upiši pojam za pogađanje: ',
                 'Type a term to guess: '][language_index]).upper())
        start = input([
            '\nZa nastavak pritisni Enter\nZa novi unos bilo koju drugu tipku: ',
            '\nHit Enter to continue\nOr any key for new term: '
        ][language_index])
        if start == '':
            break

    clear()
    hidden_term = ''
    for char in term:
        if char == ' ':
            hidden_term += ' '
        elif char != ' ':
            hidden_term += '•'

    hangman_0()
    print(hidden_term)

    wrong_guesses = 0
    tried_guesses = []
    game_on = True

    while game_on:

        guess = input(['Pogodi slovo! ',
                       'Guess a character! '][language_index]).upper()

        while True:
            if len(guess) > 1:
                guess = input(
                    ['Upiši samo jedno slovo! ',
                     'Type only one character! '][language_index]).upper()
            elif guess == '':
                guess = input([
                    'Prije Entera upiši slovo! ',
                    'Before hitting Enter type a character! '
                ][language_index])
            elif guess in tried_guesses:
                guess = input([
                    'Slovo je već upotrijebljeno, probaj drugo! ',
                    'Character already used, try another! '
                ][language_index]).upper()
            else:
                break

        tried_guesses.append(guess)

        clear()
        for i in range(len(term)):
            if guess.upper() == ''.join(term[i]).upper():
                hidden_term = list(hidden_term)
                hidden_term[i] = guess.upper()

        if guess.upper() not in ''.join(term).upper():
            if wrong_guesses == 6:
                hangman_7()
                print(['\nJaoooooo!', '\nAuuuuuch!'][language_index])
                print(['\nRješenje je:\n', '\nThe solution is:\n'
                       ][language_index] + ''.join(term))
                game_on = False
                break
            else:
                wrong_guesses += 1

        if '•' not in hidden_term:
            print(['Pobjedaaaa!\n\n', 'You won!\n\n'][language_index] +
                  ''.join(term))
            print('\nBravooo!')
            game_on = False
            break

        board = vars()[f'hangman_{wrong_guesses}']()
        hidden_term = ''.join(hidden_term)
        print(hidden_term)

    replay = True
    while replay:
        print('\n')
        new_game = input([
            'Enter za novu igru\nEsc za kraj ',
            'Hit Enter for new game\nEsc to quit '
        ][language_index])
        if new_game == '':
            replay = False
        elif new_game == '\x1b':
            clear()
            game = False
            break
