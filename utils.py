from numpy import *
from sympy import *
from Crypto.Hash import HMAC, SHA256
from cryptohash import sha256


def getRandom(seed):
    randomNumber = random.randint(1, seed)
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
        tmp = int(HMac.hexdigest(), 16)
        tmp2 = (tmp / (10 ** 75))  # make hashing smaller for temporary
        pr = nextprime(tmp2)
        res.append(pr)
    return res
