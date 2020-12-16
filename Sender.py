from utils import *
import hmac
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
        sByte = s.to_bytes(2, byteorder='big')
        msg = hRoh.to_bytes(2, byteorder='big')
        h = hmac.new(sByte, b'', hashlib.sha3_256)
        h.update(msg)
        Ext = h.hexdigest()
        ########################
        result = [s, f, Ext]
        return result