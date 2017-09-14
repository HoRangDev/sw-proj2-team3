import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				check = int(parse[3])
				check = int(parse[2])
			except:
				print("Wrong Input!: You must write like this.=> add Name Age Score")
			else:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':int(parse[3])}
				scdb += [record]
		elif parse[0] == 'del':
			try:
				check = parse[1]
			except:
				print("Wrong Input!:")
			else:
				while isIn(scdb, parse[1]):
					for p in scdb:
						if p['Name'] == parse[1]:
							scdb.remove(p)
		elif parse[0] == 'show':
			sortKey ='Name'
			showScoreDB(scdb, sortKey)

		elif parse[0] == 'find':
			try:
				check = parse[1]
			except:
				print("Check your input!")
			else:
				findDB(scdb, parse[1])

		elif parse[0] == 'findNA':
			try:
				check = int(parse[2])
			except:
				print("Wrong Input!")
			else:
				findNADB(scdb, parse[1], int(parse[2]))
				
		elif parse[0] == 'inc':
			try:
				check = int(parse[2])
			except:
				print("Check your input!")
			else:
				increseDB(scdb, parse[1], int(parse[2]))

		elif parse[0] == 'best':
			bestDB(scdb)

		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + str(p[attr]), end=' ')
		print()

def isIn(scdb, keyname):
	for p in scdb:
		if p['Name'] == keyname:
			return True
	return False

def findDB(scdb, keyname):
	for p in scdb:
		if p['Name'] == keyname:
			for attr in sorted(p):
				print(attr + "=" + str(p[attr]), end=' ')
			print()

def findNADB(scdb, name, age):
	for p in scdb:
		if (p['Name'] == name) and (p['Age'] == age):
			for attr in sorted(p):
				print(attr + "=" + str(p[attr]), end=' ')
			print()

def increseDB(scdb, keyname, amount):
	for p in scdb:
		if p['Name'] == keyname:
			p['Score'] += amount

def bestDB(scdb):
	before = 0
	for p in sorted(scdb, key=lambda person: -person['Score']):
		if (before <= p['Score']):
			for attr in sorted(p):
				print(attr + "=" + str(p[attr]), end=' ')
			print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
