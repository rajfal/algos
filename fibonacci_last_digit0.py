# Uses python3
from timeit import default_timer as timer


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
    
    
def get_fibonacci_last_digit_itrn(n):
#iterative solution
#613455
#0
#get_fibonacci_last_digit_itrn(613455)(Time used: 5.10/5.00, memory used: 9363456/536870912.)
#

    x = 0
    y = z = 1
    for i in range(0, n):
        x = y
        y = z
        z = x + y
        #y, z = z, x + y
        #print("--- i=" + str(i) + " x =" + str(x) + " y =" + str(y) + " z =" + str(z))
    #p= x % 10
    #print(str(p))
    return x % 10	  
    
def fibonacci_last_digit(n):
    # return last digit of the 1st element of the tuple
    return fast_dbl_fib(n)[0] % 10


def fast_dbl_fib(n):
 
    if n == 0:
        return (0, 1)
    else:
        a, b = fast_dbl_fib((n // 2))    
        #a = ... F(n) 
        #b = ... F(n+1) 
        
    c = 2*b - a    
    c = (a * c)     # F(2n) 
    d = (a*a + b*b) # F(2n + 1) 
    
    if(n%2 == 0):
        return (c, d)
    else:
        return (d, c+d)


if __name__ == '__main__':

    n = int(input())
    #start = timer()
    print(fibonacci_last_digit(n))
    #proc_time = timer() - start
    #print("fibonacci_last_digit(" + str(n) + ") took %f seconds" % proc_time)
