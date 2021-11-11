def encrypt(message, public_key):
    N = public_key[0]
    e = public_key[1]
    num = 0
    while message:
        num *= 10000000
        sub = message[0:2]
        num += (convert_to_num(sub) ** e) % N
        message = message[2:]
    return num

def convert_to_num(message):
    num = 1
    for c in message:
        num *= 1000
        num += ord(c)
    return num
