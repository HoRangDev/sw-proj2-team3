import sys
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()

        self.initUI()

        self.showDB(self.getKey())

    def initUI(self):
        name = QLabel('Name: ')
        age = QLabel('Age: ')
        score = QLabel('Score: ')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        firstLineBox = QHBoxLayout()

        firstLineBox.addWidget(name)
        firstLineBox.addWidget(self.nameEdit)

        firstLineBox.addWidget(age)
        firstLineBox.addWidget(self.ageEdit)

        firstLineBox.addWidget(score)
        firstLineBox.addWidget(self.scoreEdit)

        amount = QLabel('Amount: ')
        self.amountEdit = QLineEdit()

        keyLab = QLabel('key: ')
        self.keyCombobox = QComboBox()
        self.keyCombobox.addItems(['Name', 'Age', 'Score'])

        secondLine = QHBoxLayout()
        secondLine.addStretch(100)
        secondLine.addWidget(amount)
        secondLine.addWidget(self.amountEdit)

        secondLine.addWidget(keyLab)
        secondLine.addWidget(self.keyCombobox)

        addButton = QPushButton('ADD')
        addButton.clicked.connect(self.addButtonEvent)

        delButton = QPushButton('DEL')
        delButton.clicked.connect(self.delButtonEvent)

        findButton = QPushButton('FIND')
        findButton.clicked.connect(self.findButtonEvent)

        incButton = QPushButton('INC')
        incButton.clicked.connect(self.incButtonEvent)

        showButton = QPushButton('SHOW')
        showButton.clicked.connect(self.showButtonEvent)

        thirdLine = QHBoxLayout()
        thirdLine.addStretch(100)
        thirdLine.addWidget(addButton)
        thirdLine.addWidget(delButton)
        thirdLine.addWidget((findButton))
        thirdLine.addWidget(incButton)
        thirdLine.addWidget(showButton)

        resLab = QLabel('Result:')
        self.resTex = QTextEdit()

        vrtLayout = QVBoxLayout()
        vrtLayout.addLayout(firstLineBox)
        vrtLayout.addLayout(secondLine)
        vrtLayout.addLayout(thirdLine)
        vrtLayout.addWidget(resLab)
        vrtLayout.addWidget(self.resTex)

        self.setLayout(vrtLayout)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def getKeyValue(self, key):
        if key == 'Name':
            return self.nameEdit.text()
        elif key == 'Age':
            return int(self.ageEdit.text())
        elif key == 'Score':
            return int(self.scoreEdit.text())
        elif key == 'Amount':
            return int(self.amountEdit.text())

    def getKey(self):
        return self.keyCombobox.currentText()

    def addButtonEvent(self, event):
        self.addDB(self.getKeyValue('Name'), self.getKeyValue('Age'), self.getKeyValue('Score'))
        self.showDB(self.getKey())

    def delButtonEvent(self, event):
        key = self.getKey()
        self.delDB(key, self.getKeyValue(key))
        self.showDB(key)

    def findButtonEvent(self, event):
        key = self.getKey()
        self.findDB(key, self.getKeyValue(key))

    def incButtonEvent(self, event):
        key = self.getKey()
        self.increseDB(key, self.getKeyValue(key), self.getKeyValue('Amount'))

    def showButtonEvent(self, event):
        key = self.getKey()
        self.showDB(key)

    def closeEvent(self, event):
        self.writeScoreDB();

    def readScoreDB(self):
        fH = open(self.dbfilename, 'rb')

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def addDB(self, name, age, score):
        record = {'Name': name, 'Age':age, 'Score':score}
        self.scoredb += [record]

    def delDB(self, key, keyValue):
        while self.isIn(key, keyValue):
            for p in self.scoredb:
                if p[key] == keyValue:
                    self.scoredb.remove(p)
        self.showDB(key)

    def showDB(self, sortKey):
        res = ""
        if (sortKey == 'Score'):
            for p in sorted(self.scoredb, key=lambda person: -person[sortKey]):
                for attr in sorted(p):
                    res += (attr + "=" + str(p[attr]) + '\t')
                res += '\n'
        else:
            for p in sorted(self.scoredb, key=lambda person: person[sortKey]):
                for attr in sorted(p):
                    res += (attr + "=" + str(p[attr]) + '\t')
                res += '\n'
        self.resTex.setText(res)

    def findDB(self, key, keyValue):
        res = ""
        for p in self.scoredb:
            if p[key] == keyValue:
                for attr in sorted(p):
                    res += (attr + "=" + str(p[attr]) + ' ')
                res += '\n'
        if len(res) == 0:
            res = "Nothing found with Key: " + key + " , Value: " + keyValue

        self.resTex.setText(res)

    def increseDB(self, key, keyValue, amount):
        for p in self.scoredb:
            if p[key] == keyValue:
                p['Score'] += amount
        self.showDB(key)

    def isIn(self, key, keyValue):
        for p in self.scoredb:
            if p[key] == keyValue:
                return True
        return False

    def bestDB(self):
        before = 0
        for p in sorted(self.scoredb, key=lambda person: -person['Score']):
            if (before <= p['Score']):
                for attr in sorted(p):
                    print(attr + "=" + str(p[attr]), end=' ')
                print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())