from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift: int = int(input("Type the shift number:\n"))


if direction=='encode':
    encoded_message=''
    for i in text:
        if i in alphabet:
            text_index = alphabet.index(i)+shift
            text_index%=len(alphabet)
            encoded_message+=alphabet[text_index]
            

    print(encoded_message)