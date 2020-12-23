# import Crypto
# from Crypto.PublicKey import RSA
# from Crypto import Random
from Receiver import Receiver
from Sender import Sender
from utils import *


def run_protocol(Sender_set, Receiver_set):
    # Generating p q to compute N
    q = randprime(3, 15)
    p = randprime(15, 25)
    N = p * q
    print("RSA parameters are : ", " N = ", N, ", p =", p, ", q = ", q)
    secretKey = getRandom(100)
    print("The secret Key is ", secretKey, "and it should be secure transmitted")
    print("Generating a Generator g  \n ..........")
    g = findGenerator(N)
    print("g is now = ", g)
    print("\ncomputing the hash h\n........... ")
    receiver = Receiver(secretKey, g, N, Receiver_set)
    h = receiver.hashReceiver()
    print("the Hash h = ", h)



    return 1


run_protocol([7], [1, 2, 3])
