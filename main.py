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
        print(args)
        if args[0] == "gen-key":
            gen = generate_key()
            private_key = gen[0]
            public_key = gen[1]
            public_keys[args[1]] = generate_key()




if __name__ == "__main__":
    main()