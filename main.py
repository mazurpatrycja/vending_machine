import sys

from PySide2.QtWidgets import QWidget, QApplication

from vending_machine_gui import Ui_Form
from vending_machine import VendingMachine


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    gui_functions = VendingMachine(GUI=window)
    sys.exit(app.exec_())
