print("CAESAR CIPHER PROGRAM")

def caesar_cipher(t, s, a):
    r = ""
    for char in t:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shift_direction = s if a == 'e' else -s
            r += chr((ord(char) - start + shift_direction) % 26 + start)
        else:
            r += char
    return r

def main():
    A = input("Please select an option: 'E' for encryption or 'D' for decryption: ").lower()
    while A not in ['e', 'd']:
        print("Invalid selection. Please choose 'e' for encryption or 'd' for decryption.")
        A = input("Please select an option: 'e' for encryption or 'd' for decryption: ").lower()

    m = input(" Please Enter the message: ")
    s = int(input("Please Enter the shift value: "))

    r = caesar_cipher(m, s, A)
    action_word = "Encrypted" if A == 'e' else "Decrypted"
    print(f"\n{action_word} Message: {r}")

if __name__ == "__main__":
    main()
