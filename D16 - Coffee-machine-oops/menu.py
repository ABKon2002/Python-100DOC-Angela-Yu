class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", ingredients = {'water': 200, 'milk': 150, 'coffee': 24}, cost=2.5),
            MenuItem(name="espresso", ingredients = {'water': 50, 'coffee': 18}, cost=1.5),
            MenuItem(name="cappuccino", ingredients = {'water': 250, 'milk': 50, 'coffee': 24}, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

    def get_item(self, drink):
        for item in self.menu:
            if item.name == drink.lower():
                return item
        return -1

