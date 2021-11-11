from generate_keys import generate_key
from encrypt import encrypt
from decrypt import decrypt

public_keys = {}

def main():
    while True:
        print("Please Enter a Command")
        x = input()
        args = []
        while " " in x:
            word = x[0:x.index(" ")]
            args.append(word)
            x = x[x.index(" ") + 1:]
        args.append(x)
        if args[0] == "gen-key":
            gen = generate_key()
            private_key = gen[0]
            public_key = gen[1]
            print(f"Your Private Key is {private_key}")
            print(f"Your Public Key is {public_key}")
            public_keys[args[1]] = public_key
        elif args[0] == "send":
            public_key = public_keys[args[1]]
            print(public_key)
            print(encrypt(args[2], public_key))
        elif args[0] == "decode":
            message = int(args[1])
            public_key = public_keys[args[2]]
            private_key = int(args[3])
            print(decrypt(message, public_key, private_key))



if __name__ == "__main__":
    main()