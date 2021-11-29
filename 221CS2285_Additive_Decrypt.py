def decrypt(message,key):
    cipher=""
    for i in range(len(message)):
        ch=message[i]
        if(ch.islower()):
            cipher+=chr((ord(ch)+26-key-97)%26+97)
        else:
            cipher+=chr((ord(ch)+26-key-65)%26+65)
    return cipher
print("Enter the message to be encrypted")
message=input()
key=int(input("enter the key"))
print('Cipher message is')
print(decrypt(message,key))

