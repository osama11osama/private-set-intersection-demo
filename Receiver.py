from utils import *
import hashlib


class Receiver:

    def __init__(self, secretKey, g, N, Sr):
        self.N = N
        self.Sr = Sr
        self.secretKey = secretKey
        self.g = g

    """Generating primes using PRF and then compute the hash value h """
    def hashReceiver(self):
        print("you are Now in hashReceiver")
        PRF_Primes_List = prf(self.secretKey, self.Sr)
        print("the PRF primes for Sr are :", PRF_Primes_List)
        r = getRandom(self.N)
        primesProd = math.prod(PRF_Primes_List)
        h = self.g ** (r * primesProd)
        res = [h, r]
        return res

    def checkIntersection(self, s, f, R, i, r):
        tmp = self.Sr
        tmp.pop(i)
        primes = prf(self.secretKey, tmp)
        primesProd = math.prod(primes)
        secArg = f ** (r * primesProd)
        #############################
        sByte = str(s).encode('utf-8')
        msg = str(secArg).encode('utf-8')
        ha = hashlib.sha3_256()
        ha.update(msg + sByte)
        extractor = int(ha.hexdigest(), 16)
        ##############################
        if extractor == R:
            return i
