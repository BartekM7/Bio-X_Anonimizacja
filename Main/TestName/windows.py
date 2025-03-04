import dearpygui.dearpygui as dpg
from TestName.callbacks import start_callback

def main_window():
    with dpg.window(label="Wybór", width=700, height=400,no_title_bar=True):
        dpg.add_text("Wybierz plik do anonimizacji:")

        dpg.add_input_text(tag="input_file", width=400)
        dpg.add_spacer(height=5)

        dpg.add_checkbox(tag="rekurencyjnie", label="Rekurencyjnie")

        dpg.add_button(label="Wybierz..", callback=lambda: dpg.show_item("input_file_dialog"))

        dpg.add_spacer(height=20)
        dpg.add_text("Wybierz folder na plik po anonimizacji:")
        dpg.add_input_text(tag="output_folder", width=600)
        dpg.add_spacer(height=10)
        dpg.add_button(label="Wybierz...", callback=lambda: dpg.show_item("output_folder_dialog"))

        dpg.add_spacer(height=20)
        dpg.add_button(label="Start", callback=lambda: dpg.configure_item("anonymization_modal", show=True))

def error_window():
    with dpg.window(label="Błąd", modal=True, show=False, tag="error_modal", no_title_bar=True, width=200, height=10,):
        dpg.add_text("Wybierz plik i folder.")
        error_button = dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_modal", show=False))

def success_window():
    with dpg.window(label="Sukces", modal = True, show=False, tag="success_modal", no_title_bar=True, width=350, height=30):
        dpg.add_text("Zanonimizowany plik znajduje się pod adresem:\n")
        dpg.add_text("", tag="success_text")
        success_button = dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("success_modal", show=False))

def anonymization_data_window():
    with dpg.window(label="Anonimizacja", width=400, height=300,no_title_bar=True, show=False, tag="anonymization_modal"):
        dpg.add_text("Dane do animizacji\n")

        dpg.add_text("PatientNAME:")
        dpg.add_input_text(tag="name", width=300)
        dpg.add_spacer(height=10)

        dpg.add_text("PatientID:")
        dpg.add_input_text(tag="id", width=300)
        dpg.add_spacer(height=10)

        dpg.add_text("PatientBirthDate:")
        dpg.add_input_text(tag="birth_date", width=300)
        dpg.add_spacer(height=10)

        dpg.add_button(label="Rozpocznij anonimizacje", callback=start_callback)
