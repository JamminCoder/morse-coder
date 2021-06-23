
def read_morse_file(path):
    with open(path, "r") as f:
        return f.read().split("\n")


class Morse:
    def __init__(self):
        self.morse_file = "morse.txt"
        self.morse_file_content = read_morse_file(self.morse_file)
        self.charset = []
        self.morse_chars = []
        self.parse_morse_file()

    def parse_morse_file(self):
        for line in self.morse_file_content:
            line = line.split(" ")
            morse_char = line[0]
            plain_char = line[1].lower()
            self.charset.append(plain_char)
            self.morse_chars.append(morse_char)


class Encoder(Morse):
    def __init__(self, plain_text):
        super().__init__()
        self.words = plain_text.lower().split(" ")

    def run(self):
        encoded_message = ""
        for word in self.words:
            encoded_word = ""
            for char in word:
                char_ind = self.charset.index(char)
                morse_char = self.morse_chars[char_ind]
                encoded_word += morse_char + " "
            encoded_message += encoded_word + " "
        return encoded_message


class Decoder(Morse):
    def __init__(self, morse_code):
        super().__init__()
        self.words = morse_code.lower().split("  ")

    def run(self):
        decoded_message = ""
        for word in self.words:
            decoded_word = ""
            morse_chars = word.split(" ")
            for morse_char in morse_chars:
                morse_char_ind = self.morse_chars.index(morse_char)
                plain_text_char = self.charset[morse_char_ind]
                decoded_word += plain_text_char
            decoded_message += decoded_word + " "
        return decoded_message[:-1] + "."
