from xml.etree.ElementTree import tostring

from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QFileDialog, QCheckBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "apka"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 1000
        self.main_window()
        self.directory = False
        self.selected_input_path = " "
        self.selected_output_path = " "

    def main_window(self):
        #First thing first
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #select in_file button
        self.button_select_input_path = QPushButton("Select Input File Path", self)
        self.button_select_input_path.move(100, 70)
        self.button_select_input_path.clicked.connect(self.on_button_select_input_path_click)

        #label for select in_file path
        self.label_input_path = QLabel("Input File Path", self)
        self.label_input_path.adjustSize()
        self.label_input_path.move(120, 120)

        #select out_file button
        self.button_select_output_path = QPushButton("Select Output File Path", self)
        self.button_select_output_path.move(100, 150)
        self.button_select_output_path.clicked.connect(self.on_button_select_output_filepath_click)

        #lebel for selected out_file path
        self.label_output_path = QLabel("Output File Path", self)
        self.label_output_path.adjustSize()
        self.label_output_path.move(120, 200)

        #button for future use
        self.button_future_use = QPushButton("Future use button",self)
        self.button_future_use.move(100, 400)
        self.button_future_use.clicked.connect(self.on_button_future_use_function)

        #check box for if files are in or out
        self.checkbox_directory = QCheckBox("dir", self)
        self.checkbox_directory.setGeometry(50, 250, 100, 50)
        self.checkbox_directory.stateChanged.connect(self.on_checkbox_click_directory)

        #shows all
        self.show()

    #dialog for input button
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

    #button for future use space for function
    def on_button_future_use_function(self):
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
