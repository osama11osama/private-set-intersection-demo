from utils import *
from Receiver import *
from Sender import *
import time


def getSecretKey():
    ran = getRandom(1000)
    return ran


def protocol():
    p = 5
    q = 3
    N = p * q
    g = findGenerator(N)
    sKey = getSecretKey()
    receiver = Receiver(sKey, g, N, [13, 21, 2])
    tmp = receiver.hashReceiver()
    return tmp


a = protocol()
print(a)

