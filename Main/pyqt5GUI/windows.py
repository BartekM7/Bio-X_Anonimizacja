from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QFileDialog, QCheckBox
from PyQt5.QtGui import QIcon

from File_anonymization.dicom_files_anonymization import anonymize_dicom_directory, anonymize_single_dicom_file_and_save


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Anonimizacja plików DCM"
        self.setWindowIcon(QIcon("/Main/pyqt5GUI/Assets/ikonka_testowa.png"))
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 200
        self.main_window()
        self.directory = False
        self.selected_input_path = " "
        self.selected_output_path = " "


    def main_window(self):
        #First thing first
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # label for select in_file path
        self.label_input_path = QLabel("Input File Path", self)
        self.label_input_path.adjustSize()
        self.label_input_path.move(20, 10)

        #select in_file button
        self.button_select_input_path = QPushButton("Select Input File Path", self)
        self.button_select_input_path.move(10, 30)
        self.button_select_input_path.clicked.connect(self.on_button_select_input_path_click)

        # lebel for selected out_file path
        self.label_output_path = QLabel("Output File Path", self)
        self.label_output_path.adjustSize()
        self.label_output_path.move(20, 70)

        #select out_file button
        self.button_select_output_path = QPushButton("Select Output File Path", self)
        self.button_select_output_path.move(10, 90)
        self.button_select_output_path.clicked.connect(self.on_button_select_output_filepath_click)

        #check box for if files are in or out
        self.checkbox_directory = QCheckBox("dir", self)
        self.checkbox_directory.setGeometry(20, 110, 100, 50)
        self.checkbox_directory.stateChanged.connect(self.on_checkbox_click_directory)

        # button for future use
        self.button_future_use = QPushButton("Start", self)
        self.button_future_use.move(10, 160)
        self.button_future_use.clicked.connect(self.on_button_future_use_function)

        #shows all
        self.show()

    #dialog for output button
    def on_button_select_output_filepath_click(self):
        if self.directory:
            file_name= QFileDialog.getExistingDirectory(self, "Select Directory")
        else:
            file_name, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)")

        if file_name:
            self.selected_output_path = file_name[0] if isinstance(file_name, list) else file_name
            self.label_output_path.setText(f"Selected file: {self.selected_output_path}")
            self.label_output_path.adjustSize()
        else:
            self.label_output_path.setText("No file selected")
            self.label_output_path.adjustSize()

    # dialog for input button
    def on_button_select_input_path_click(self):
        if self.directory:
            file_name = QFileDialog.getExistingDirectory(self, "Select Directory")
        else:
            file_name, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)")

        if file_name:
            self.selected_input_path = file_name[0] if isinstance(file_name, list) else file_name
            self.label_input_path.setText(f"Selected file: {self.selected_input_path}")
            self.label_input_path.adjustSize()
        else:
            self.label_input_path.setText("No file selected")
            self.label_input_path.adjustSize()

    #button for future use space for function
    def on_button_future_use_function(self):
        if self.directory:
            anonymize_dicom_directory(self.selected_input_path, self.selected_output_path)
        else:
            anonymize_single_dicom_file_and_save(self.selected_input_path, self.selected_output_path)
        #put future function here
        # function_name(self.selected_input_path, self.selected_output_path , self.directory)
        ################        string                     string               bool
        #and then comment return
        return
        #print(self.selected_input_path + "    " + self.selected_output_path + "     " + f"{self.directory}")

    #checkbox if directory
    def on_checkbox_click_directory(self, state):
        if state:
            self.directory = True
        else:
            self.directory = False

# class SuccesWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         super().title = "Success"
#         self.width = 200
#         self.height = 100
#
#     def succes_window(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # label for select in_file path
#         self.label_input_path = QLabel("Success", self)
#         self.label_input_path.adjustSize()
#         self.label_input_path.move(20, 10)
