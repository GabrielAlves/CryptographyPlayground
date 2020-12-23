class I18NAboutProjectView:
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
        self.about_project_title = "About"
        self.about_project_labelframe_text = "About the project"
        self.about_project_attachments_labelframe_text = "Attachments"
        self.about_project_license_button_text = "License"
        self.about_project_readme_button_text = "Readme"
        self.about_project_github_button_text = "Github"


    def set_portuguese_language(self):
        self.about_project_title = "Sobre"
        self.about_project_labelframe_text = "Sobre o projeto"
        self.about_project_attachments_labelframe_text = "Anexos"
        self.about_project_license_button_text = "Licença"
        self.about_project_readme_button_text = "Leia-me"
        self.about_project_github_button_text = "Github"