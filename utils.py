import random
from sympy import *


# changes
def getRandom(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(1, greatestElement)
    return randomNumber


def getRandomPrime(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(2, greatestElement)
    return randomNumber

def prf(greatestIndex):
    """
    TODO
    what should be the universeSize ?

    prf function returns the Universes U as a list

    seed will be the size limit of the set of primes
    """
    size = getRandom(greatestIndex)
    res = []
    size += 1
    for i in range(1, size):
        tmp = getRandom(greatestIndex)
        tmpP = prime(tmp)
        if tmpP not in res:
            res.append(tmpP)
        else:
            size += 1
    return res
#the first immplementation

def getRandomFromList(l):
	return l[getRandom(len(l))-1]

#is that really uniformly random?
def generators(x):
    n = getRandomFromList(prevPrimeList(x))
    
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a ** x) % n)
        if g == s:
            results.append(a)
    #Breturn (getRandomFromList(results),n)
    return getRandomFromList(results)
    


def prevPrimeList(n):
    n = n + 1
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

def generat_crs(N,l):
	g = generators (N)
	distinct_Primes= prf(l)
	crs = str(N)+' '+ str (g)
	for i in range(0,len(distinct_Primes)):
		crs = crs + ' ' + str(distinct_Primes[i])

	return crs

#print(prf(10))
#print(generat_crs(12,10))
print(generators(12))