import math as math
import random
from MillerRabin import is_probable_prime
from QS import QS
from Pollard import Pollard_rho
import time

def GenPrime(n):
    p = random.getrandbits(n)
    while not is_probable_prime(p):
        p = random.getrandbits(n)
    return p

def GenModulus(n):
    p = GenPrime(n)
    q = GenPrime(n)
    while q == p:
        q = GenPrime(n)
    N = p * q
    print(N, p, q)
    return N,p,q

def TrialDivision(N):
    m = math.floor(math.sqrt(N) + 0.5)
    i = 3
    while i <= m:
        if N % i == 0:
            return i
        i += 1

def QSF(n, N):
    B = 2**(math.ceil(math.sqrt(n * math.log(n))))
    D = math.ceil(B ** 1.5 * math.log(n))
    if n == 50: 
        B = 8000
        D = 8000000
    if n == 60: 
        B = 12000
        D = 20000000
    print('B , D = ', B,' , ', D)
    print(QS(N,B,D))

if __name__ == "__main__":
    n = int(input('Please input security parameter n: '))
    method = int(input('What method?  1 for trial division, 2 for Pollard-rho, 3 for Quadratic Sieve.  '))
    N,p,q = GenModulus(n)
    t0 = time.process_time()
    if method == 1: 
        TrialDivision(N)
    elif method == 2: 
        Pollard_rho(n, N)
    else:
        QSF(n, N)
    print('Time used: ', time.process_time() - t0)




