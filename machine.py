import decimal
from typing import List, Dict
from widgets import Widget


class Item():
    name = None

    def __init__(self, name: str, price: decimal):
        self.name = name
        self.price = price
        self.widget = Widget()
        
    def __repr__(self):
        return self.name + ': ' + str(self.price)


class Machine():
    
    def __init__(self, items: Dict[Item.name, Item], cash: dict):
        self.total = 0
        self.items = items
        self.cash = cash
        self.balance = sum(self.cash.values())

    def _buy_item(self, item: Item) -> bool:
        if item in self.items.keys() and self.items[item] > 0:
            self.items[item] -= 1
            self.balance += item.price
            return True
        return False
    
    def buy_items(self, selected_items: List[Item]):
        return_cash = 0
        for selected_item in selected_items:
            self.total += selected_item.price

        return selected_items, return_cash

