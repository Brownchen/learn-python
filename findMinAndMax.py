def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for x in L:
        if x<min:
            min = x
        if x>max:
            max = x
    print(min,max)
    return (min,max)

findMinAndMax([3,2,55,66,74,22])
