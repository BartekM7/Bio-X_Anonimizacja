from pyqt5GUI.windows import *
from PyQt5.QtWidgets import QApplication
import sys

def start_gui():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())