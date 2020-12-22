from utils import *
import hashlib


class Receiver:

    def __init__(self, secretKey, g, N, Sr):
        self.N = N
        self.Sr = Sr
        self.secretKey = secretKey
        self.g = g
        self.r = 0

    def hashReceiver(self):
        primesT = prf(self.secretKey, self.Sr)
        r = getRandom(self.N)
        product = math.prod(primesT)
        a = r * product
        tmp = self.g
        h = int(tmp) ** int(a)
        self.r = r
        return h

    def checkIntersection(self, s, f, R, i):
        tmp = self.Sr
        tmp.pop(i)
        primes = prf(self.secretKey, tmp)
        product = math.prod(primes)
        secArg = f ** (self.r * product)
        #############################
        sByte = str(s).encode('utf-8')
        msg = str(secArg).encode('utf-8')
        ha = hashlib.sha3_256()
        ha.update(msg + sByte)
        extractor = int(ha.hexdigest(), 16)
        ##############################
        if extractor == R:
            return i
