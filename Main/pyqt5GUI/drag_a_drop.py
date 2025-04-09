from PyQt5.QtWidgets import  QListWidget
from PyQt5.QtCore import Qt, QUrl
import os


class ListboxWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setAcceptDrops(True)
        self.move(750,0)
        self.resize(400, 400)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

        for url in event.mimeData().urls():
            if url.isLocalFile():
                file_path = str(url.toLocalFile())
                self.parent.selected_input_path = file_path
                self.on_drag_a_drop_set_input_label(file_path)
                break

        else:
            event.ignore()

        #print(self.selected_input_path)

    def on_drag_a_drop_set_input_label(self, path):
        if os.path.isdir(path):
            self.parent.label_input_path.setText(f"Selected Directory: {path}")
            self.parent.label_input_path.adjustSize()
            self.parent.directory = True
        elif os.path.isfile(path):
            self.parent.label_input_path.setText(f"Selected File: {path}")
            self.parent.label_input_path.adjustSize()
            self.parent.directory = False
