import math
from utils import *
import hmac
import hashlib


class Receiver:

    def __init__(self, crs, Sr):
        self.crs = crs
        self.Sr = Sr


    #1- we shuld have a function that generate random n prime
    #2- we have to finde a generator of an RSA modulu
    #3- we schuold have function that hashes the the receiver input (compute h) using the primes and the generator
    def hashReceiver(self):
        # """
        # :param self: crs string which is composed of an RSA modulus N = PQ,
        #             a uniformly random generator g ∈ ZN
        #             and pairwise distinct primes p1,....pl.
        # :return: hashed value of receiver h and random r
        # """

        primes = []
        tmp = self.crs.split(' ')
        N = int(tmp[0])
        g = int(tmp[1])
        primesT = list(map(int, tmp[2:]))
        r = getRandom(N)
        for i in self.Sr:
            if i in primesT:
                primes.append(i)
        product = math.prod(primes)
        h = g ** (r * product)
        res = [h, r]
        return res

    def checkIntersection(self, s, f, r, i, R):
        primes = []
        tmp = list(self.Sr)
        tmp.pop(i)

        tmpP = self.crs.split(' ')
        primesT = list(map(int, tmpP[2:]))

        for i in tmp:
            if i in primesT:
                primes.append(i)
        product = math.prod(primes)
        secArg = f ** (r * product)
        #############################
        sByte = s.to_bytes(2, byteorder='big')
        msg = secArg.to_bytes(2, byteorder='big')
        Hmac = hmac.new(sByte, b'', hashlib.sha3_256)
        Hmac.update(msg)
        extractor = Hmac.hexdigest()
        ##############################
        if extractor == R:
            return i
