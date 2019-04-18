import random
import math


msg = "Teste"
msg_cifrada = ""
msg_decifrada = ""


def criptografia():
    msg = input('Insira o texto para criptografar: ')
    print("Gerando Chaves")
    # p = generatepq()
    # q = generatepq()
    # p = generateLargePrime(512)
    # q = generateLargePrime(512)
    p = 3
    q = 5
    print("p = ", p)
    print("q = ", q)
    generateKeys(p, q)


def generatepq():
    n = random.getrandbits(31)
    while not primo(n):
        n = generatepq()
    return n


def primo(n):
    # https://www.youtube.com/watch?v=q4o9AWwdvl4
    raiz = int(math.sqrt(n))
    for d in range(2, raiz + 1):
        if n % d == 0:
            return False
    return True


def generateKeys(p,q):
    n = p*q
    print('n: ', n)
    phi= (p-1)*(q-1)
    print('phi: ', phi)
    #MDC precisa ser 1
    while True:
        # print("whili")
        # e = random.randrange(2 ** (512 - 1), 2 ** (512))
        e = 7
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print("e: ",e)


    # d = generateD(e, phi)
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)


    print("PHi ", phi, " n ", n, " e",e, " d:",d)
    # N e E chave publica


def generateE(phi):
    e = random.randrange(1, phi)
    m = mdc(e, phi)
    while m !=1 and e >1:
        e = random.randrange(1, phi)
        m = mdc(e, phi)
    return e


def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generateD(e, phi):
    d = random.getrandbits(12)
    temp = (e * d) % phi
    while temp !=1:
        d = random.getrandbits(12)
        temp = (e * d) % phi
    return d


def rabinMiller(num):
    # Returns True if num is a prime number.


    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1


    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().


    if (num < 2):
        return False # 0, 1, and negative numbers are not prime


    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


    if num in lowPrimes:
        return True


    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False


    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabinMiller(num)


def generateLargePrime(keysize=1024):
    # Return a random prime number of keysize bits in size.
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b




def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m


    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


criptografia()
