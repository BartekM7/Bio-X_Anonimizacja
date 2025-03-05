from pickle import FALSE

from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QFileDialog, QCheckBox



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "apka"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 1000
        self.initUI()
        self.file = False
        self.directory = False

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button_select_input_filepath = QPushButton("Select Input File Path", self)
        self.button_select_input_filepath.move(100, 70)
        self.button_select_input_filepath.clicked.connect(self.on_button_select_input_filepath_click)
        self.button_select_input_filepath.hide()

        self.label_input_filepath = QLabel("Input File Path", self)
        self.label_input_filepath.adjustSize()
        self.label_input_filepath.move(120, 120)

        self.button_select_output_filepath = QPushButton("Select Output File Path", self)
        self.button_select_output_filepath.move(100, 150)
        self.button_select_output_filepath.clicked.connect(self.on_button_select_output_filepath_click)
        self.button_select_output_filepath.hide()

        self.label_output_filepath = QLabel("Output File Path", self)
        self.label_output_filepath.adjustSize()
        self.label_output_filepath.move(120, 200)

        self.checkbox_file = QCheckBox("File", self)
        self.checkbox_file.setGeometry(50, 250, 100, 30)
        self.checkbox_file.stateChanged.connect(self.on_checkbox_click_file)

        self.checkbox_directory = QCheckBox("dir", self)
        self.checkbox_directory.setGeometry(50,300,100,30)
        self.checkbox_directory.stateChanged.connect(self.on_checkbox_click_directory)

        self.show()

    #dialogi:
    def on_button_select_input_filepath_click(self):
        selected_file_path = ""
        if self.file:
            file_name, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)")
        else:
            file_name= QFileDialog.getExistingDirectory(self, "Select Directory")

        if file_name:
            selected_file_path = file_name[0] if isinstance(file_name, list) else file_name
            self.label_input_filepath.setText(f"Selected file: {selected_file_path}")
            self.label_input_filepath.adjustSize()
            print(file_name)
        else:
            self.label_input_filepath.setText("No file selected")
            self.label_input_filepath.adjustSize()
        return selected_file_path

    def on_button_select_output_filepath_click(self):
        selected_file_path = ""
        if self.file:
            file_name, _ = QFileDialog.getOpenFileNames(self, "Select File", "", "All Files (*)")
        else:
            file_name= QFileDialog.getExistingDirectory(self, "Select Directory")

        if file_name:
            selected_file_path = file_name[0] if isinstance(file_name, list) else file_name
            self.label_output_filepath.setText(f"Selected file: {selected_file_path}")
            self.label_output_filepath.adjustSize()
        else:
            self.label_output_filepath.setText("No file selected")
            self.label_output_filepath.adjustSize()

        return selected_file_path

    def on_checkbox_click_file(self, state):
        if state:
            self.checkbox_directory.hide()
            self.button_select_input_filepath.show()
            self.button_select_output_filepath.show()
            self.file = True
        else:
            self.checkbox_directory.show()
            self.button_select_input_filepath.hide()
            self.button_select_output_filepath.hide()
            self.file = False

    def on_checkbox_click_directory(self, state):
        if state:
            self.checkbox_file.hide()
            self.button_select_input_filepath.show()
            self.button_select_output_filepath.show()
            self.directory = True
        else:
            self.checkbox_file.show()
            self.button_select_input_filepath.hide()
            self.button_select_output_filepath.hide()
            self.directory = False
