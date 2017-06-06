# Uses python3
import sys


def gcd_recursive(a, b):
#recursive solution, see gcd.py

    return a if b==0 else gcd_recursive(b, a%b)  
    
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_improved(a, b):
    gcdiv = 0
    gcdiv = gcd_recursive(a, b)
    lcm = a*b//gcdiv
    return lcm

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm_improved(a, b))

