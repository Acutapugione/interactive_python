import sys
import subprocess
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QTextEdit


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!", parent=self)

        self.setFixedSize(QSize(400, 300))

        self.label = QLabel()

        self.input = QTextEdit()
        # self.input.textChanged.connect(self.label.setText)

        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        code_text = self.input.toPlainText()
        with open("tmp.py", "w") as fp:
            fp.write(code_text)

        from tmp import a
        print(a)
        # subprocess.run(["python3", "-m", "tmp"])

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()