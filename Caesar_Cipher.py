def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return "shift muss be an integer"
    if shift < 1 or shift > 24:
        return "Shift must be an integer between 1 and 25."
    if not encrypt:
        shift = -shift
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, False)


print("""
             CAESAR CYPHER
    ===================================

            1. Encrypt Text 
            2. Decrypt Text
                                            by Ezekiel Roll
""")
choice = input("choose an Option : ")
if choice == "1":
    file_to_encrypt = input("Enter file to encrypt : ")
    number_of_shift_to_encrypt = int(input("Enter number of shift to Encrypt"))
    encrypted_text = encrypt(file_to_encrypt, number_of_shift_to_encrypt)
    print("Encrypted_Message: " + encrypted_text)

elif choice == "2":
    encrypted_text = input("Enter Text to Decrypt : ")
    number_of_shift = input("Enter the number of shift : ")
    decrypted_text = decrypt(encrypted_text, int(number_of_shift))
    print("Decrypted Message : " + decrypted_text)

else:
    print("Invalid Option")

