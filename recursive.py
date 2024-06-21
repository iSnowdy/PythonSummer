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