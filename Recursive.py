# Recursive function basic example.
# Shows the Base Case (the way to "go out" of the function" first and then the Recursive Case itself
def countDown(i):
    print(i)
    if i <= 3:
        return
    else:
        countDown(i-1)
        
countDown(10)

# Showing how a recursive function uses the Call Stack
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(5))

def sum(arr):
    total = 0
    for x in arr: total += x
    return total
    
print(sum([2, 4, 6]))

# Lets change that last function into a recursive one
# First we must figure out the Base Case. The simplest array (list in Python) that we could get is one of 0 or 1 element in it
# Then we proceed to accomplish that Base Case with our Recursive Case

def recursiveSum(arr):
    if len(arr) == 0: return 0
    elif len(arr) == 1: return arr[0]
    else:
        return arr[0] + recursiveSum(arr[1:])
        
print(recursiveSum([2, 4, 6]))

# Now we will build our own "len()" function with a recursive function

testArr = [7, 4, 17, 2, 3, 15, 5]
print(testArr)
print(len(testArr))

def myLen(arr, len = 0): # We give len as a predetermined value. This will make it so we don't have to put it on the call function 
    if not arr: return len # "if not" will handle the case when the array (list in Python) is empty
    else:
        arr.pop()
        return myLen(arr, len + 1)
    
print("Longitud de la lista de: ", myLen(testArr[:])) 
# Here we are creatin a Shallow Copy of the List because we will be deleting elements from it. So we want to keep the original List 
# in its original form. Also, since its a shallow copy without explicitly assigning it to a variable, once the operation (the call function)
# is done, the copy will be freed from the memory by Python
print(testArr)

# Now lets find the maxium number in a list with a recursive function

def maxNumber(arr):
    if not arr: return max
    elif len(arr) == 1: return arr[0]
    
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1] # Returns the first number if it is bigger than the second. If not, then the second
    max = maxNumber(arr[1:])
    return arr[0] if arr[0] > max else max 
    # Returns the first number of the list if it is bigger than the already searched for max. It is needed since we are giving a reduced list every time
        
print("Max: ", maxNumber(testArr[:]))
print(len(testArr))

# Quicksort with recursion

import random

def quickSort(arr):
    if len(arr) < 2: return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1) # Random pivot instead of always the first one. This will make it so the running time is O(nlogn) in the avg/best case scenario
        pivot = arr[pivot_index]
       
        less = [i for i in arr if i < pivot] # Creation of a new list in a similar way of a for-each in Java
        greater = [i for i in arr if i > pivot] # This is called a "List Comprehension" in Python. The syntax is: [loop + original list + condition]
        
        return quickSort(less) + [pivot] + quickSort(greater)
        
print("Sorted: ", quickSort(testArr))