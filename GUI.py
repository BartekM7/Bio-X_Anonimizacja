import dearpygui.dearpygui as dpg


def start_callback():
    input_file = dpg.get_value("input_file")
    output_folder = dpg.get_value("output_folder")

    if input_file and output_folder:
        print(f"Input File: {input_file}")
        print(f"Output Folder: {output_folder}")
        print("Starting process...")
        # Add your processing code here
    else:
        # Show an error popup if either input file or output folder is missing
        dpg.configure_item("error_modal", show=True)


dpg.create_context()

# Main window
with dpg.window(label="Anonimizacja", width=700, height=400,no_title_bar=True):
    dpg.add_text("Wybierz plik do anonimizacji:")
    dpg.add_input_text(tag="input_file", width=600)
    dpg.add_spacer(height=10)
    dpg.add_button(label="Wybierz..", callback=lambda: dpg.show_item("input_file_dialog"))

    dpg.add_text("Wybierz folder na plik po anonimizacji:")
    dpg.add_input_text(tag="output_folder", width=600)
    dpg.add_spacer(height=10)
    dpg.add_button(label="Wybierz...", callback=lambda: dpg.show_item("output_folder_dialog"))

    dpg.add_spacer(height=20)
    dpg.add_button(label="Start", callback=start_callback)

# File dialog for input file
with dpg.file_dialog(directory_selector=False, show=False,width=600, height=300,
                     callback=lambda sender, app_data: dpg.set_value("input_file", app_data['file_path_name']),
                     tag="input_file_dialog"):
    dpg.add_file_extension(".DICOM")

# Directory dialog for output folder
with dpg.file_dialog(directory_selector=True, show=False,width=600, height=300,
                     callback=lambda sender, app_data: dpg.set_value("output_folder", app_data['file_path_name']),
                     tag="output_folder_dialog"):
    pass

# Error modal popup
with dpg.window(label="Błąd", modal=True, show=False, tag="error_modal", no_title_bar=True, width=175, height=30,):
    dpg.add_text("Wybierz plik i folder.")
    dpg.set_item_pos("error_modal",(300,100))
    error_button = dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("error_modal", show=False))
    dpg.set_item_pos(error_button, (50,50))

dpg.create_viewport(title='Anonimizacja', width=700, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()