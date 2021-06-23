#!/usr/bin/python3

def read_morse_file(path):
    with open(path, "r") as f:
        return f.read().split("\n")


class Morse:
    def __init__(self):
        self.morse_code_file = "morse.txt"
        self.plain_charset = []
        self.morse_file_content = read_morse_file(self.morse_code_file)  # Morse code alphabet
        self.morse_chars = []
        self.parse_morse_chars()

    def parse_morse_chars(self):
        for line in self.morse_file_content:
            line = line.split(" ")
            morse_char = line[0]
            plain_char = line[1]
            self.plain_charset.append(plain_char.lower())
            self.morse_chars.append(morse_char)


class Decoder(Morse):
    def __init__(self, code_str):
        super().__init__()  # Inherits __init__ method from Morse class
        code_str = code_str.lower()
        self.words = code_str.split("  ")  # Each morse-code word is separated by 2 spaces

    def run(self):
        decoded_message = ""
        for word in self.words:
            decoded_word = ""
            morse_chars = word.split(" ")
            for morse_char in morse_chars:
                if morse_char not in self.morse_chars:
                    print("That's not valid morse code!")
                    exit()

                morse_char_ind = self.morse_chars.index(morse_char)
                char = self.plain_charset[morse_char_ind]
                decoded_word += char
            decoded_word += " "
            decoded_message += decoded_word
        return decoded_message[:-1] + "."  # The [:-1] + "." bit just adds a period at the end of the message


class Encoder(Morse):
    def __init__(self, plain_str):
        super().__init__()  # Inherits __init__ method from Morse class
        plain_str = plain_str.lower()
        self.words = plain_str.split(" ")

    def run(self):
        encoded_message = ""
        for word in self.words:
            encoded_word = ""
            for char in word:
                if char not in self.plain_charset:
                    print("Enter letters only please!")
                    exit()
                char_ind = self.plain_charset.index(char)
                encoded_word += self.morse_chars[char_ind] + " "
            encoded_message += encoded_word + " "
        return encoded_message
