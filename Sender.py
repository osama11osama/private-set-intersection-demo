from utils import *
import hashlib


class Sender:
    def __init__(self, secretKey, N, g, w, h, r):
        self.N = N
        self.w = w
        self.h = h
        self.g = g
        self.secretKey = secretKey
        self.r = r

    def computeSender(self):
        """

        :return: returns a list composed of s, f, Ext
        """
        primes = prf(self.secretKey, [w])
        Roh = getRandom(N)
        s = getRandom(N)
        f = self.g ** (Roh * primes[0])
        hRoh = self.h ** Roh
        #######################
        sByte = str(s).encode('utf-8')
        msg = str(hRoh).encode('utf-8')
        h = hashlib.sha3_256()
        h.update(msg + sByte)
        Ext = int(h.hexdigest(), 16)
        ########################
        result = [s, f, Ext, self.r]
        return result
