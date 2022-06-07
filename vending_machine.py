from platform import machine


class VendingMachine:
    def __init__(self) -> None:
        self.wallet = 0
        self.bank = 0  # Money for exchange

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
