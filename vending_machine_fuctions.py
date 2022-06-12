import json
import time


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

    def check_and_add_coin(self, machine_type: str) -> None:
        coin = self.GUI.ui.comboBox.currentText()
        coin = coin.replace(" EUR", "")
        coin = int(float(coin) * 100)  # Multiply to avoid float format.

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
        return

    def get_price(self, machine_type: str, chosen_product: str) -> int:
        file = open("products.json")
        products = json.load(file)
        price = products[machine_type][chosen_product]

        return price

    def enough_money_check(self, price: str, chosen_product: str) -> str:
        """Check if custumer inserted enough money.
        If not display appropriate message"""

        if self.money < price:
            self.status = "Not Enough Money"
            message = (
                self.welcome_message
                + str(self.money / 100)
                + " EUR "
                + self.status
            )
            self.GUI.threadclass.signal_change_status.emit(message)
            return "NO"
        else:
            self.GUI.threadclass.signal_disable_buttons.emit(chosen_product)
            return "YES"

    def prepare_product_and_get_change(self, price: int) -> int:
        change = self.money - price
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

        # When change is equal to 0, it means that costumer has inserted
        # enough money or all change has already been given.
        if change == 0:
            # Prepare product.
            self.status = "Preparing ...\n"
            message = (
                self.status
                + "Money: "
                + str(self.money / 100)
                + " EUR "
                + "Change: "
                + str((self.money - price) / 100)
                + " EUR"
            )
            self.GUI.threadclass.signal_change_status.emit(message)

            # Update progress bar to simulate preparing product.
            for i in [25, 50, 75, 100]:
                time.sleep(1)
                self.GUI.threadclass.signal_progress_bar.emit(i)

            # Give the change.
            self.status = "Change: " + str((self.money - price) / 100) + " EUR"
            message = (
                "Bought product.\n"
                + "Money: "
                + str(self.money / 100)
                + " EUR "
                + self.status
            )
            self.GUI.threadclass.signal_change_status.emit(message)
        else:
            self.status = "No change."
            message = self.status + " Money returned."
            self.GUI.threadclass.signal_change_status.emit(message)

        return change

    def take_money_and_reset_machine(self, change: int) -> None:
        # Add money to machine if the product was bought.
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

        # Reset machine to unlock buying another product.
        self.wallet = []
        self.money = 0
        time.sleep(3)
        message = self.welcome_message + "0 EUR "
        self.GUI.threadclass.signal_change_status.emit(message)
        self.GUI.threadclass.signal_progress_bar.emit(-1)
        self.GUI.threadclass.signal_reset_buttons.emit()

    def decline_purchase(self) -> None:
        # Return all money to the customer.
        self.wallet = []
        self.money = 0

        message = self.welcome_message + str(self.money) + " EUR"
        self.GUI.threadclass.signal_change_status.emit(message)
