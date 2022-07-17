alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

string=(text)
list1 = list(string)

def encrypt(message=text,number=shift):
    result=""
    for letter in list1:
        pos = alphabet.index(letter)
        new=(pos+(shift+1))%25
        result = result + alphabet[new]
    print(f"The encoded messsage is {result}.")
   


def decrypt(result=text,number=shift):
    decrypt_answer=""
    for letter in result:
        pos = alphabet.index(letter)
        new=(pos-(shift+1))%25
        decrypt_answer= decrypt_answer+alphabet[new]
    print(f"The decoded message is {decrypt_answer}.")
        

if direction=='encode':
    encrypt()
elif direction=='decode':
    decrypt()
    
