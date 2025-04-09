from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QMovie
import sys

class JarvisUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JARVIS Activated")
        self.setGeometry(100, 100, 600, 600)

        # Set up label for GIF
        self.label = QLabel(self)
        self.movie = QMovie("assets/jarvis.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisUI()
    window.show()
    sys.exit(app.exec_())
