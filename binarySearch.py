#imports math library
import math as mt
def makeArray(length, step, element):
    arra = [element] * (step**length)
    index = 0
    for x in arra:
        product = 2**index
        arra[index] = product
        index+=1
    return arra
def binarySearch(arr, low, high, x):
    if high>=low:
        mid = (high+low)//2
        if arr[mid]==x:
            return arr[mid]
        elif x < mid:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)
    else:
        return -1
def printResult(result, length):
    if result==-1:
        print("Not found.")
    else:
        print("FOUND!!!!!!!!")
input = 536870912
length = 5
arra = makeArray(length, 2, 0)
print(arra)
result = binarySearch(arra, 0, len(arra)-1, input)
printResult(result,length)​