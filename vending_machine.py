class VendingMachine:
    def __init__(self) -> None:
        self.wallet = []
        self.money = 0.0  # Sum of money in the wallet
        self.status = ""

        # Money for exchange
        self.ones = 20  # The amount of 1 Euro.
        self.fifties = 20  # The amount of 50 Eurocent.
        self.twenties = 20  # The amount of 20 Eurocent.
        self.dimes = 20  # The amount of 10 Eurocent.
        self.nickels = 20  # The amount of 5 Eurocent.

    def check_and_add_coin(self, machine_type, coin):
        self.status = ""  # Reset status.
        # Check if added coin is allowed.
        coffe_machine_coins = [1, 0.5]
        drink_machine_coins = [1, 0.5, 0.2, 0.1, 0.05]
        snack_machine_coins = [1, 0.5, 0.2, 0.1]

        if machine_type == "coffee_machine" and coin in coffe_machine_coins:
            self.wallet.append(coin)
        elif machine_type == "drink_machine" and coin in drink_machine_coins:
            print("here")
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
                price = 1.5
            elif chosen_product == "hot_chocolate":
                price = 1
            elif chosen_product == "hot_water":
                price = 0.5

        if machine_type == "drink_machine":
            if chosen_product == "coke":
                price = 1.20
            elif chosen_product == "water":
                price = 0.75

        if machine_type == "snack_machine":
            if chosen_product == "mms":
                price = 2.5
            elif chosen_product == "chips":
                price = 1.9
            elif chosen_product == "snickers":
                price = 1.3
            elif chosen_product == "pantera_rosa":
                price = 0.7

        return price

    def buy_product_and_get_changed(self, price):
        if self.money < price:
            self.status = "Not Enough Money"
            return

        change = round(self.money - price, 2)
        change_dict = {}

        if change > 0:
            one_euros = change // 1
            if one_euros > 0:
                if one_euros <= self.ones:
                    change_dict["one_euros"] = one_euros
                    change -= 1 * one_euros
                    self.ones -= one_euros
                else:
                    change_dict["one_euros"] = self.ones
                    change -= 1 * self.ones

            fifties = change // 0.5
            if fifties > 0:
                if fifties <= self.fifties:
                    change_dict["fifties"] = fifties
                    change -= 0.5 * fifties

                else:
                    change_dict["fifties"] = self.fifties
                    change -= 0.5 * self.fifties

            twenties = change // 0.2
            if twenties > 0:
                if twenties <= self.twenties:
                    change_dict["twenties"] = twenties
                    change -= 0.2 * twenties
                else:
                    change_dict["twenties"] = self.twenties
                    change -= 0.2 * self.twenties

            dimes = change // 0.1
            if dimes > 0:
                if dimes <= self.dimes:
                    change_dict["dimes"] = dimes
                    change -= 0.1 * dimes
                else:
                    change_dict["dimes"] = self.dimes
                    change -= 0.1 * self.dimes

            nickels = change // 0.05
            if nickels > 0:
                if nickels <= self.nickels:
                    change_dict["nickles"] = nickels
                    change -= 0.05 * nickels
                else:
                    change_dict["nickles"] = self.nickels
        change = round(change, 2)
        if change == 0:
            print(change_dict)
            self.status = "Bought product. Change: " + str(self.money - price)
        else:
            self.status = "No change"

    def decline_purchase(self):
        # Return all money to the customer.
        self.wallet = []
        self.money = 0


if __name__ == "__main__":
    machine = VendingMachine()

    machine.check_and_add_coin("coffee_machine", 0.1)
    machine.check_and_add_coin("coffee_machine", 0.1)
    machine.check_and_add_coin("coffee_machine", 0.75)
    machine.check_and_add_coin("coffee_machine", 5)

    price = machine.get_price("drink_machine", "coke")
    print("price:", price)

    machine.buy_product(price)
    print(machine.status)
