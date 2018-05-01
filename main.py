from PyQt5.QtWidgets import QApplication
from sys import argv
from lib.MainFormModule import MainForm


if __name__ == '__main__':
    app = QApplication(argv)
    form = MainForm()
    form.show()
    exit(app.exec_())
