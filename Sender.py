from utils import *
from fuzzy_extractor import FuzzyExtractor

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
        Ext = FuzzyExtractor(s, hRoh)
        result = [s, f, Ext]
        return result
