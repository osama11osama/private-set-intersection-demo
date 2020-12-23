from utils import *
from Receiver import *
from Sender import *


def protocol():
    p = 5
    q = 17
    N = p * q
    g = findGenerator(N)
    sKey = getRandom(100)
    receiver = Receiver(sKey, g, N, [13, 3, 5])  # [13, 3, 5] is Sr input
    h = receiver.hashReceiver()
    print("h =", h)
    sen = Sender(sKey, N, g, 5, h)  # 2 is Ss input
    send = sen.computeSender()
    print("s =", send[0])
    print("f =", send[1])
    print("R =", send[2], "\n")
    primesI = prf(sKey, [13, 3, 5])  # [13, 3, 5] is Sr input
    li = len(primesI)
    x = 0
    while x != li:
        receiver.checkIntersection(send[0], send[1], send[2], x, primesI)
        x += 1
    return 0


protocol()
