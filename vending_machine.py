class VendingMachine:
    def __init__(self) -> None:
        self.wallet = []
        self.money = 0  # Sum of money in the wallet
        self.status = ""

        # Money for exchange
        self.ones = 20  # The amount of 1 Euro.
        self.fifties = 20  # The amount of 50 Eurocent.
        self.twenties = 20  # The amount of 20 Eurocent.
        self.dimes = 20  # The amount of 10 Eurocent.
        self.nickels = 20  # The amount of 5 Eurocent.

    def check_and_add_coin(self, machine_type, coin):
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
            self.status = "Not Allowed Coin"

        # Calculate how much money the customer has.
        self.money = sum(self.wallet)

    def get_price(self, machine_type, chosen_product):
        if machine_type == "coffee_machine":
            if chosen_product == "coffee":
                price = 150
            elif chosen_product == "hot_chocolate":
                price = 100
            elif chosen_product == "hot_water":
                price = 50

        if machine_type == "drink_machine":
            if chosen_product == "coke":
                price = 120
            elif chosen_product == "water":
                price = 75

        if machine_type == "snack_machine":
            if chosen_product == "mms":
                price = 250
            elif chosen_product == "chips":
                price = 190
            elif chosen_product == "snickers":
                price = 130
            elif chosen_product == "pantera_rosa":
                price = 70

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


if __name__ == "__main__":
    machine = VendingMachine()

    machine.check_and_add_coin("drink_machine", 100)
    machine.check_and_add_coin("drink_machine", 50)
    machine.check_and_add_coin("drink_machine", 75)
    machine.check_and_add_coin("drink_machine", 500)

    price = machine.get_price("drink_machine", "coke")
    print("price:", price)
    print("money", machine.money)
    change = machine.buy_product_and_get_change(price)
    machine.add_costumers_money_to_machine(change)
    print(machine.ones)
    print(machine.status)
