#!/usr/bin/python3


import Morse

modes = "d decode e encode"
mode = input(">> Do you want to decode or encode [d/e]? >> ").lower()
while mode not in modes:
    if mode == "exit":
        exit()
    mode = input(">> Use 'd or 'decode' for decode mode.\
                \n>> Or use 'e' or 'encode' for encode mode,\
                \n>> or just type exit>> ").lower()

if mode == "d" or mode == "decode":
    code = input("Enter Morse code >> ")
    decoded_message = Morse.Decoder(code).run()
    print(f">> {decoded_message}")

if mode == "e" or mode == "encode":
    text = input("Enter Text >> ")
    encoded_message = Morse.Encoder(text).run()
    print(f">> {encoded_message}")
