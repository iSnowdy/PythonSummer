# We are trying to implement the Euclid's Algorithm using Python here
# First of all, we know that the GCD(A, B) if A or B is 0, then the other one is the MCD
# If none of them are, then we need to "Divide and Conquer" the problem to solve it. We reduce
# the problem until one of them is 0. To do that, we need to do a long division to find out
# the remainder. So that: GCD(A, B) = GCD(B, R). And with a simple recursive function we can
# call GCD(B, R) until A or B is 0
    
def longDivision(A, B):
    results = []
    q = A // B
    r = A % B
    results.append(q)
    results.append(r)
    return results

def GCD(A, B): # Base Cases first, then Recursive Case. The objective in recursive functions is to arrive to the Base Case(s)
    if A == 0: return B
    elif B == 0: return A
    else: return GCD(B, longDivision(A, B)[1]) # GCD(B, A % B) also works, but I wanted to make an extra function on purpose
        
print(GCD(270, 192))
print(GCD(252, 105))
print(GCD(48, 18))
print(GCD(1680, 640))