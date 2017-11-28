import random
from Hangman import *
from Helper import *

class WordDatabase:
    def __init__(self, file):
        fileInst = open(file, 'r')
        self.database = fileInst.read().split('\n')
        fileInst.close()

    def pick_random_word(self):
        return self.database[random.randrange(0, len(self.database))]

class GameInstance:
    def __init__(self, database):
        self.hangman = Hangman()
        self.database = database

    def showUI(self, bIsSurvived):
        if (bIsSurvived):
            print("Tries: " + str(self.hangman.get_max_life() - self.life))
            print("Wrong Answers: " + str(self.wrong_answer))
            print(self.hangman.get_character(self.life))
        else:
            print("Your dead!")
            print("The answer was \"" + self.word + "\"")

        player_input = input("Input( \"0\" to start new game, \"1\" to finish game) : ")
        return player_input


    def execute(self):
        bisRunning = True
        self.reset()

        while (bisRunning):
                bIsSurvived = self.life > 0
                player_input = self.showUI(bIsSurvived)

                if (player_input == "0"):
                    self.reset()
                elif (player_input == "1"):
                    bisRunning = False
                elif (player_input.isalpha() and len(player_input) == 1 and bIsSurvived):
                    self.input_sentence(player_input)
                    print("Current Answer: " + self.solved)
                else:
                    print("Wrong input! try again!")

    def reset(self):
        self.life = self.hangman.get_max_life()
        self.word = self.database.pick_random_word()
        self.solved = "_ " *  (len(self.word))
        self.wrong_answer = []

        print(self.word)

    def input_sentence(self, sentence):
        founded_list = findAll(self.word, sentence)
        if (len(founded_list) == 0):
            self.decrease_life()
            if (not (sentence in self.wrong_answer)):
                self.wrong_answer.append(sentence)
        else:
            solved_list = self.solved.split()
            for idx in founded_list:
                solved_list[idx] = sentence
            self.solved = " ".join(solved_list)

    def decrease_life(self):
        self.life -= 1

    def get_current_life(self):
        return self.life

    def get_current_word(self):
        return self.word;

if __name__ == "__main__":
    word_database = WordDatabase("words.txt")
    game_inst = GameInstance(word_database)
    game_inst.execute()