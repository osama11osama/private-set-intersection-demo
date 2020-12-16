from utils import *
from Receiver import *
from Sender import *

a = generat_crs(10, 15)
print(a)

re = Receiver(a, [2, 3, 4])
t = re.hashReceiver()

se = Sender(a, [3], t[0])
x = se.computeSender()

for i in range(0, 3):
    y = re.checkIntersection(x[0], x[1], x[2], 1, t[1])
    print(y)