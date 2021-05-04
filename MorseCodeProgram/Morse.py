#!/usr/bin/python3

def read(path):
    with open(path, "r") as f:
        return f.read()


class Morse:
    def __init__(self):
        # Characters to decode to. NOTE: Characters and number must be in alphebetical order or
        # Decoder will not work. I.E "abcdef...1234567890"
        self.morse_code_file = "morse.txt"
        self.charset = "abcdefghijklmnopqrstuvwxyz1234567890"
        self.morse_code = read(self.morse_code_file)  # Morse code alphabet
        self.morse_chars = []
        self.parse_morse_chars()

    def parse_morse_chars(self):
        self.morse_code = self.morse_code.split("\n")
        for line in self.morse_code:
            morse_char = line.split(" ")[:1][0]
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
                morse_char_ind = self.morse_chars.index(morse_char)
                char = self.charset[morse_char_ind]
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
                char_ind = self.charset.index(char)
                encoded_word += self.morse_chars[char_ind] + " "
            encoded_message += encoded_word + " "
        return encoded_message
