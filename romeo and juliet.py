import sys


def main():
    if sys.argv[1] == "encrypt":
        message = input("Please enter a message you want to encrypt:")
        encrypt_message = ""
        for word in message:
            for letter in word:
                if letter == "h":
                    letter = "19"
                    encrypt_message += letter + ","
                elif letter == "t":
                    letter = "91"
                    encrypt_message += letter + ","
                elif letter == "u":
                    letter = "92"
                    encrypt_message += letter + ","

                elif letter == "v":
                    letter = "93"
                    encrypt_message += letter + ","

                elif letter == "w":
                    letter = "94"
                    encrypt_message += letter + ","

                elif letter == "x":
                    letter = "95"
                    encrypt_message += letter + ","

                elif letter == "y":
                    letter = "96"
                    encrypt_message += letter + ","

                elif letter == "z":
                    letter = "97"
                    encrypt_message += letter + ","

                elif letter == " ":
                    letter = "98"
                    encrypt_message += letter + ","

                elif letter == ",":
                    letter = "99"
                    encrypt_message += letter + ","

                elif letter == "k":
                    letter = "32"
                    encrypt_message += letter + ","

                elif letter == "l":
                    letter = "33"
                    encrypt_message += letter + ","

                elif letter == "m":
                    letter = "34"
                    encrypt_message += letter + ","

                elif letter == "n":
                    letter = "35"
                    encrypt_message += letter + ","

                elif letter == "o":
                    letter = "36"
                    encrypt_message += letter + ","

                elif letter == "p":
                    letter = "37"
                    encrypt_message += letter + ","

                elif letter == "q":
                    letter = "38"
                    encrypt_message += letter + ","

                elif letter == "r":
                    letter = "39"
                    encrypt_message += letter + ","

                elif letter == "s":
                    letter = "90"
                    encrypt_message += letter + ","

                elif letter == "b":
                    letter = "13"
                    encrypt_message += letter + ","

                elif letter == "c":
                    letter = "14"
                    encrypt_message += letter + ","

                elif letter == "d":
                    letter = "15"
                    encrypt_message += letter + ","

                elif letter == "e":
                    letter = "16"
                    encrypt_message += letter + ","

                elif letter == "f":
                    letter = "17"
                    encrypt_message += letter + ","

                elif letter == "g":
                    letter = "18"
                    encrypt_message += letter + ","

                elif letter == "i":
                    letter = "30"
                    encrypt_message += letter + ","

                elif letter == "j":
                    letter = "31"
                    encrypt_message += letter + ","

                elif letter == "S":
                    letter = "64"
                    encrypt_message += letter + ","

                elif letter == "T":
                    letter = "65"
                    encrypt_message += letter + ","

                elif letter == "U":
                    letter = "66"
                    encrypt_message += letter + ","

                elif letter == "V":
                    letter = "67"
                    encrypt_message += letter + ","

                elif letter == "W":
                    letter = "68"
                    encrypt_message += letter + ","

                elif letter == "X":
                    letter = "69"
                    encrypt_message += letter + ","

                elif letter == "Y":
                    letter = "10"
                    encrypt_message += letter + ","

                elif letter == "Z":
                    letter = "11"
                    encrypt_message += letter + ","

                elif letter == "a":
                    letter = "12"
                    encrypt_message += letter + ","

                elif letter == "J":
                    letter = "45"
                    encrypt_message += letter + ","

                elif letter == "K":
                    letter = "46"
                    encrypt_message += letter + ","

                elif letter == "L":
                    letter = "47"
                    encrypt_message += letter + ","

                elif letter == "M":
                    letter = "48"
                    encrypt_message += letter + ","

                elif letter == "N":
                    letter = "49"
                    encrypt_message += letter + ","

                elif letter == "O":
                    letter = "60"
                    encrypt_message += letter + ","

                elif letter == "P":
                    letter = "61"
                    encrypt_message += letter + ","

                elif letter == "Q":
                    letter = "62"
                    encrypt_message += letter + ","

                elif letter == "R":
                    letter = "63"
                    encrypt_message += letter + ","

                elif letter == "A":
                    letter = "56"
                    encrypt_message += letter + ","

                elif letter == "B":
                    letter = "57"
                    encrypt_message += letter + ","

                elif letter == "C":
                    letter = "58"
                    encrypt_message += letter + ","

                elif letter == "D":
                    letter = "59"
                    encrypt_message += letter + ","

                elif letter == "E":
                    letter = "40"
                    encrypt_message += letter + ","

                elif letter == "F":
                    letter = "41"
                    encrypt_message += letter + ","

                elif letter == "G":
                    letter = "42"
                    encrypt_message += letter + ","

                elif letter == "H":
                    letter = "43"
                    encrypt_message += letter + ","

                elif letter == "I":
                    letter = "44"
                    encrypt_message += letter + ","

                elif letter == ".":
                    letter = "100"
                    encrypt_message += letter + ","

                elif letter == ";":
                    letter = "101"
                    encrypt_message += letter + ","

                elif letter == "‘":
                    letter = "102"
                    encrypt_message += letter + ","

                elif letter == "?":
                    letter = "103"
                    encrypt_message += letter + ","

                elif letter == "!":
                    letter = "104"
                    encrypt_message += letter + ","

                elif letter == ":":
                    letter = "105"
                    encrypt_message += letter + ","

        encrypt_message = encrypt_message[:-1]
        with open('encrypted_msg.txt', 'w') as encrypted_file:
            encrypted_file.write(encrypt_message)


    # decrypt
    elif sys.argv[1] == "decrypt":
        with open('encrypted_msg.txt', 'r') as encrypted_file:
            decrypt_message = ""
            encrypt_code = encrypted_file.read()
            encrypt_code_list = encrypt_code.split(",")
            for item in encrypt_code_list:
                if item == "19":
                    decrypt_message += "h"

                elif item == "91":
                    decrypt_message += "t"

                elif item == "92":
                    decrypt_message += "u"

                elif item == "93":
                    decrypt_message += "v"

                elif item == "94":
                    decrypt_message += "w"

                elif item == "95":
                    decrypt_message += "x"

                elif item == "96":
                    decrypt_message += "y"

                elif item == "97":
                    decrypt_message += "z"

                elif item == "98":
                    decrypt_message += " "

                elif item == "99":
                    decrypt_message += ","

                elif item == "32":
                    decrypt_message += "k"

                elif item == "33":
                    decrypt_message += "l"

                elif item == "34":
                    decrypt_message += "m"

                elif item == "35":
                    decrypt_message += "n"

                elif item == "36":
                    decrypt_message += "o"

                elif item == "37":
                    decrypt_message += "p"

                elif item == "38":
                    decrypt_message += "q"

                elif item == "39":
                    decrypt_message += "r"

                elif item == "90":
                    decrypt_message += "s"

                elif item == "13":
                    decrypt_message += "b"

                elif item == "14":
                    decrypt_message += "c"

                elif item == "15":
                    decrypt_message += "d"

                elif item == "16":
                    decrypt_message += "e"

                elif item == "17":
                    decrypt_message += "f"

                elif item == "18":
                    decrypt_message += "g"

                elif item == "30":
                    decrypt_message += "i"

                elif item == "31":
                    decrypt_message += "j"

                elif item == "64":
                    decrypt_message += "S"

                elif item == "65":
                    decrypt_message += "T"

                elif item == "66":
                    decrypt_message += "U"

                elif item == "67":
                    decrypt_message += "V"

                elif item == "68":
                    decrypt_message += "W"

                elif item == "69":
                    decrypt_message += "X"

                elif item == "10":
                    decrypt_message += "Y"

                elif item == "11":
                    decrypt_message += "Z"

                elif item == "12":
                    decrypt_message += "a"

                elif item == "45":
                    decrypt_message += "J"

                elif item == "46":
                    decrypt_message += "K"

                elif item == "47":
                    decrypt_message += "L"

                elif item == "48":
                    decrypt_message += "M"

                elif item == "49":
                    decrypt_message += "N"

                elif item == "60":
                    decrypt_message += "O"

                elif item == "61":
                    decrypt_message += "P"

                elif item == "62":
                    decrypt_message += "Q"

                elif item == "63":
                    decrypt_message += "R"

                elif item == "56":
                    decrypt_message += "A"

                elif item == "57":
                    decrypt_message += "B"

                elif item == "58":
                    decrypt_message += "C"

                elif item == "59":
                    decrypt_message += "D"

                elif item == "40":
                    decrypt_message += "E"

                elif item == "41":
                    decrypt_message += "F"

                elif item == "42":
                    decrypt_message += "G"

                elif item == "43":
                    decrypt_message += "H"

                elif item == "44":
                    decrypt_message += "I"

                elif item == "100":
                    decrypt_message += "."

                elif item == "101":
                    decrypt_message += ";"

                elif item == "102":
                    decrypt_message += "‘"

                elif item == "103":
                    decrypt_message += "?"

                elif item == "104":
                    decrypt_message += "!"

                elif item == "105":
                    decrypt_message += ":"

            print(decrypt_message)


if __name__ == '__main__':
    main()