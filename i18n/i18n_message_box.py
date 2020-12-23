class I18NMessageBox:
    def __init__(self, language):
        self.set_language(language)

    
    def set_language(self, language):
        if language == "en":
            self.set_english_language()

        elif language == "pt":
            self.set_portuguese_language()

        else:
            raise NotImplementedError

    
    def set_english_language(self):
        self.nothing_written_warning_title = "Nothing was written!"
        self.nothing_written_warning_content = "Please write something!"

        self.process_error_title = "Error during process"
        self.process_error_content = "Something went wrong. Please, report it on Github"


    def set_portuguese_language(self):
        self.nothing_written_warning_title = "Nada foi escrito!"
        self.nothing_written_warning_content = "Por favor, escreva algo!"

        self.process_error_title = "Erro durante processo"
        self.process_error_content = "Algo deu errado. Por favor, reporte no Github"