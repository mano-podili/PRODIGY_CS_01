def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result
def caesar_decrypt(text, shift):
    decrypted_message = ""
    # Decrypt each character in the message
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message
def main():
    while True:
        print("------------------------------------------------")
        print("Options:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        mode = input("Choose an option: ").lower()
        if mode == '1':
            message = input("Enter the message: \n")
            shift = None
            while shift is None:
                try:
                    shift = int(input("Enter the shift value: \n"))
                except ValueError:
                    print("Invalid shift value. Please enter an integer.")
            encrypted_message = caesar_encrypt(message, shift)
            print(f"------Encrypted message: {encrypted_message}------")
        elif mode == '2':
            message = input("Enter the message: \n")
            shift = None
            while shift is None:
                try:
                    shift = int(input("Enter the shift value: \n"))
                except ValueError:
                    print("Invalid shift value. Please enter an integer.")
            decrypted_message = caesar_decrypt(message, shift)
            print(f"------Decrypted message: {decrypted_message}------")
        elif mode == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 for encrypt, 2 for decrypt, or 3 to quit.")
if __name__ == "__main__":
    main()
