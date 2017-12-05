from hangman import Hangman
from guess import Guess
from word import Word
from os import system


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()

    print(hangman.currentShape())
    print(guess.displayGuessed())
    while hangman.is_live():
        guessedChar = input('Select a letter: ')
        system('clear')
        if len(guessedChar) != 1:
            print(hangman.currentShape())
            print(guess.displayCurrent())
            print("tried : [" + guess.displayGuessed() + "]")
            print('One character at a time!')
            continue
        if guess.is_usedChar(guessedChar):
            print(hangman.currentShape())
            print(guess.displayCurrent())
            print("tried : [" + guess.displayGuessed() + "]")
            print('You already guessed \"' + guessedChar + '\"')
            continue

        correct = guess.guess(guessedChar)
        if not correct:
            hangman.decreaseLife()

        if guess.is_finish():
            finished = True
            break

        print(hangman.currentShape())
        print(guess.displayCurrent())
        print("tried : [" + guess.displayGuessed() + "]")


    if finished:
        print(hangman.currentShape())
        print('Success' + '[' + guess.displayGuessWord() + ']')
    else:
        print(hangman.currentShape())
        print('word [' + guess.displayGuessWord() + ']')
        print('guess [' + guess.displayCurrent() + ']')
        print('Fail')


if __name__ == '__main__':
    gameMain()
