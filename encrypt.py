def encrypt(message, public_key):
    N = public_key[0]
    e = public_key[1]
    to_num = convert_to_num(message)
    return (to_num ** e) % N

def convert_to_num(message):
    num = 0
    for c in message:
        num *= 1000
        num += ord(c)
    return num
