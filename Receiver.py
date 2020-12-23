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
        tmp = pow(int(self.g), r, self.N)
        for i in primesT:
            tmp = pow(tmp, i, self.N)
        h = tmp
        self.r = r
        return h

    def checkIntersection(self, s, f, R, i, primesI):
        reV = primesI[i]
        del primesI[i]
        tmp = pow(f, self.r, self.N)
        for j in primesI:
            tmp = pow(tmp, j, self.N)
        secArg = tmp
        primesI.insert(i, reV)
        #############################
        sByte = str(s).encode('utf-8')
        msg = str(secArg).encode('utf-8')
        ha = hashlib.sha3_256()
        ha.update(msg + sByte)
        extractor = int(ha.hexdigest(), 16)
        ##############################
        print("ext:", extractor)
        if extractor == R:
            print("There is an intersection with index:", i)
        else:
            print("No intersection with index", i)
