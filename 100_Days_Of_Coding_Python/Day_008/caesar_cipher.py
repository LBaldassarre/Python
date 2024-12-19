import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar (start_text, shift_amount, cipher_direction):
    end_text = ""
    
    end_shift = shift_amount % len(alphabet)
    if cipher_direction == "decode":
        end_shift *= -1
        
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char) + end_shift
            if position > len(alphabet) - 1:
                position = position - len(alphabet)
            end_text += alphabet[position]
            
    print(f"The {cipher_direction}d message is {end_text}")

print(art.logo)

# Check if the user want to keep encoding
keep_encoding = "yes"
while (keep_encoding == "yes"):
    
    # check for correct direction
    direction = ""
    while (direction not in ["encode", "decode"]):

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction not in ["encode", "decode"]:
            print("That's not a viable option, please choose again")
        else:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

        cesar(text, shift, direction)
    
    keep_encoding = input("Do you want to keep going (yes / no): \n").lower()

print("Good Bye.")