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

