import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, n-1, n)
        if x != 1:
            return False
    return True

def generate_prime_number(n=1024):
    prime = False
    while not prime:
        p = random.randint(2**(n-1), 2**n-1)
        if is_prime(p):
            return p

def generate_key_pair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    gcd_val = gcd(phi, e)
    while gcd_val != 1:
        e = random.randint(2, phi-1)
        gcd_val = gcd(phi, e)
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    c = pow(message, e, n)
    return c

def decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m


# 키 쌍 생성
public_key, private_key = generate_key_pair()

# 메시지 선택
message = 12345

# 암호화
ciphertext = encrypt(message, public_key)

# 복호화
decrypted_message = decrypt(ciphertext, private_key)

# 결과 출력
print("message:",message)
print("encrypted:",ciphertext)
print("decrypted:",decrypted_message)