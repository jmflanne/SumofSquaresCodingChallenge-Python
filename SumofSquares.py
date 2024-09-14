#Sum of Squares Coding Challenge
#Name: Jenna Flannery

#calculate sum of squares of given integers for each test case, do not include negative numbers in calculation
#rules:
#no for or while loops, no list/set/dictionary comprehension, no global variables

#import sys is used for sys.exit() in exception handling
import sys
#removeSpace removes whitespace in string and returns string
def removeSpace(inputInts):
    finalInputInts = inputInts.split()
    return finalInputInts

#formatInput converts numbers in string array into integers and removes negative numbers, returns converted string array
def formatInput(numInts, inputInts):
    try:
        numInts -= 1
        if numInts >= 0:
            inputInts[numInts] = int(inputInts[numInts])
            if ((inputInts[numInts] > 100) or (inputInts[numInts] < -100)):
                raise Exception()
            return formatInput(numInts, inputInts)
    except IndexError:
        print("Number of integers did not match input. Error at formatInput")
        sys.exit()
    except ValueError:
        print("Input should only include integers. Error at formatInput")
        sys.exit()
    except:
        print("Input should be between -100 and 100. Error at formatInput")
        sys.exit()
            
    else:
        return inputInts

#sumOfSquares adds new square to ongoing sum, returns sum
def sumOfSquares(newInt,currentSum):
    if newInt > 0:
        square = newInt ** 2
        currentSum += square
    return currentSum

#getInput retrieves the number of integers and the integers from the user, calls conversion functions to properly format data
#and returns the input in an array in the format [numInts,integerData]
def getInput():
    testCaseDataArr = []
    try:
        numInts = int(input())
        if ((numInts <= 0) or (numInts > 100)):
            raise Exception()
    except:
        print("Integer value incorrect. Error at getInput")
        sys.exit()
    integerData = input()
    #format data before adding it to array
    integerData = removeSpace(integerData)
    integerData = formatInput(numInts,integerData)
    #add to array
    testCaseDataArr.append(numInts)
    testCaseDataArr.append(integerData)
    return testCaseDataArr

#testCaseData uses the number of test cases to ask user for data related to each test case using getInput()
def testCaseData(numTestCases,testCases):
    numTestCases -= 1
    if numTestCases >= 0:
        testCases.append(getInput())
        testCaseData(numTestCases,testCases)
            
#incrementSum uses numInts to go through array of integers and find the target sum for the test case
def incrementSum(numInts,inputInts,intSum):
    try:
        numInts -= 1
        if numInts >= 0:
            currentInt = inputInts[numInts]
            intSum = sumOfSquares(currentInt,intSum)
            return incrementSum(numInts,inputInts,intSum)
    except TypeError:
        print("Number of integers did not match input. Error at incrementSum")
        sys.exit()
    else:
        return intSum
#initializes sum to 0, uses increment sum to find target sum and returns it
def calculate(numInts,inputInts):
    intSum = 0
    intSum = incrementSum(numInts,inputInts,intSum)
    return intSum

#final function that starts the search for the sum, writes them to console in the order that user inputted corresponding test case
def getOutput(numTestCases,testCases,index):
    numTestCases -= 1
    finalSum = 0
    if numTestCases >= 0:
        finalSum = calculate(testCases[index][0],testCases[index][1])
        print(finalSum)
        index += 1
        return getOutput(numTestCases,testCases,index)
    else:
        return

#start() gets number of test cases from user and uses that to get output
def start():
    try:
        numTestCases = int(input())
        if ((numTestCases < 1) or (numTestCases > 100)):
            raise Exception("incorrect value")
    except:
        print("Incorrect value entered. Number should be greater than or equal to 1 and less than or equal to 100. Error at start")
        sys.exit()
    #create an array of test cases, that will hold arrays representing each test case
    testCases = []
    testCaseData(numTestCases,testCases)
    #data gathered, now we compute
    getOutput(numTestCases,testCases,0)


def main():
    #run start function to begin:
    start()
if __name__=="__main__":
    main()
