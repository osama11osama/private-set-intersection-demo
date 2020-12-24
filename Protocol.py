from utils import *
from Receiver import *
from Sender import *


def protocol():
    p = 881
    q = 997
    N = p * q
    g = findGenerator(N)
    sKey = getRandom(1000)
    print("Enter the receiver elements separated by space:")
    recInput = input()
    recIn = list(map(int, recInput.split()))
    receiver = Receiver(sKey, g, N, recIn)
    h = receiver.hashReceiver()
    print("Enter the sender element:")
    senInput = input()
    sen = Sender(sKey, N, g, senInput, h)
    send = sen.computeSender()
    primesI = prf(sKey, recIn)
    li = len(primesI)
    x = 0
    while x != li:
        receiver.checkIntersection(send[0], send[1], send[2], x, primesI)
        x += 1
    return 0


protocol()
