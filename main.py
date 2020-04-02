import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Name: ')
        self.name_input = QLineEdit()
        self.text_label = QLabel("There has been no name entered, so I can't do anything yet.")
        self.button = QPushButton('Set Name')
        self.init_ui()

    def init_ui(self):
        self.button.clicked.connect(self.alter_name)

        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle('Nothing has been clicked')
        self.show()

    def alter_name(self):
        inputted_text = self.name_input.text()
        our_string = "You've entered " + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text + "'s Window")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())