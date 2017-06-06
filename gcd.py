# Uses python3


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    
    
    
def gcd_recursive(a, b):
#recursive solution
#45
#1134903170
#calc_fib(45) took 0.000091 seconds

#blog.adamklein.com/?p=334
    
    return a if b==0 else gcd_recursive(b, a%b)    

if __name__ == "__main__":
	
	
	
    a, b = map(int, input().split())
    
    print(gcd_recursive(a, b))
