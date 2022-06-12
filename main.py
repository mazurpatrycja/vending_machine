import sys

from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QThread, Signal

from vending_machine_gui import Ui_Form
from vending_machine_fuctions import VendingMachine


class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.threadclass = ThreadClass()
        self.interface()
        self.behavior = None
        self.show()

    def interface(self):
        self.ui.pushButton_add_coin.clicked.connect(
            lambda: self.change_behavior("insert_coin")
        )
        self.ui.pushButton_cancel.clicked.connect(
            lambda: self.change_behavior("cancel_buying")
        )

        # Thread signals.
        self.threadclass.signal_change_status.connect(self.change_status)

    def change_behavior(self, next_behavior):
        self.behavior = next_behavior
        self.threadclass.start()

    def change_status(self, status):
        self.ui.label_status.setText(status)


class ThreadClass(QThread):
    def __init__(self, parent=MainWindow) -> None:
        super(ThreadClass, self).__init__(None)

    signal_change_status = Signal(str)

    def run(self):
        if window.behavior == "insert_coin":
            gui_functions.check_and_add_coin("coffee_machine")
        if window.behavior == "cancel_buying":
            gui_functions.decline_purchase()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    gui_functions = VendingMachine(GUI=window)
    sys.exit(app.exec_())
