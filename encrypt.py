def encrypt(message, public_key):
    N = public_key[0]
    e = public_key[1]
    num = 1
    while message:
        num *= 10000000
        sub = message[0:2]
        num += (convert_to_num(sub) ** e) % N
        message = message[2:]
    return num

def convert_to_num(message):
    num = 0
    for c in message:
        num *= 1000
        num += ord(c)
    return num

