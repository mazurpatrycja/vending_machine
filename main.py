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
        self.ui.pushButton_coffee.clicked.connect(
            lambda: self.change_behavior("make_coffe")
        )

        # Thread signals.
        self.threadclass.signal_change_status.connect(self.change_status)
        self.threadclass.signal_disable_buttons.connect(self.disable_buttons)

    def change_behavior(self, next_behavior):
        self.behavior = next_behavior
        self.threadclass.start()

    def change_status(self, status):
        self.ui.label_status.setText(status)

    def disable_buttons(self, product):
        if product == "coffee":
            self.ui.pushButton_choco.setDisabled(True)
            self.ui.pushButton_water.setDisabled(True)
        if product == "hot_chocolate":
            self.ui.pushButton_coffee.setDisabled(True)
            self.ui.pushButton_water.setDisabled(True)
        if product == "hot_water":
            self.ui.pushButton_coffee.setDisabled(True)
            self.ui.pushButton_choco.setDisabled(True)

        # The user cannot cancel or add coins
        # while the product is about to be prepared.
        self.ui.pushButton_cancel.setDisabled(True)
        self.ui.pushButton_add_coin.setDisabled(True)


class ThreadClass(QThread):
    def __init__(self, parent=MainWindow) -> None:
        super(ThreadClass, self).__init__(None)

    signal_change_status = Signal(str)
    signal_disable_buttons = Signal(str)

    def run(self):
        if window.behavior == "insert_coin":
            gui_functions.check_and_add_coin("coffee_machine")

        if window.behavior == "cancel_buying":
            gui_functions.decline_purchase()

        if window.behavior == "make_coffe":
            price = gui_functions.get_price("coffee_machine", "coffee")
            answer = gui_functions.enough_money_check(price, "coffee")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    gui_functions = VendingMachine(GUI=window)
    sys.exit(app.exec_())
