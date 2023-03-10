import random
import math
from random import randint

def Q1():
    def shiftElements(data):
        if len(data) == 0:
            return

        temp = data[-1]
        for i in range(-1, -1 * len(data), -1):
            data[i] = data[i-1]
        data[0] = temp
        return data

    def getList(x):

        val = ''
        pos = 1
        list = []

        while (val != '!'):
            val = input('Enter value for list #' + str(x) +
                        ', position #' + str(pos) + ': ')
            if val == '!':
                print('List #' + str(x) + ':\t' + str(list))
                return list
            else:
                list.append(eval(val))
                pos = pos + 1

    def sameElements(list1, list2):
        shift = 0
        list2copy = list(list2)
        if len(list1) == len(list2copy):
            while (shift != len(list1)):
                if list1 == list2copy:
                    print('\t', list1)
                    print('\t\t And')
                    print('\t', list2)
                    print('\t\t Are Identical')
                    shift = len(list1)
                else:
                    list2copy = shiftElements(list2copy)
                    shift = shift + 1
        else:
            print('\t Not Identical')

    sameElements(getList(1), getList(2))


def Q2old():

    def getInput():
        input = [0] * 20
        for i in range(20):
            input[i] = random.randint(1, 6)
        print(input)
        return input

    def bracketStat(x, val, k):
        open = ' '

        if val[k] != val[k+1]:
            if x == ' ) ':
                print(val[k], end=open)            
            elif x == ' ( ':
                x = ' ) '
                print(val[k], end=x)
            if x == ' ) ' and val[k+1] == val[k+2]:
                x = ' ( '
                print(x, end=open)
            else:
                print(val[k], end=open)
        else:
            print(val[k], end=open)

    inputString = getInput()
    print(inputString)
    x = ' ) '

    for k in range(18):
        bracketStat(x, inputString, k)

def Q2():
    string = [random.randrange(1, 7) for i in range(20)]
    runVal = []
    print(string)
    runStat = False
    run = ""
    for i in range(len(string)):
        if runStat:
            if string[i] != string[i - 1]:
                run = ""
                runVal.append(run)
                runStat = False
                continue
            else:
                run += str(string[i])

        if not runStat:
            if i != len(string) - 1:
                if string[i] == string[i + 1]:
                    runStat = True
                    run += str(string[i])
    runVal = sorted(runVal, key=len)
    result = ""
    print("\n")
    if (len(runVal) > 0):
        result = result.join(str(x) for x in string)
        result = result.replace(runVal[-1], "(" + runVal[-1] + ")", 1)
    print('result: ', result)

Q2()

