class Morse():
    def __init__(self):
        self.table = {
          "" : "",
          ".-" : "a",
          "-..." : "b",
          "-.-." : "c",
          "-.." : "d",
          "." : "e",
          "..-." : "f",
          "--." : "g",
          "...." : "h",
          ".." : "i",
          ".---" : "j",
          "-.-" : "k",
          ".-.." : "l",
          "--" : "m",
          "-." : "n",
          "---" : "o",
          ".--." : "p",
          "--.-" : "q",
          ".-." : "r",
          "..." : "s",
          "-" : "t",
          "..-" : "u",
          "...-" : "v",
          ".--" : "w",
          "-..-" : "x",
          "-.--" : "y",
          "--.." : "z",
          "/" : " ",
          ".----" : "1",
          "..---" : "2",
          "...--" : "3",
          "....-" : "4",
          "....." : "5",
          "-...." : "6",
          "--..." : "7",
          "---.." : "8",
          "----." : "9",
          "-----" : "0",
          ".-.-.-" : ".",
          "--..--" : ",",
          "..--.." : "?",
          ".----." : "'",
          "-.-.--" : "!",
          "-..-." : "/",
          "-.--." : "(",
          "-.--.-" : ")",
          ".-..." : "&",
          "---..." : ":",
          "-.-.-." : ";",
          ".-.-." : "+",
          "-....-" : "-",
          "-...-" : "=",
          "-....-" : "-",
          "..--.-" : "_",
          ".-..-." : "\"",
          ".-..-." : "\"",
          "...-..-" : "$",
          ".--.-." : "@",
          ".-.-" : "ä",
          ".--.-" : "á",
          "-.-.." : "ç",
          "----" : "ch",
          ".-..-" : "è",
          "..-.." : "é",
          "--.--" : "ñ",
          "---." : "ö",
          "..--" : "ü"}

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        phrase_begining = True
        encrypted_message = encrypted_message.split(" ") 
        for morse in encrypted_message:
            if morse not in self.table:
                decrypted_message += morse
                continue

            if phrase_begining == True and morse != "/":
                decrypted_message += self.table[morse].upper()
                phrase_begining = False
            else:
                decrypted_message += self.table[morse]
            if morse == ".-.-.-" or morse == "-.-.--" or morse == "..--..": 
                phrase_begining = True
        return decrypted_message
        
    def encrypt(self, unencrypted_message):
        unencrypted_message = unencrypted_message.lower() 
        number_letters = len(unencrypted_message)
        encrypted_message = ""
        for position_letter in range(number_letters):
            for morse in self.table: 
                if self.table[morse] == unencrypted_message[position_letter]: 
                    encrypted_message += morse

                    if position_letter != number_letters - 1:
                        encrypted_message += " "

                    break 

        return encrypted_message