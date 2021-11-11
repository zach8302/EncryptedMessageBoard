def decrypt(encrypted, public_key, private_key):
    N = public_key[0]
    s = ""
    while encrypted > 0:
        part = encrypted % 10000000
        part %= N
        num = (part ** private_key) % N
        s = to_str(num) + s
        encrypted //= 10000000
    return s

def to_str(num):
    s = ""
    while num > 10:
        c = chr(num % 1000)
        s = c + s
        num //= 1000
    return s
