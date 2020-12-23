class I18NCryptographyPlayground:
    def __init__(self, language):
        self.set_language(language)


    def set_language(self, language):
        if language == "pt":
            self.set_portuguese_language()

        elif language == "en":
            self.set_english_language()

        else:
            raise NotImplementedError


    def set_english_language(self):
        self.window_title = "Cryptography Playground"

        self.coding_tab_text = "Code"
        self.decoding_tab_text = "Decode"

        self.menu_file_label = "File"
        self.menu_file_new_label = "New"
        self.menu_file_exit_label = "Exit"

        self.menu_help_label = "Help"
        self.menu_help_about_label = "About"

        self.coding_section_labelframe = "Encryption Section"
        self.decoding_section_labelframe = "Decryption Section"

        self.label_for_message_to_be_encrypted = "Write below the message you want to encrypt"

        self.label_encrypted_message = "Your encrypted message will be shown below"

        self.cryptography_options = "Cryptography options"

        self.caesar_cryptography_button_text = "ASCII-Caesar"
        self.morse_cryptography_button_text = "Morse"

        self.label_for_message_to_be_decrypted = "Write below the message you want to decrypt"

        self.label_decrypted_message = "Your decrypted message will be shown below"


    def set_portuguese_language(self):
        self.window_title = "Parque da Criptografia"

        self.coding_tab_text = "Codifique"
        self.decoding_tab_text = "Decodifique"

        self.coding_section_labelframe = "Seção de Criptografia"
        self.decoding_section_labelframe = "Seção de Descriptografia"

        self.menu_file_label = "Arquivo"
        self.menu_file_new_label = "Novo"
        self.menu_file_exit_label = "Fechar"

        self.menu_help_label = "Ajuda"
        self.menu_help_about_label = "Sobre"

        self.label_for_message_to_be_encrypted = "Escreva abaixo a mensagem que você quer criptografar"

        self.label_encrypted_message = "Sua mensagem criptografada será mostrada abaixo"

        self.cryptography_options = "Opções de criptografia"

        self.caesar_cryptography_button_text = "ASCII-Caesar"
        self.morse_cryptography_button_text = "Morse"

        self.label_for_message_to_be_decrypted = "Escreva abaixo a mensagem que você deseja descriptografar"

        self.label_decrypted_message = "Sua mensagem descriptografada será mostrada abaixo"