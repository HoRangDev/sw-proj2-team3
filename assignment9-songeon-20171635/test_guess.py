import unittest
from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('test')
        self.g3 = Guess('ttt')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_______')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_e_____')
    def testDisplayGuessWord(self):
        self.assertEqual(self.g2.displayGuessed(), '')
        self.g2.guess('z')
        self.assertEqual(self.g2.displayGuessed(), 'z')
    def testIsFinish(self):
        self.assertEqual(self.g3.is_finish(), False)
        self.g3.guess('t')
        self.assertEqual(self.g3.is_finish(), True)


if __name__=='__main__':
    unittest.main()
