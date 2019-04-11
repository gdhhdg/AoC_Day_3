import re
import functools
from functools import reduce
from operator import add
import collections
import itertools

f = open('day_3_input.txt', 'r')
text = f.read()
f.close()
splitText = re.sub(r'[\n]', ', ', text ) # split by new line
textArray = splitText.split(', ')
testarray = ['#1 1,3: 4x4', '#2 3,1: 4x4', '#3 5,5: 2x2']

textArrayStripped = [x for x in textArray if x] #clear 'falsy'

# part 1
SizeArray = map(lambda x: re.sub(r'.+@', '', x), textArrayStripped) #removes ID
splitArray = map(lambda y: re.split('[,x:]', y), SizeArray) #creates array of only digits so each can be worked with
def addSquares(array):  # To an array/list, add up all the used squares in a x.y format.
    fullArray = []
    base = [array[0], array[1]]
    for x in range(int(array[2])):
        for y in range(int(array[3])):
            fullArray.append(str(int(array[0]) + int(x)) + '.' + str(int(array[1]) + int(y)))
    return fullArray
fillArray = map(addSquares, splitArray)
joinedArray = reduce(add, fillArray) # combines each array into a single array to check for duplicates more easily
# def searchInAll(array):# searches for doubles and returns them into a single array
#     returnarray = []
#     for x in range(len(array)):
#         if array.count(array[x]) > 1:
#             returnarray.append(array[x])
#     return returnarray

# doubleSquares = searchInAll(joinedArray)## not used
doubleSquares = [item for item, count in collections.Counter(joinedArray).items() if count > 1] # faster way to find doubles
final = list(dict.fromkeys(doubleSquares)) #remove duplicates in array
print(final) # list of all squares that overlap
print(len(final)) # Count/Answer Confirmed.

part 2
idDictionary = {}
IDarray = map(lambda x: re.sub(r'@', '', x), textArrayStripped)
IDSplit = map(lambda y: re.split('[ ,x:]', y), IDarray)
nospace = map(lambda array: [x for x in array if x], IDSplit)#clear 'falsy'

def addSquaresWithID(array):  # To an array/list, add up all the used squares in a x.y format.
    fullArray = [str(array[0])]
    for x in range(int(array[3])):
        for y in range(int(array[4])):
            fullArray.append(str(int(array[1]) + int(x)) + '.' + str(int(array[2]) + int(y)))
    return fullArray
fillArrayID = map(addSquaresWithID, nospace)

def toDictionary(array):
    for each in array:
        idDictionary.update({each[0] : each[1:None]})

toDictionary(fillArrayID)
dupvals = [item for sublist in idDictionary.values() for item in sublist]
dups = []
dups = [item for item, count in collections.Counter(dupvals).items() if count > 1]
dups = set(dups)
for key,values in idDictionary.items():
    count = 0
    for value in values:
        if not value in dups:
            count += 1
            if count == len(values):
                print(key,' match')


