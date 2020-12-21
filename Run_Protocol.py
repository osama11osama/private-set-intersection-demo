# import Crypto
# from Crypto.PublicKey import RSA
# from Crypto import Random
from Receiver import Receiver
from Sender import Sender
from utils import Random_n_Prime, Random_generators, generat_crs


def run_protocol(Sender_set, Receiver_set):
    # # what is the max size of the U ? we did not understand the idea of PRF to use it fo Large Universe
    U = max(Sender_set + Receiver_set)
    print(U)

    # Where we have to use the RSA param?
    # chose P and Q then Compute N
    P = 3
    Q = 11
    N = P * Q

    """
    # should we generate l prime? or there is a better Idea?
    primes = Random_n_Prime(1, U)

    # Is the generator have to be a generator for random i < N
    g = Random_generators(N)

    primes_string = ""
    for i in range(U):
        primes_string += str(primes[i]) + " "

    crs = str(N) + " " + str(g) + " " + primes_string
    """
    crs = generat_crs(N, U)
    print(crs)

    receiver = Receiver(crs, Receiver_set)
    res = receiver.hashReceiver()
    r = res[1]
    h = res[0]
    sender = Sender(crs, Sender_set, h)
    result = sender.computeSender()
    # seed = result[0]
    # f = result[1]
    # R = result[2]
    # i = 0
    # intersection = receiver.checkIntersection(seed, f, r, i, R)

    return 1


run_protocol([7], [0, 3, 4, 7, 9, 10])
