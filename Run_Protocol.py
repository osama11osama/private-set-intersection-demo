# import Crypto
# from Crypto.PublicKey import RSA
# from Crypto import Random
from Receiver import Receiver
from Sender import Sender
from utils import Random_n_Prime, Random_generators


def run_protocol(Sender_set, Receiver_set):
    # what is the max size of the U ? we did not understand the idea of PRF to use it fo Large Universe
    U = max(Sender_set + Receiver_set)
    # should we generate l prime? or there is a better Idea?
    primes = Random_n_Prime(1, U)
    # Where we have to use the RSA param?

    # chose P and Q then Compute N
    P = 1987
    Q = 6997
    N = P * Q
    # Is the generator have to be a generator for random i < N
    g = Random_generators(N)
    primes_string = ""
    for i in range(U):
        primes_string += str(primes[i]) + " "

    crs = str(N) + " " + str(g) + " " + primes_string

    w = 0
    h = 0
    receiver = Receiver(crs, Receiver_set)
    sender = Sender(crs, w, h)

    return 1


run_protocol([0, 1, 2, 3, 4, 5], [0, 3, 4, 7, 9, 73])