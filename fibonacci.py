# Uses python3

import math

# research: 
# http://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python

from timeit import default_timer as timer


def calc_fib(n):
# naive recursive solution
# 45
# 1134903170
# calc_fib(45) took 400.565805 seconds	
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def sq_root (n):
	return math.sqrt(n)


def calc_fib_binnet(n):
# binnet formula solution
# 45
# 1134903170
# calc_fib(45) took 0.000077 seconds	
    if (n <= 1):
        return n
    else:
        sqrt_5 = sq_root(5)
        term_1 = ((1 + sqrt_5)/2)**n
        term_2 = ((1 - sqrt_5)/2)**n
 
        #return ((1+sq_root(5))**n-(1-sq_root(5))**n)/(2**n*sq_root(5)) 
        #return int((term_1-term_2)/sqrt_5)
        return (term_1 - term_2)/sqrt_5


def calc_fib_itrn(n):
#iterative solution
#45
#1134903170
#calc_fib(45) took 0.000091 seconds

    x = 0
    y = z = 1
    for i in range(0, n):
        x = y
        y = z
        z = x + y
        #print("--- i=" + str(i) + " x =" + str(x) + " y =" + str(y) + " z =" + str(z))
    #p= x % 10
    #print(str(p))
    return x	


n = int(input())

#start = timer()

print(calc_fib_itrn(n))
#proc_time = timer() - start
#print("calc_fib_itrn(" + str(n) + ") took %f seconds" % proc_time)


