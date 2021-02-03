from sympy import *
from Crypto.Hash import HMAC, SHA256
import random


def getRandom(seed):
    randomNumber = random.randint(1, seed)
    return randomNumber


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def findGenerator(N):
    tmp = getRandom(N)
    if gcd(tmp, N) == 1:
        return tmp
    else:
        return findGenerator(N)


def prf(secretKey, elementsSet):
    res = []
    secretKeyByte = str(secretKey).encode('utf-8')

    for i in elementsSet:
        HMac = HMAC.new(secretKeyByte, digestmod=SHA256)
        element = str(i).encode('utf-8')
        HMac.update(element)
        tmp = int(HMac.hexdigest(), 16)
        pr = nextprime(tmp)
        res.append(pr)
    return res
