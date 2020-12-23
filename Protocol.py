from utils import *
from Receiver import *
from Sender import *


def protocol(Sr, Ss):
    p = prime(getRandom(300))
    q = prime(getRandom(300))
    N = p * q
    g = findGenerator(N)
    print("N is ", N, ", p is ", p, ", q is", q, ", g is", g)
    sKey = getRandom(200)
    receiver = Receiver(sKey, g, N, Sr)  # [13, 3, 5] is Sr input
    print("PRF are:                ", prf(sKey, Sr))
    h = receiver.hashReceiver()
    sender = Sender(sKey, N, g, Ss, h)  # 2 is Ss input
    senderParameters = sender.computeSender()
    s = senderParameters[0]
    f = senderParameters[1]
    R = senderParameters[2]
    print("h =", h, ", s =", s, ", f =", f, "\nR =", R, "\n")
    receiver.checkIntersection(s, f, R, 0)
    receiver.checkInterS(s, f, R)

    return 0


protocol([1, 2, 3], 1)
