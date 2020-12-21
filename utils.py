import random
from sympy import *
<<<<<<< Updated upstream
from Crypto.Hash import HMAC, SHA256
=======


def isPrime(x):
    count = 0
    for i in range(int(x / 2)):
        if x % (i + 1) == 0:
            count = count + 1
    return count == 1


# gives list of n primes starting from the K-th prime to L-th
def Random_n_Prime(k, l):
    numbers = [i for i in range(k, l + 1)]
    n_primes = []
    for i in range(l):
        rand = random.choice(numbers)
        n_primes.append(prime(rand))
        numbers.remove(rand)

    return n_primes


def Random_generators(n):
    Primes = [i for i in range(1, n + 1) if isPrime(i)]
    print(Primes)
    # chose one random prim from primes to find generator for it and return the generator
    n = (random.choice(Primes))
    print(n)
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a ** x) % n)
        if g == s:
            results.append(a)
    print(results)
    return random.choice(results)
>>>>>>> Stashed changes


def getRandom(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(1, greatestElement)
    return randomNumber


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def findGenerator(N):
    list = []
    for i in range(1, N):
        if gcd(N, i) == 1:
            list.append(i)
    return random.choice(list)


def prf(secretKey, elementsSet):
    res = []
    secretKeyByte = str(secretKey).encode('utf-8')
    HMac = HMAC.new(secretKeyByte, digestmod=SHA256)
    for i in elementsSet:
        element = str(i).encode('utf-8')
        HMac.update(element)
        pr = nextprime(int(HMac.hexdigest(), 16))
        res.append(pr)
    return res


<<<<<<< Updated upstream
def generate_crs(N, l):
    g = findGenerator(N)
=======
def generat_crs(N, l):
    g = Random_generators(N)

>>>>>>> Stashed changes
    distinct_Primes = prf(l)
    # or we just have to use l primes
    crs = str(N) + ' ' + str(g)
    for i in range(0, len(distinct_Primes)):
        crs = crs + ' ' + str(distinct_Primes[i])

    return crs
<<<<<<< Updated upstream
=======


def test_generator(g, number, size):
    l = {0}
    for i in range(size):
        l.add(g ** i % number)
    print(l)


test_generator(5,50,50)
>>>>>>> Stashed changes
