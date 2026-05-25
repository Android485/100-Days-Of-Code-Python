from caeser_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decision = 'yes'
while decision == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caeser(original_text, shift_amount, direction):
        decrypted_text = ""
        if direction == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter not in alphabet:
                decrypted_text += letter
                continue
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
            
            
        print(f"Here is the decrypted result: {decrypted_text}")


    caeser(original_text=text, shift_amount=shift, direction=direction)
    decision = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if decision == 'no':
        print("Goodbye!")