from generate_keys import generate_key
from encrypt import encrypt
from decrypt import decrypt

public_keys = {}
messages = {}

def main():
    read_public_keys()
    read_messages()

    print("Enter help for a list of commands")
    while True:
        print("Please Enter a Command:")
        command = input()
        if command == "keygen":
            keygen()
        elif command == "send":
            send()
        elif command == "decode":
            decode()
        elif command == "inbox":
            inbox()
        elif command == "help":
            print("keygen: generate a private public key pair\nsend: send an encrypted message\ndecode: decode an encrypted message\ninbox: view your messages")
        else:
            print("Invalid Command")
        print("\n")

def keygen():
    print("Enter a name:")
    user = input()
    gen = generate_key()
    private_key = gen[0]
    public_key = gen[1]
    print(f"Your Private Key is {private_key}")
    print(f"Your Public Key is {public_key}")
    public_keys[user] = public_key
    write_public_key(user, public_key)

def send():
    print("Enter the recipient's Username:")
    user = input()
    if not user in public_keys :
        print("Invalid User")
        return
    public_key = public_keys[user]
    print("Enter a message:")
    message = input()
    name = user + str(len(messages))
    encrypted = encrypt(message, public_key)
    messages[name] = encrypted
    write_message(name, encrypted)
    print(f"Message ID: {name}")

def decode():
        print("Enter your Username:")
        user = input()
        if not user in public_keys :
            print("Invalid User")
            return
        public_key = public_keys[user]
        print("Enter the Message ID")
        message = input()
        if not message in messages:
            print("Invalid Message ID")
            return
        message = messages[message]
        print("Enter your Private Key:")
        key = input()
        private_key = int(key)
        print(decrypt(message, public_key, private_key))   

def inbox():
    print("Enter your Username:")
    user = input()
    i = 0
    first = True
    print("Messages:")
    for i in range(len(messages)):
        name = user + str(i)
        if name in messages:
            print("\n")
            first = False
            print(name)

def write_public_key(user, key):
    key_file = open("public_keys.txt", "a")
    key_file.write(f'{user} {key[0]} {key[1]}\n')
    key_file.close()


def read_public_keys():
    key_file = open("public_keys.txt")
    keys = key_file.read()
    while keys:
        space = keys.index(" ")
        user = keys[0:space]
        keys = keys[space + 1:]
        space = keys.index(" ")
        public = int(keys[0:space])
        keys = keys[space + 1:]
        end = keys.index("\n")
        e = int(keys[0:end])
        keys = keys[end + 1:]
        public_keys[user] = (public, e)

def write_message(name, message):
    message_file = open("messages.txt", "a")
    message_file.write(f'{name} {message}\n')
    message_file.close()

def read_messages():
    message_file = open("messages.txt")
    contents = message_file.read()
    while contents:
        space = contents.index(" ")
        name = contents[0:space]
        contents = contents[space + 1:]
        end = contents.index("\n")
        message = contents[0:end]
        contents = contents[end + 1:]
        messages[name] = message


if __name__ == "__main__":
    main()