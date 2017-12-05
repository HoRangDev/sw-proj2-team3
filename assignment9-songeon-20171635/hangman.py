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
    def __init__(self):
        self.remainingLives = len(self.text) - 1

    def decreaseLife(self):
        self.remainingLives  -= 1

    def currentShape(self):
        return self.text[self.remainingLives]

    def is_live(self):
        return True if self.remainingLives > 0 else False


