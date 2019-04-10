import re
import functools
from functools import reduce
from operator import add
import collections
f = open('./day_3_input.txt', 'r')
text = f.read()
f.close()
splitText = re.sub(r'[\n]', ', ', text )
textArray = splitText.split(', ')
textArrayStripped = [x for x in textArray if x] #clear 'falsy'
SizeArray = map(lambda x: re.sub(r'.+@', '', x), textArrayStripped)
testarray = ['1,3: 4x4', '3,1: 4x4', '5,5: 2x2']
splitArray = map(lambda y: re.split('[,x:]', y), SizeArray)
def addSquares(array):
    fullArray = []
    base = [array[0], array[1]]
    for x in range(int(array[2])):
        for y in range(int(array[3])):
            fullArray.append(str(int(array[0]) + int(x)) + '.' + str(int(array[1]) + int(y)))
    return fullArray
fillArray = map(addSquares, splitArray)
joinedArray = reduce(add, fillArray)
def searchInAll(array):
    returnarray = []
    for x in range(len(array)):
        if array.count(array[x]) > 1:
            returnarray.append(array[x])
    return returnarray

# doubleSquares = searchInAll(joinedArray)
doubleSquares = [item for item, count in collections.Counter(joinedArray).items() if count > 1]
final = list(dict.fromkeys(doubleSquares))
print(final)
print(len(final))
