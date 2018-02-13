import string
import random
import time

#input
goal = input("       Enter goal string: ")
highestMatch = []
highestMatchCount = 0
listOfRandoms = []
runCount = 0
possibleIndexesToChange = []
matches = []
match = True
generationSize = 20

while highestMatchCount != len(goal):
    #index choices setup
    for i in range(0, len(goal)):
        possibleIndexesToChange.append(i)

    #initial builder
    for i in range(0, generationSize):
        time.sleep(0.05)
        if runCount == 0:
            randomList = []
            for i in range(len(goal)):
                randLetter = random.choice(string.ascii_letters)
                randomList.append(randLetter)
        
            randomString = ''.join(randomList)
            listOfRandoms.append(randomString)          
            zipped = list(zip(randomString, goal))
            highestMatch = randomString
            
        if runCount == 1:
            matches = []

	    #mutation
        else:
	        #random index
            while match == True:
                index = random.choice(possibleIndexesToChange)
                time.sleep(0.03)
                if index not in matches:
                    #del possibleIndexesToChange[index]
                    
                    match == False
                    break
            #random char
            newChar = random.choice(string.ascii_letters)
            print("\nInserting " + str(newChar) + " at index " + str(index) + ",\n")
            
            highestMatch = list(highestMatch)
            highestMatch[index] = newChar
            #cloning
            listOfRandoms.append(highestMatch)
            zipped = list(zip(highestMatch, goal))
        
        matchCount = 0
        for x, (i,j) in enumerate(zipped):
            if i == j:
                matchCount = matchCount + 1
                matches.append(x)        

                print("Del: " + str(x))
                #possibleIndexesToChange.pop(x)
                #del possibleIndexesToChange[x]

                print( i, '--', j)
            else:
                print( i, '  ', j)

        print( '\nLetter match count:', matchCount)
        
        #store new highest matched string
        if len(matches) > highestMatchCount:
            highestMatchCount = highestMatchCount + 1
            
        print("Lenth of goal word: " + str(len(goal)) + "\n\n")
        listOfRandoms = []
        
        if matchCount == len(goal):
            print("\nCorrect spelling found!\n")
            raise SystemExit
    runCount = runCount + 1
