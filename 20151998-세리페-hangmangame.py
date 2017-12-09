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
    
    
class Guess:
    def __init__(self, word):
        self.secret = word
        self.guessedChars = ""
        self.numTries = 0
        self.currentStatus ="_"
        self.db={}
        for k in range(len(self.secret)):
            self.currentStatus+="_"
            self.db[k]="_"


    def display(self):
        print("current:%s" % self.currentStatus)
        print("tries: %d" % self.numTries)


    def guess(self, character):
        self.guessedChars += character
        temp=""
        if (self.secret.find(character)==-1):
            self.numTries += 1
            return
        for k in range (len(self.secret)):
            if (character==self.secret[k]):
                self.db[k]=character
        for k in range (len(self.secret)):
            temp+=self.db[k]
            self.currentStatus=temp

        if (self.secret == self.currentStatus):
            return True
      
      
      
      
class Hangman:

    text = [

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

    ]



    def getLife(self):
        return len(self.text) - 1


    def get(self, life):
        return self.text[life]
        
        
import random

class Word:

    def __init__(self, filename):

        self.words = []#file acip satir satir bolup liste yaptigimiz dosyayayi kapat
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()#rstrip  nedem kulllaniliyor
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):
        #kelime database nin index kapsamin icinde numara olusturarak denk yerine kelime return

        r = random.randrange(self.count)
        return self.words[r]
