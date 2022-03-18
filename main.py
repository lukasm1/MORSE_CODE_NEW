special_symbols = [",", ".", "?", "!"]
morse_code_dict = {
    "A": "·−",
    "B": "−···",
    "C": "−·−·",
    "D": "−··",
    "E": "·",
    "F": "··−·",
    "G": "−−·",
    "H": "····",
    "I": "··",
    "J": "·−−−",
    "K": "−·−",
    "L": "·−··",
    "M": "−−",
    "N": "−·",
    "O": "−−−",
    "P": "·−−·",
    "Q": "−−·−",
    "R": "·−·",
    "S": "···",
    "T": "−",
    "U": "··−",
    "V": "···−",
    "W": "·−−",
    "X": "−··−",
    "Y": "−·−−",
    "Z": "−−··",
    "0": "−−−−−",
    "1": "·−−−−",
    "2": "··−−−",
    "3": "···−−",
    "4": "····−",
    "5": "·····",
    "6": "−····",
    "7": "−−···",
    "8": "−−−··",
    "9": "−−−−·",
}

game = True

print("\nWelcome to the Morse-Code-Converter.")

while game:

    print(
        "\nIf you want to convert text to Morse, please type ENCRYPT. If you want to convert Morse to text, please type DECRYPT.")
    print("To exit the converter, please type EXIT.")
    wish = input("What do you wish: ").upper()

    if wish == "ENCRYPT":

        message_to_convert = input("\nEnter the code you wish to convert to Morse: ").upper()
        encrypted_message = ""

        for letter in message_to_convert:

            if letter in morse_code_dict:
                encrypted_message += f"{morse_code_dict[letter]} "
            elif letter == " ":
                encrypted_message += letter
            else:
                encrypted_message += f"{letter} "

        print(f"Message in Morse: {encrypted_message}")


    elif wish == "DECRYPT":

        encrypted_message = input("\nEnter the Morse you wish to convert to text: ").upper()

        encrypted_message_list = encrypted_message.split(" ")
        decrypted_message = ""

        for item in encrypted_message_list:

            if item in special_symbols:
                decrypted_message += item

            elif item == "":
                decrypted_message += " "

            else:

                for key in morse_code_dict:

                    if item == morse_code_dict[key]:
                        decrypted_message += key

        print(f"Decrypted message: {decrypted_message}")

    if wish == "EXIT":
        game = False