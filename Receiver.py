from utils import *
import hashlib


class Receiver:

    def __init__(self, secretKey, g, N, Sr):
        self.N = N
        self.Sr = Sr
        self.secretKey = secretKey
        self.g = g
        self.PRF_Primes = prf(self.secretKey, self.Sr)
        self.r = getRandom(self.N)

    def hashReceiver(self):
        print("in hashReceiver PRF are:", self.PRF_Primes)
        tmp = pow(int(self.g), self.r, self.N)
        for i in self.PRF_Primes:
            tmp = pow(tmp, i, self.N)
        h = tmp
        return h

    def checkIntersection(self, s, f, R):

        for i in range(3):
            tmpPRF = self.PRF_Primes
            iPrime = tmpPRF[i]
            del tmpPRF[i]
            tmp = pow(f, self.r, self.N)
            for j in tmpPRF:
                tmp = pow(tmp, j, self.N)
            primeProd = tmp
            #############################
            sByte = str(s).encode('utf-8')
            message = str(primeProd).encode('utf-8')
            hashObj = hashlib.sha3_256()
            hashObj.update(message + sByte)
            extractor = int(hashObj.hexdigest(), 16)
            ##############################

            print("ext in index ", i, " is :",  extractor)
            if extractor == R:
                print("There is an intersection with index:", i)
            else:
                print("No intersection with index", i)

        #
        # reV = self.PRF_Primes[i]
        # del self.PRF_Primes[i]
        # tmp = pow(f, self.r, self.N)
        # for j in self.PRF_Primes:
        #     tmp = pow(tmp, j, self.N)
        # secArg = tmp
        # self.PRF_Primes.insert(i, reV)
        # #############################
        # sByte = str(s).encode('utf-8')
        # msg = str(secArg).encode('utf-8')
        # ha = hashlib.sha3_256()
        # ha.update(msg + sByte)
        # extractor = int(ha.hexdigest(), 16)
        # ##############################
        # print("ext:", extractor)
        # if extractor == R:
        #     print("There is an intersection with index:", i)
        # else:
        #     print("No intersection with index", i)
