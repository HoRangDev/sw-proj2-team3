class Guess:

    def __init__(self, word):
        self.num_tries = 0
        self.guess_word = [c for c in word]
        self.black_box = ['_'] * len(word)
        self.guessed_char = []
        self.finish_flag = False

    def displayCurrent(self):
        return ''.join(self.black_box)

    def displayGuessed(self):
        return ', '.join(self.guessed_char)

    def displayGuessWord(self):
        return ''.join(self.guess_word)

    def is_usedChar(self, guessedChar):
        return True if guessedChar in self.guessed_char else False

    def guess(self, character):
        self.guessed_char.append(character)
        if character not in self.guess_word:
            self.num_tries += 1
            return False

        flag = False
        for i in range(len(self.guess_word)):
            if self.black_box[i] == '_' and self.guess_word[i] == character:
                self.black_box[i] = character
                flag = True
        return flag

    def is_finish(self):
        return False if '_' in self.black_box else True


