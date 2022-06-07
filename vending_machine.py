class VendingMachine:
    def __init__(self) -> None:
        self.wallet = []
        self.money = 0  # Sum of money in the wallet
        self.bank = 1000  # Money for exchange
        self.status = ""

    def check_and_add_coin(self, machine_type, coin):
        self.status = ""  # Reset status.
        # Check if added coin is allowed.
        coffe_machine_coins = [1, 0.5]
        drink_machine_coins = [1, 0.5, 0.2, 0.1, 0.05]
        snack_machine_coins = [1, 0.5, 0.2, 0.1]

        if machine_type == "coffee_machine" and coin in coffe_machine_coins:
            self.wallet.append(coin)
        elif machine_type == "dring_machine" and coin in drink_machine_coins:
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

    def buy_product(self, price):
        if self.money < price:
            self.status = "Not Enough Money"
        elif (self.money - price) > self.bank:
            self.status = "No Change"
        else:
            self.status = "Bought product. Change: " + str(self.money - price)
            self.bank = self.bank + price

    def decline_purchase(self):
        # Return all money to the customer.
        self.wallet = []
        self.money = 0


if __name__ == "__main__":
    machine = VendingMachine()
    price = machine.get_price("coffee_machine", "hot_chocolate")
    print(price)

    machine.check_and_add_coin("coffee_machine", 1)
    print(machine.money)
    machine.check_and_add_coin("coffee_machine", 0.5)
    print(machine.money)
    machine.check_and_add_coin("coffee_machine", 5)
    print(machine.money)

    machine.buy_product(price)
    print(machine.status)
