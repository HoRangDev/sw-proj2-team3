import unittest
from Hangman_tb_game import *

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.database = WordDatabase("words.txt")
        self.game_inst = GameInstance(self.database)

    def tearDown(self):
        pass

    def testAnswer(self):
        self.game_inst.reset()
        self.game_inst.setWord("test")
        self.assertEqual(self.game_inst.get_current_input(), "_ _ _ _ ")
        self.game_inst.input_sentence("e")
        self.assertEqual(self.game_inst.get_current_input(), "_ e _ _")
        self.game_inst.input_sentence("t")
        self.assertEqual(self.game_inst.get_current_input(), "t e _ t")
        self.game_inst.input_sentence("s")
        self.assertEqual(self.game_inst.get_current_input(), "t e s t")

    def testLife(self):
        self.game_inst.reset()
        self.game_inst.setWord("test")

        initial_life = self.game_inst.get_current_life()
        self.game_inst.input_sentence("b")
        self.assertEqual(initial_life-1, self.game_inst.get_current_life())
        self.game_inst.input_sentence("k")
        self.assertEqual(initial_life-2, self.game_inst.get_current_life())
        self.game_inst.input_sentence("k")
        self.assertEqual(initial_life - 3, self.game_inst.get_current_life())
        self.game_inst.input_sentence("k")
        self.assertEqual(initial_life - 4, self.game_inst.get_current_life())
        self.game_inst.input_sentence("k")
        self.game_inst.input_sentence("k")
        self.game_inst.input_sentence("k")
        self.game_inst.input_sentence("k")
        self.assertEqual(0, self.game_inst.get_current_life())

if __name__ == "__main__":
    unittest.main()