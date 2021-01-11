from utils import *
from Receiver import *
from Sender import *


def protocol(Sr, Ss):
    p = 881
    q = 997
    N = p * q
    g = findGenerator(N)
    sKey = getRandom(1000)
    receiver = Receiver(sKey, g, N, Sr)
    h = receiver.hashReceiver()
    sen = Sender(sKey, N, g, Ss, h)
    send = sen.computeSender()
    primesI = prf(sKey, Sr)
    li = len(primesI)
    x = 0
    while x != li:
        receiver.checkIntersection(send[0], send[1], send[2], x, primesI)
        x += 1
    return 0


print("Enter the receiver elements separated by space:")
recInput = input()
recIn = list(map(int, recInput.split()))

print("Enter the sender element:")
senInput = input()
senIn = list(map(int, senInput.split()))

for i in senIn:
    protocol(recIn, i)

