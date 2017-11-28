class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.numTries = 0
        self.F_tries = 0
        self.guessedChars = []
        self.k = list('_' * len(self.secretWord))

    def display(self):

        print("Current :", " ".join(self.k))
        print("Tries :", self.numTries)
        self.currentStatus = " ".join(self.k)


    def guess(self, character):

        count = 0

        s_word = list(self.secretWord)

        for i in range(0, len(s_word)):
            if s_word[i] == character:
                self.k[i] = character
                count += 1

        if count == 0:
            self.F_tries += 1

        self.numTries += 1
        self.guessedChars.append(character)
        
        if not '_' in self.k:
            return True
