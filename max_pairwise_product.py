# Uses python3
import random

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0


def FastPairwiseProduct1(a):
## attempt #1

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                product = a[i]*a[j]

    ## test result:
    ## Failed case #4/17: time limit exceeded (Time used: 10.00/5.00, memory used: 19103744/536870912.)            
    return product



def FastPairwiseProduct2(a):
## attempt #2
    # find max item list by value/index tuple
    high = list(max([(i,v) for v,i in enumerate(a)]))

    # remove that max item by its index
    del a[high[1]]
    #a.pop(high[1])

    max1 = high[0]
    # retrieve the next highest value
    max2 = max([(i) for v,i in enumerate(a)])

    ## test result:
    ## Good job! (Max time used: 0.21/5.00, max memory used: 36007936/536870912.) # a.pop()
    ## Good job! (Max time used: 0.20/5.00, max memory used: 35237888/536870912.) # del

    return max1*max2


def FastPairwiseProduct3(a):
## attempt #3
    # find max item list by value
    max1 = max(a)
    
    #if there more than two same values, return index of first only
    idx = [i for i,v in enumerate(a) if v==max1][0]
    
    # remove that max item by its index
    del a[idx]
    
    # retrieve the next highest value
    max2 = max([(i) for v,i in enumerate(a)])

    ## test result:
    ## Good job! (Max time used: 0.21/5.00, max memory used: 28086272/536870912.)

    return max1*max2
    
result = FastPairwiseProduct3(a)

print(result)
