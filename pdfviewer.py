from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView  # , QWebEngineSettings
from PyQt5.QtWidgets import QMainWindow


class PdfPreviewer(QMainWindow):
    def __init__(self):
        super(PdfPreviewer, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setFixedSize(500, 700)

        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.webView.urlChanged.connect(self.url_changed)
        self.setCentralWidget(self.webView)

    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def open_file(self, file: str):
        self.webView.setUrl(QUrl(f"file://{file}"))
