import sys
import os

import pytest
from PySide2.QtWidgets import QApplication

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vending_machine_fuctions import VendingMachine
from main import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
gui_functions = VendingMachine(GUI=window)


def test_get_price():
    price_1 = gui_functions.get_price("drink_machine", "coke")
    price_2 = gui_functions.get_price("snack_machine", "pantera_rosa")

    assert price_1 == 120 and price_2 == 70


def test_enough_money_check():
    gui_functions.money = 100
    answer_1 = gui_functions.enough_money_check(100, "hot_chocolate")
    answer_2 = gui_functions.enough_money_check(150, "coffee")

    assert answer_1 == "YES" and answer_2 == "NO"


def test_prepare_product_and_get_change():
    gui_functions.wallet = [100, 50]
    gui_functions.money = sum(gui_functions.wallet)
    left_change_1 = gui_functions.prepare_product_and_get_change(100)
    left_change_2 = gui_functions.prepare_product_and_get_change(200)

    assert left_change_1 == 0 and left_change_2 != 0


def test_take_money_and_reset_machine():
    amount_of_ones = gui_functions.ones
    amount_of_fifties = gui_functions.fifties
    gui_functions.wallet = [100, 50]
    gui_functions.take_money_and_reset_machine(0)

    amount_of_ones += 1
    amount_of_fifties += 1

    assert (
        gui_functions.ones == amount_of_ones
        and gui_functions.fifties == amount_of_fifties
    )


def test_decline_purchase():
    gui_functions.wallet = [100, 50, 50]
    gui_functions.money = sum(gui_functions.wallet)
    gui_functions.decline_purchase()

    assert len(gui_functions.wallet) == 0 and gui_functions.money == 0
