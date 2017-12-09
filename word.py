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
