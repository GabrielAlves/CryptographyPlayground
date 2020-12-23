class Caesar:
    def __init__(self):
        self.displacement = 13

    def encrypt(self, unencrypted_message):
        encrypted_message = ""

        for letter in unencrypted_message:
            ascii_number = ord(letter)
            ascii_number += self.displacement
            encrypted_char = chr(ascii_number)
            encrypted_message += encrypted_char

        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""

        for letter in encrypted_message:
            ascii_number = ord(letter)
            ascii_number -= self.displacement
            decrypted_char = chr(ascii_number)
            decrypted_message += decrypted_char
        
        return decrypted_message