from hangman import Hangman
from guess import Guess
from word import Word


def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False  # bitmediyse false
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:  # en yuksek can in degerini kayit

        display = hangman.get(maxTries - guess.numTries)  # burasi neyi baslatip nasil degistiriyor
        print(display)  # can degerinden yanan candegerini cikarttigimizda kalan can degeri
        guess.display()

        guessedChar = raw_input('Select a letter:')
        print(guessedChar)
        if len(guessedChar) != 1:
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars:
            print('You already guessed \"' + guessedChar + '\"')  # tahmin ediline harfin olup olmadigini teyit eder
            continue

        finished = guess.guess(guessedChar)  # bu method neyi return yapmak icin bulunuyor
        if finished == True:  # guess class aldigi 1 tane harfi kayit
            break

    if finished == True:  # game in ortasinda bitirip cikmada  kull
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secret + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')




if __name__ == '__main__':

    gameMain()
