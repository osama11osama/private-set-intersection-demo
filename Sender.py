from utils import *
import hashlib

LIST_INDEX = 1


class Sender:
    def __init__(self, crs, w, h):
        self.crs = crs
        self.w = w
        self.h = h

    def computeSender(self):
        """
        :return: returns a list composed of s, f, Ext
        """
        tmp = self.crs.split(' ')
        N = int(tmp[0])
        g = int(tmp[1])
        primes = list(map(int, tmp[2:]))
        Roh = getRandom(N)
        s = getRandom(N)
        f = g ** (Roh * primes[self.w + 1])
        hRoh = self.h ** Roh
        #######################
        sByte = str(s).encode('utf-8')
        msg = str(hRoh).encode('utf-8')
        h = hashlib.sha3_256()
        h.update(msg + sByte)
        Ext = int(h.hexdigest(), 16)
        ########################
        result = [s, f, Ext]
        return result