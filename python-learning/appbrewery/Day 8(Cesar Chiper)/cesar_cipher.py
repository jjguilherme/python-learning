alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        if shifted_position > len(alphabet) - 1:
            shifted_position = shifted_position - len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        if shifted_position < 0:
            shifted_position += len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {cipher_text}")

continuar = "yes"

while continuar.lower() == 'yes':
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Fuck you!")
    continuar = input("Do you want to continue? (yes or no): ")
print("Finishing program!")