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
        self.threadclass.signal_progress_bar.connect(self.update_progress_bar)
        self.threadclass.signal_reset_buttons.connect(self.reset_buttons)

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

    def update_progress_bar(self, progress):
        """A progress bar will appear if the progress is different than -1.
        -1 value is used only to hide again progress bar"""
        if progress != -1:
            if self.ui.progressbar.height() == 0:
                self.ui.progressbar.setMaximumHeight(28)  # Show progress bar.
            self.ui.progressbar.setValue(progress)
        else:
            self.ui.progressbar.setMaximumHeight(0)

    def reset_buttons(self):
        self.ui.pushButton_add_coin.setEnabled(True)
        self.ui.pushButton_cancel.setEnabled(True)
        self.ui.pushButton_choco.setEnabled(True)
        self.ui.pushButton_coffee.setEnabled(True)
        self.ui.pushButton_water.setEnabled(True)


class ThreadClass(QThread):
    def __init__(self, parent=MainWindow) -> None:
        super(ThreadClass, self).__init__(None)

    signal_change_status = Signal(str)
    signal_disable_buttons = Signal(str)
    signal_progress_bar = Signal(int)
    signal_reset_buttons = Signal()

    def run(self):
        if window.behavior == "insert_coin":
            gui_functions.check_and_add_coin("coffee_machine")

        if window.behavior == "cancel_buying":
            gui_functions.decline_purchase()

        if window.behavior == "make_coffe":
            price = gui_functions.get_price("coffee_machine", "coffee")
            answer = gui_functions.enough_money_check(price, "coffee")
            if answer == "YES":
                change = gui_functions.prepare_product_and_get_change(price)
                gui_functions.take_money_and_reset_machine(change)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    gui_functions = VendingMachine(GUI=window)
    sys.exit(app.exec_())
