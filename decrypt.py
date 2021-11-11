from encrypt import encrypt


def decrypt(encrypted, public_key, private_key):
    N = public_key[0]
    encrypted %= N
    return (encrypted ** private_key) % N
