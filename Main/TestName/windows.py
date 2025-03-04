import dearpygui.dearpygui as dpg
from TestName.callbacks import start_callback

def main_window():
    with dpg.window(label="Anonimizacja", width=700, height=400,no_title_bar=True):
        dpg.add_text("Wybierz plik do anonimizacji:")
        dpg.add_input_text(tag="input_file", width=600)
        dpg.add_spacer(height=10)
        dpg.add_button(label="Wybierz..", callback=lambda: dpg.show_item("input_file_dialog"))

        dpg.add_spacer(height=20)
        dpg.add_text("Wybierz folder na plik po anonimizacji:")
        dpg.add_input_text(tag="output_folder", width=600)
        dpg.add_spacer(height=10)
        dpg.add_button(label="Wybierz...", callback=lambda: dpg.show_item("output_folder_dialog"))

        dpg.add_spacer(height=20)
        dpg.add_button(label="Start", callback=start_callback)

def error_window():
    with dpg.window(label="Błąd", modal=True, show=False, tag="error_modal", no_title_bar=True, width=200, height=10,):
        dpg.add_text("Wybierz plik i folder.")
        error_button = dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_modal", show=False))

def success_window():
    with dpg.window(label="Sukces", modal = True, show=False, tag="success_modal", no_title_bar=True, width=350, height=30):
        dpg.add_text("Zanonimizowany plik znajduje się pod adresem:\n")
        dpg.add_text("", tag="success_text")
        success_button = dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("success_modal", show=False))
