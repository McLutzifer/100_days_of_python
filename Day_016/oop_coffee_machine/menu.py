class Coffee:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    def __init__(self) -> None:
        self.menu = [
            Coffee(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            Coffee(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            Coffee(name="cappuccino", water=250, milk=50, coffee=24, cost=3.0)
        ]
    
    