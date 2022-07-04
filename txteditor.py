from PyQt5.QtWidgets import QMainWindow, QTextEdit


class TxtEditor(QMainWindow):
    def __init__(self):
        super(TxtEditor, self).__init__()

        self.setWindowTitle('Text Editor')
        self.setFixedSize(500, 700)

        self.txteditor = QTextEdit()
        self.txteditor.textChanged.connect(self.file_changed())
        self.setCentralWidget(self.txteditor)

    def file_changed(self):
        self.setWindowTitle(self.txteditor.documentTitle())

    def open_file(self, file: str):
        with open(file) as txt:
            self.txteditor.setText(txt.read())

