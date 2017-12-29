import string
import random
import time

#input
goal = input("       Enter goal string: ")
highestMatch = []
highestMatchCount = 0
listOfRandoms = []
runCount = 0
goodGenes = []
matches = []
match = True

while highestMatchCount != len(goal):
    for i in range(0, 20):
        time.sleep(0.05)
        if runCount == 0:
            #initial builder
            randomList = []
            for i in range(len(goal)):
                randLetter = random.choice(string.ascii_letters)
                randomList.append(randLetter)
        
            randomString = ''.join(randomList)
            listOfRandoms.append(randomString)
            print("Randomly produced strings: " + ', '.join(str(v) for v in listOfRandoms))
            #tester
            zipped = list(zip(randomString, goal))
            highestMatch = randomString
            
        if runCount == 1:
            matches = []
        else:
            #mutation
            while match == True:
                index = random.randint(0, len(goal) - 1)
                time.sleep(0.03)
                #print("index rolled: " + str(index))
                if index not in matches:
                    #print("Not in matches: " + ''.join(str(matches)))
                    match == False
                    break
                #else:
                    #print("In matches!")

            newChar = random.choice(string.ascii_letters)
            print("index/newChar " + str(index) + str(newChar))
            highestMatch = list(highestMatch)
            print("highestMatch:: " + ''.join(highestMatch) )
            highestMatch[index] = newChar
            #cloning
            listOfRandoms.append(highestMatch)
            print("Randomly produced strings: " + ', '.join(str(v) for v in listOfRandoms))
            #tester
            zipped = list(zip(highestMatch, goal))
        
        for x, (i,j) in enumerate(zipped):
            if i == j:
                matches.append(x)
                print( i, '--', j)
            else:
                print( i, '  ', j)

        #print( '\n', matches)
        print( '\n Match count = ',len(matches))
        
        #store new highest matched string
        if len(matches) > highestMatchCount:
            highestMatchCount = len(matches)
            #highestMatch = randomString
        print("Highest match: " + ''.join(highestMatch) + " with count " + str(highestMatchCount))
        listOfRandoms = []
        
    runCount = runCount + 1
