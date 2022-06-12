import json
import re


class VendingMachine:
    def __init__(self, GUI) -> None:
        self.GUI = GUI

        self.wallet = []
        self.money = 0  # Sum of money in the wallet
        self.status = ""

        # Money for exchange
        self.ones = 20  # The amount of: 1 Euro,
        self.fifties = 20  # 50 Eurocent,
        self.twenties = 20  # 20 Eurocent,
        self.dimes = 20  # 10 Eurocent,
        self.nickels = 20  # 5 Eurocent.

        self.welcome_message = (
            "Hello! Insert coins and choose product.\nMoney: "
        )

    def check_and_add_coin(self, machine_type):
        coin = self.GUI.ui.comboBox.currentText()
        coin = coin.replace(" EUR", "")
        coin = int(float(coin) * 100)  # Multiply to avoid float type

        self.status = ""  # Reset status.

        # Prices are in cents to avoid float format.
        coffe_machine_coins = [100, 50]
        drink_machine_coins = [100, 50, 20, 10, 5]
        snack_machine_coins = [100, 50, 20, 10]

        # Check if added coin is allowed.
        if machine_type == "coffee_machine" and coin in coffe_machine_coins:
            self.wallet.append(coin)
        elif machine_type == "drink_machine" and coin in drink_machine_coins:
            self.wallet.append(coin)
        elif machine_type == "snack_machine" and coin in snack_machine_coins:
            self.wallet.append(coin)
        else:
            self.money = sum(self.wallet)
            self.status = " Not Allowed Coin"
            message = (
                self.welcome_message
                + str(self.money / 100)
                + " EUR "
                + self.status
            )
            self.GUI.threadclass.signal_change_status.emit(message)
            return

        # Calculate how much money the customer has.
        self.money = sum(self.wallet)
        message = self.welcome_message + str(self.money / 100) + " EUR"
        self.GUI.threadclass.signal_change_status.emit(message)

    def get_price(self, machine_type, chosen_product):
        file = open("products.json")
        products = json.load(file)

        price = products[machine_type][chosen_product]

        return price

    def buy_product_and_get_change(self, price):
        if self.money < price:
            self.status = "Not Enough Money"
            return

        change = round(self.money - price, 2)
        change_dict = {}

        # Check how many coins of each denominations are needed.
        # Then check if there is enough coins in machine.
        if change > 0:
            one_euros = change // 100
            if one_euros > 0 and one_euros <= self.ones:
                change_dict["one_euros"] = one_euros
                change -= 100 * one_euros
                self.ones -= one_euros
            elif one_euros > 0 and one_euros > self.ones:
                change_dict["one_euros"] = self.ones
                change -= 100 * self.ones
                self.ones -= one_euros

            fifties = change // 50
            if fifties > 0 and fifties <= self.fifties:
                change_dict["fifties"] = fifties
                change -= 50 * fifties
                self.fifties -= fifties
            elif fifties > 0 and fifties > self.fifties:
                change_dict["fifties"] = self.fifties
                change -= 50 * self.fifties
                self.fifties -= fifties

            twenties = change // 20
            if twenties > 0 and twenties <= self.twenties:
                change_dict["twenties"] = twenties
                change -= 20 * twenties
                self.twenties -= twenties
            elif twenties > 0 and twenties > self.twenties:
                change_dict["twenties"] = self.twenties
                change -= 20 * self.twenties
                self.twenties -= twenties

            dimes = change // 10
            if dimes > 0 and dimes <= self.dimes:
                change_dict["dimes"] = dimes
                change -= 10 * dimes
                self.dimes -= dimes
            elif dimes > 0 and dimes > self.dimes:
                change_dict["dimes"] = self.dimes
                change -= 10 * self.dimes
                self.dimes -= dimes

            nickels = change // 5
            if nickels > 0 and nickels <= self.nickels:
                change_dict["nickles"] = nickels
                change -= 5 * nickels
                self.nickels -= nickels
            elif nickels > 0 and nickels > self.nickels:
                change_dict["nickles"] = self.nickels
                change -= 5 * self.nickels
                self.nickels -= nickels

        if change == 0:
            # Give the change.
            print(change_dict)
            self.status = (
                "Bought product. Change: "
                + str((self.money - price) / 100)
                + " EU"
            )
        else:
            self.status = "No change"

        return change

    def add_costumer_money_to_machine(self, change):
        if change == 0:
            for coin in self.wallet:
                if coin == 100:
                    self.ones += 1
                elif coin == 50:
                    self.fifties += 1
                elif coin == 20:
                    self.twenties += 1
                elif coin == 10:
                    self.dimes += 1
                elif coin == 5:
                    self.nickels += 1

    def decline_purchase(self):
        # Return all money to the customer.
        self.wallet = []
        self.money = 0
        message = self.welcome_message + str(self.money) + " EUR"
        self.GUI.threadclass.signal_change_status.emit(message)
