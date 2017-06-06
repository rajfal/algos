# Uses python3


from timeit import default_timer as timer
    
    
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)
        
#def fibonacci(index):
#    return reduce(lambda r,v: r.append(r[-1]+r[-2]) or r , range(index), [0, 1])          
     
# (Public) Returns F(n).
def fibonacci(n):
    #if n < 0:
    #    raise ValueError("Negative arguments not implemented")
    return _fib(n)[0] 


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)     

if __name__ == "__main__":
	
	
	
    n = int(input())
    start = timer()
    '''
    for index, fibonacci_number in enumerate(fib()):
        #print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
        if index == n:
            #print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
            last_digit = fibonacci_number %10
            print(last_digit)
            break
    '''
    print(fibonacci(n))
    proc_time = timer() - start
    print("last_digit(" + str(n) + ") took %f seconds" % proc_time)
