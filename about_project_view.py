import tkinter as tk
from tkinter import ttk

import webbrowser
import os

from gui_settings import GUISettings
from i18n.i18n_about_project_view import I18NAboutProjectView
from i18n.i18n_cryptography_playground import I18NCryptographyPlayground

class AboutProjectView:
    def __init__(self):
        self.create_widgets()

    def create_widgets(self):
        self.create_window()
        self.create_title_about_project()
        self.add_padding_to_widgets_in_window()
        self.create_attachments_labelframe()
        self.create_license_button()
        self.create_readme_button()
        self.create_github_button()
        self.add_padding_to_buttons()


    def create_window(self):
        self.about_window = tk.Toplevel()
        self.configure_window()


    def define_gui_language(self):
        self.i18n_about_project_view = I18NAboutProjectView("en")
        self.i18n_cryptography_playground = I18NCryptographyPlayground("en")


    def define_gui_settings(self):
        self.gui_settings = GUISettings()


    def configure_window(self):
        self.define_gui_language()
        self.define_gui_settings()

        self.about_window.title(self.i18n_about_project_view.about_project_title)
        self.about_window.resizable(False, False)


    def create_title_about_project(self):
        self.title_about = ttk.Label(self.about_window, text = self.i18n_cryptography_playground.window_title.upper(), font = (self.gui_settings.font_family, self.gui_settings.font_size + 6))
        self.title_about.grid(columnspan = 3)


    def create_attachments_labelframe(self):
        self.attachments_labelframe = ttk.LabelFrame(self.about_window, text = self.i18n_about_project_view.about_project_attachments_labelframe_text)
        self.attachments_labelframe.grid()


    def add_padding_to_widgets_in_window(self):
        for child in self.about_window.winfo_children():
            child.grid_configure(padx = self.gui_settings.padding_width, pady = self.gui_settings.padding_height)


    def create_license_button(self):
        self.license_button = ttk.Button(self.attachments_labelframe, text = self.i18n_about_project_view.about_project_license_button_text, command = self.show_license)
        self.license_button.grid(column = 0, row = 0, sticky = tk.W)


    def create_readme_button(self):
        self.readme_button = ttk.Button(self.attachments_labelframe, text = self.i18n_about_project_view.about_project_readme_button_text, command = self.show_readme)
        self.readme_button.grid(column = 1, row = 0, sticky = tk.W)


    def create_github_button(self):
        self.github_button = ttk.Button(self.attachments_labelframe, text = self.i18n_about_project_view.about_project_github_button_text, command = self.show_github)
        self.github_button.grid(column = 2, row = 0, sticky = tk.W)


    def add_padding_to_buttons(self):
        for button in self.attachments_labelframe.winfo_children():
            button.grid_configure(padx = self.gui_settings.padding_width, pady = self.gui_settings.padding_height)


    def show_license(self):
        os.system("notepad.exe license.md")


    def show_readme(self):
        os.system("notepad.exe readme.md")


    def show_github(self):
        github_url = "https://github.com/GabrielAlves"

        webbrowser.open_new_tab(github_url)