import dearpygui.dearpygui as dpg
from Main.File_anonymization.dicom_files_anonymization import anonymize_dicom
import os

def start_callback():
    input_file = dpg.get_value("input_file")
    output_folder = dpg.get_value("output_folder")
    patient_name = dpg.get_value("name")
    patient_id = dpg.get_value("id")
    patient_birth_date = dpg.get_value("birth_date")

    if input_file and output_folder:
        print(f"Input File: {input_file}")
        print(f"Output Folder: {output_folder}")
        print("Starting process...")

        output_file_path = os.path.join(output_folder, "anonymized.dcm")
        try:
            anonymize_dicom(input_file, output_file_path)
            print(f"Plik zapisny jako: {output_file_path}")
            dpg.set_value("success_text", output_file_path)
            dpg.configure_item("success_modal", show=True)
            dpg.focus_item("success_modal")
        except ValueError as e:
            print(f"Error: {e}")
            dpg.configure_item("error_modal", show=True)
    else:
        dpg.configure_item("error_modal", show=True)