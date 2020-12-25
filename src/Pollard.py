import math as math
from helpers import gcd
import random
from MillerRabin import is_probable_prime

def Pollard_rho(n,N):
    def H(x):
        return (x*x + 1)%N
    
    x = random.randint(1, N - 1)
    d = gcd(x,N)
    if d != 1: 
        print('Factor found: ', d)
    y = x

    B = 2**(math.ceil(n/2))
    print('try 2^(n/2) = ', B, ' steps')
    i = 0
    while i < B:
        x = H(x)
        y = H(H(y))
        p = gcd((x - y)%N, N)
        if p != 1 and p != 0: 
            print('Factor found: ', p)
            return 
        i += 1
    print('Fail')
