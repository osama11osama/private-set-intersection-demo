import random


def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1

def Random_n_Prime(minNumber, n):
    #genrate primes from minNumber to minNumber**2
    primes = [i for i in range(minNumber,minNumber**2) if isPrime(i)]
    #Chose n random prime from primes and return it
    n_primes = []
    for i in range(n):
        rand= random.choice(primes)
        n_primes.append(rand)
        primes.remove(rand)

    return n_primes
 
def Random_generators(n):
    #genrate primes under n
    primes = [i for i in range(1,n) if isPrime(i)]
    #chose one random prim from primes to finde genrator for it and return the genrator
    n = random.choice(primes)
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a**x) % n)
        if g == s:
            results.append(a)
    #print(results)
    return random.choice(results)

# changes
def getRandom(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(1, greatestElement)
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

def getRandomFromList(l):
	return l[getRandom(len(l))-1]

def generat_crs(N,l):
	g = generators (N)
	distinct_Primes= prf(l)
	crs = str(N)+' '+ str (g)
	for i in range(0,len(distinct_Primes)):
		crs = crs + ' ' + str(distinct_Primes[i])

	return crs


def test_generator (g, number , size):
    l = {0}
    for i in range(size):
     l.add(g**i %number)
    print(l)

print(getRandom(100))
print(Random_generators(1000))
print(Random_n_Prime(23,10))
