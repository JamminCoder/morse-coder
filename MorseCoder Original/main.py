import Morse


mode = str(input("Decode or encode? [d/e] "))

if mode == "e":
    text = str(input("Enter text >> "))
    encoded_message = Morse.Encoder(text).run()
    print(f">> {encoded_message}")


if mode == "d":
    code = str(input("Enter code >> "))
    decoded_message = Morse.Decoder(code).run()
    print(f">> {decoded_message}")
