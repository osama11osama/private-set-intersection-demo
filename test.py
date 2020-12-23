from Receiver import *
from utils import *


Sr = [2, 3, 4]
Ss = [3]
primes = [3, 5, 7]
N = 3 * 5
g = 5
r = 2
h = g **(r * 3 * 5 * 7)
roh = 3
hPowerRoh = h ** roh
seed = 4
f = g ** (roh * 5)
#############################
sByte = str(seed).encode('utf-8')
msg = str(hPowerRoh).encode('utf-8')
ha = hashlib.sha3_256()
ha.update(msg + sByte)
R = int(ha.hexdigest(), 16)
##############################
print("R =  ", R)

primes1 = [3, 5]
primes2 = [3, 7]
primes3 = [5, 7]

receiver = Receiver(123, g, N, Sr)


# sByte = str(seed).encode('utf-8')
# msg = str(f**(r*3*5)).encode('utf-8')
# ha = hashlib.sha3_256()
# ha.update(msg + sByte)
# R1 = int(ha.hexdigest(), 16)
# print("R1 = ", R1)
#
# sByte = str(seed).encode('utf-8')
# msg = str(f**(r*3*7)).encode('utf-8')
# ha = hashlib.sha3_256()
# ha.update(msg + sByte)
# R2 = int(ha.hexdigest(), 16)
# print("R2 = ", R2)
#
# sByte = str(seed).encode('utf-8')
# msg = str(f**(r*5*7)).encode('utf-8')
# ha = hashlib.sha3_256()
# ha.update(msg + sByte)
# R3 = int(ha.hexdigest(), 16)
# print("R3 = ", R3)
