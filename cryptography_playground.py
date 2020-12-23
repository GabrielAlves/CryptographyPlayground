import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as msg
from tkinter import Menu

from i18n.i18n_cryptography_playground import I18NCryptographyPlayground
from i18n.i18n_message_box import I18NMessageBox
from gui_settings import GUISettings
from cryptography_algorithms.morse import Morse
from cryptography_algorithms.caesar import Caesar

from about_project_view import AboutProjectView


class CryptographyPlayground:
    def __init__(self):
        self.create_widgets()


    def create_widgets(self):
        self.create_window()
        self.create_menu()
        self.create_tabs()
        self.create_widgets_of_coding_tab()
        self.create_widgets_of_decoding_tab()


    def define_gui_settings(self):
        self.gui_settings = GUISettings()


    def create_window(self):
        self.window = tk.Tk()
        self.configure_window()    

    
    def define_gui_language(self):
        self.i18n_cryptography_playground = I18NCryptographyPlayground("en")
        self.i18n_message_box = I18NMessageBox("en")


    def configure_window(self):
        self.define_gui_settings()
        self.define_gui_language()
        self.window.title(self.i18n_cryptography_playground.window_title)
        self.window.iconbitmap(self.window, "images/icons/lock_icon.ico")
        self.window.resizable(False, False)


    def create_menu(self):
        self.create_menu_bar()
        self.create_file_menu_item()
        self.create_help_menu_item()


    def create_menu_bar(self):
        self.menu_bar = Menu(self.window)
        self.window.configure(menu = self.menu_bar)


    def create_file_menu_item(self):
        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = self.i18n_cryptography_playground.menu_file_new_label, command = self.open_new_window)
        self.file_menu.add_command(label = self.i18n_cryptography_playground.menu_file_exit_label, command = self.close_window)
        self.menu_bar.add_cascade(label = self.i18n_cryptography_playground.menu_file_label, menu = self.file_menu)


    def create_help_menu_item(self):
        self.help_menu = Menu(self.menu_bar, tearoff = 0)
        self.help_menu.add_command(label = self.i18n_cryptography_playground.menu_help_about_label, command = AboutProjectView)
        self.menu_bar.add_cascade(label = self.i18n_cryptography_playground.menu_help_label, menu = self.help_menu)


    def create_tabs(self):
        self.create_tab_control()
        self.create_coding_tab()
        self.create_decoding_tab()
        self.manage_tab_control()


    def create_tab_control(self):
        self.tab_control = ttk.Notebook(self.window)


    def create_coding_tab(self):
        self.coding_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.coding_tab, text = self.i18n_cryptography_playground.coding_tab_text)


    def create_decoding_tab(self):
        self.decoding_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.decoding_tab, text = self.i18n_cryptography_playground.decoding_tab_text)


    def manage_tab_control(self):
        self.tab_control.pack(expand = 1, fill = "both")


    def create_widgets_of_coding_tab(self):
        self.create_coding_section_labelframe()
        self.create_widgets_from_coding_section_labelframe()
        self.create_encryption_options_labelframe()
        self.create_buttons_from_encryption_options()


    def create_coding_section_labelframe(self):
        self.coding_labelframe = ttk.LabelFrame(self.coding_tab, text = self.i18n_cryptography_playground.coding_section_labelframe)
        self.coding_labelframe.grid(row = 0, padx = self.gui_settings.coding_section_padding_width, pady = self.gui_settings.padding_height)


    def create_widgets_from_coding_section_labelframe(self):
        self.create_label_for_message_to_be_encrypted()
        self.create_scrolledtext_for_message_to_be_encrypted()
        self.create_label_for_encrypted_message()
        self.create_scrolledtext_for_encrypted_message()


    def create_label_for_message_to_be_encrypted(self):
        self.label_for_message_to_be_encrypted = ttk.Label(self.coding_labelframe, text = self.i18n_cryptography_playground.label_for_message_to_be_encrypted, font = (self.gui_settings.font_family, self.gui_settings.font_size))
        self.label_for_message_to_be_encrypted.grid(row = 1)


    def create_scrolledtext_for_message_to_be_encrypted(self):
        self.scrolledtext_for_message_to_be_encrypted = scrolledtext.ScrolledText(self.coding_labelframe, width = self.gui_settings.scrolledtext_width, height = self.gui_settings.scrolledtext_height, font = (self.gui_settings.font_family, self.gui_settings.font_size), wrap = tk.WORD)
        self.scrolledtext_for_message_to_be_encrypted.grid(row = 2, pady = self.gui_settings.padding_height)
        self.scrolledtext_for_message_to_be_encrypted.focus()


    def create_label_for_encrypted_message(self):
        self.label_encrypted_message = ttk.Label(self.coding_labelframe, text = self.i18n_cryptography_playground.label_encrypted_message, font = (self.gui_settings.font_family, self.gui_settings.font_size))
        self.label_encrypted_message.grid(row = 3)

    
    def create_scrolledtext_for_encrypted_message(self):
        self.scrolledtext_for_encrypted_message = scrolledtext.ScrolledText(self.coding_labelframe, width = self.gui_settings.scrolledtext_width, height = self.gui_settings.scrolledtext_height, font = (self.gui_settings.font_family, self.gui_settings.font_size), wrap = tk.WORD)
        self.scrolledtext_for_encrypted_message.grid(row = 4, pady = self.gui_settings.padding_height)


    def create_encryption_options_labelframe(self):
        self.coding_tab_cryptography_options = ttk.LabelFrame(self.coding_labelframe, text = self.i18n_cryptography_playground.cryptography_options)
        self.coding_tab_cryptography_options.grid(row = 5, pady = self.gui_settings.padding_height, sticky = tk.W)


    def create_buttons_from_encryption_options(self):
        self.create_caesar_encryption_button()
        self.create_morse_encryption_button()
        self.add_padding_to_encryption_buttons()


    def create_caesar_encryption_button(self):
        self.button_caesar_cryptography = ttk.Button(self.coding_tab_cryptography_options, text = self.i18n_cryptography_playground.caesar_cryptography_button_text, command = lambda : self.process_message(Caesar, "encrypt", self.scrolledtext_for_message_to_be_encrypted, self.scrolledtext_for_encrypted_message))
        self.button_caesar_cryptography.grid(column = 0, row = 0, sticky = tk.W)


    def create_morse_encryption_button(self):
        self.button_morse_cryptography = ttk.Button(self.coding_tab_cryptography_options, text = self.i18n_cryptography_playground.morse_cryptography_button_text, command = lambda : self.process_message(Morse, "encrypt", self.scrolledtext_for_message_to_be_encrypted, self.scrolledtext_for_encrypted_message))
        self.button_morse_cryptography.grid(column = 1, row = 0, sticky = tk.W)


    def add_padding_to_encryption_buttons(self):
        for button in self.coding_tab_cryptography_options.winfo_children():
            button.grid_configure(padx = self.gui_settings.padding_width, pady = self.gui_settings.padding_height)


    def create_widgets_of_decoding_tab(self):
        self.create_decoding_section_labelframe()
        self.create_widgets_from_decoding_section_labelframe()
        self.create_decryption_options_labelframe()
        self.create_buttons_from_decryption_options()


    def create_decoding_section_labelframe(self):
        self.decoding_labelframe = ttk.LabelFrame(self.decoding_tab, text = self.i18n_cryptography_playground.decoding_section_labelframe)
        self.decoding_labelframe.grid(row = 0, padx = self.gui_settings.coding_section_padding_width, pady = self.gui_settings.padding_height)


    def create_widgets_from_decoding_section_labelframe(self):
        self.create_label_for_message_to_be_decrypted()
        self.create_scrolledtext_for_message_to_be_decrypted()
        self.create_label_for_decrypted_message()
        self.create_scrolledtext_for_decrypted_message()


    def create_label_for_message_to_be_decrypted(self):
        self.label_for_message_to_be_decrypted = ttk.Label(self.decoding_labelframe, text = self.i18n_cryptography_playground.label_for_message_to_be_decrypted, font = (self.gui_settings.font_family, self.gui_settings.font_size))
        self.label_for_message_to_be_decrypted.grid(row = 1)


    def create_scrolledtext_for_message_to_be_decrypted(self):
        self.scrolledtext_for_message_to_be_decrypted = scrolledtext.ScrolledText(self.decoding_labelframe, width = self.gui_settings.scrolledtext_width, height = self.gui_settings.scrolledtext_height, font = (self.gui_settings.font_family, self.gui_settings.font_size), wrap = tk.WORD)
        self.scrolledtext_for_message_to_be_decrypted.grid(row = 2, pady = self.gui_settings.padding_height)
        self.scrolledtext_for_message_to_be_decrypted.focus()


    def create_label_for_decrypted_message(self):
        self.label_decrypted_message = ttk.Label(self.decoding_labelframe, text = self.i18n_cryptography_playground.label_decrypted_message, font = (self.gui_settings.font_family, self.gui_settings.font_size))
        self.label_decrypted_message.grid(row = 3)

    
    def create_scrolledtext_for_decrypted_message(self):
        self.scrolledtext_for_decrypted_message = scrolledtext.ScrolledText(self.decoding_labelframe, width = self.gui_settings.scrolledtext_width, height = self.gui_settings.scrolledtext_height, font = (self.gui_settings.font_family, self.gui_settings.font_size), wrap = tk.WORD)
        self.scrolledtext_for_decrypted_message.grid(row = 4, pady = self.gui_settings.padding_height)


    def create_decryption_options_labelframe(self):
        self.decoding_tab_cryptography_options = ttk.LabelFrame(self.decoding_labelframe, text = self.i18n_cryptography_playground.cryptography_options)
        self.decoding_tab_cryptography_options.grid(row = 5, pady = self.gui_settings.padding_height, sticky = tk.W)


    def create_buttons_from_decryption_options(self):
        self.create_caesar_decryption_button()
        self.create_morse_decryption_button()
        self.add_padding_to_decryption_buttons()


    def create_caesar_decryption_button(self):
        self.button_caesar_cryptography = ttk.Button(self.decoding_tab_cryptography_options, text = self.i18n_cryptography_playground.caesar_cryptography_button_text, command = lambda : self.process_message(Caesar, "decrypt", self.scrolledtext_for_message_to_be_decrypted, self.scrolledtext_for_decrypted_message))
        self.button_caesar_cryptography.grid(column = 0, row = 0, sticky = tk.W)


    def create_morse_decryption_button(self):
        self.button_morse_cryptography = ttk.Button(self.decoding_tab_cryptography_options, text = self.i18n_cryptography_playground.morse_cryptography_button_text, command = lambda : self.process_message(Morse, "decrypt", self.scrolledtext_for_message_to_be_decrypted, self.scrolledtext_for_decrypted_message))
        self.button_morse_cryptography.grid(column = 1, row = 0, sticky = tk.W)

    
    def add_padding_to_decryption_buttons(self):
        for button in self.decoding_tab_cryptography_options.winfo_children():
            button.grid_configure(padx = self.gui_settings.padding_width, pady = self.gui_settings.padding_height)


    def close_window(self):
        self.window.quit()
        self.window.destroy()
        exit()

    
    def open_new_window(self):
        CryptographyPlayground()


    def show_message_box(self, type, title, content):
        type = type.lower()
        if type == "info":
            msg.showinfo(title, content)

        elif type == "warning":
            msg.showwarning(title, content)

        elif type == "error":
            msg.showerror(title, content)


    def change_message_on_scrolledtext(self, scrolledtext, message):
        scrolledtext.delete("1.0", "end")
        scrolledtext.insert("1.0", message)


    def get_text_from_scrolledtext(self, scrolledtext):
        text = scrolledtext.get("1.0", "end-1c").strip()
        return text


    def process_message(self, cryptography_algorithm, action, source_scrolledtext, destiny_scrolledtext):
        source_message = self.get_text_from_scrolledtext(source_scrolledtext)

        if source_message == "":
            self.show_message_box("warning", self.i18n_message_box.nothing_written_warning_title, self.i18n_message_box.nothing_written_warning_content)

        else:
            try:
                if action == "encrypt":
                    destiny_message = cryptography_algorithm().encrypt(source_message)

                elif action == "decrypt":
                    destiny_message = cryptography_algorithm().decrypt(source_message)

                self.change_message_on_scrolledtext(destiny_scrolledtext, destiny_message)
                destiny_scrolledtext.focus()

            except Exception as exception:
                print(exception)
                self.show_message_box("error", self.i18n_message_box.process_error_title, self.i18n_message_box.process_error_content)
    

if __name__ == "__main__":
    cryptography_playground = CryptographyPlayground()
    cryptography_playground.window.mainloop()