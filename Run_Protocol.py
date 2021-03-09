from Receiver import *
from Sender import *
import random


def protocol(Sr, senderSet):
    p = 12009342892403487151
    q = 16745092048479459697
    N = p * q
    g = findGenerator(N)
    print("N is ", N, ", p is ", p, ", q is", q, ", g is", g)
    for Ss in senderSet:
        sKey = getRandom(200)
        receiver = Receiver(sKey, g, N, Sr)
        h = receiver.hashReceiver()
        sender = Sender(sKey, N, g, Ss, h)
        senderParameters = sender.computeSender()
        s = senderParameters[0]
        f = senderParameters[1]
        R = senderParameters[2]
        receiver.checkIntersection(s, f, R)

    return 0



rein = random.sample(range(2, 1000), 200)
print(rein)

print("Enter users number:")
users = int(input())

start = 1
while start <= users:
    print("user", start, "give your set:")
    senInput = input()
    senIn = list(map(int, senInput.split()))
    protocol(rein, senIn)
    start += 1

