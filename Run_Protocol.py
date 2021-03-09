from utils import *
from Receiver import *
from Sender import *


def protocol(Sr, senderSet):
    p = 1021
    q = 1597
    N = p * q
    g = findGenerator(N)
    print("N is ", N, ", p is ", p, ", q is", q, ", g is", g)
    for Ss in senderSet:

        sKey = getRandom(200)
        receiver = Receiver(sKey, g, N, Sr)
        # print("PRF are:                ", prf(sKey, Sr))
        h = receiver.hashReceiver()
        sender = Sender(sKey, N, g, Ss, h)
        senderParameters = sender.computeSender()
        s = senderParameters[0]
        f = senderParameters[1]
        R = senderParameters[2]
        # print("h =", h, ", s =", s, ", f =", f, "\nR =", R, "\n")
        receiver.checkIntersection(s, f, R)

    return 0


protocol([3, 4], [1, 3, 5, 4])
