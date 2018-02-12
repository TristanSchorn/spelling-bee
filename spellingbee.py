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
possibleIndexesToChange = []
matches = []
match = True
generationSize = 20

while highestMatchCount != len(goal):
    
    #index choices setup
    for i in range(0, len(goal)):
        possibleIndexesToChange.append(i)
    
    for i in range(0, generationSize):
        time.sleep(0.05)
        if runCount == 0:
            #initial builder
            randomList = []
            for i in range(len(goal)):
                randLetter = random.choice(string.ascii_letters)
                randomList.append(randLetter)
        
            randomString = ''.join(randomList)
            listOfRandoms.append(randomString)
            #tester
            zipped = list(zip(randomString, goal))
            highestMatch = randomString
            
        if runCount == 1:
            matches = []
        else:
            #mutation
            while match == True:
                
                #index = random.randint(0, len(goal) - 1)
                index = random.choice(possibleIndexesToChange)
                
                time.sleep(0.03)
                #print("index rolled: " + str(index))
                if index not in matches:
                    #print("Not in matches: " + ''.join(str(matches)))
                    match == False
                    break
                #else:
                    #print("In matches!")

            newChar = random.choice(string.ascii_letters)
            print("\nInserting " + str(newChar) + " at index " + str(index) + ",\n")
            
            highestMatch = list(highestMatch)
            #print("highestMatch:: " + ''.join(highestMatch) )
            highestMatch[index] = newChar
            #cloning
            listOfRandoms.append(highestMatch)
            #print("Randomly produced strings: " + ', '.join(str(v) for v in listOfRandoms))
            #tester
            zipped = list(zip(highestMatch, goal))
        
        matchCount = 0
        for x, (i,j) in enumerate(zipped):
            
            if i == j:
                matchCount = matchCount + 1
                matches.append(x)
                print( i, '--', j)
            else:
                print( i, '  ', j)
            #print("Match count: " + str(matchCount))

        #print( '\n', matches)
        print( '\nLetter match count:', matchCount)
        
        #store new highest matched string
        if len(matches) > highestMatchCount:
            #highestMatchCount = len(matches)
            highestMatchCount = highestMatchCount + 1
            
            #highestMatch = randomString
        #print("Highest match: " + ''.join(highestMatch) + " with count " + str(highestMatchCount))
        print("Lenth of goal word: " + str(len(goal)) + "\n\n")
        listOfRandoms = []
        
        if matchCount == len(goal):
            print("\nCorrect spelling found!\n")
            raise SystemExit

        
    runCount = runCount + 1
    
    
