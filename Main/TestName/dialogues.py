import dearpygui.dearpygui as dpg

def input_dialogue():
    checkbox_state = dpg.get_value("rekurencyjnie")

    if checkbox_state:
        # wywołanie rekurencyjne
        print("Rekurencyjnie")
    else:
        # pojedynczy plik DCM
        print("Pojedynczy plik")
    with dpg.file_dialog(directory_selector=False, show=False,width=600, height=300,
                         callback=lambda sender, app_data: dpg.set_value("input_file", app_data['file_path_name']),
                         tag="input_file_dialog"):
        dpg.add_file_extension(".DCM")

def output_dialogue():
    with dpg.file_dialog(directory_selector=True, show=False,width=600, height=300,
                         callback=lambda sender, app_data: dpg.set_value("output_folder", app_data['file_path_name']),
                         tag="output_folder_dialog"):
        pass


