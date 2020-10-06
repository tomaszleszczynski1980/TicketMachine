import decimal
from typing import List, Dict
from widgets import Widget


# class Item():
#     name = None
#
#     def __init__(self, name: str, price: decimal):
#         self.name = name
#         self.price = price
#         self.widget = Widget()
#
#     def __repr__(self):
#         return self.name + ': ' + str(self.price)
#
#     def select_item(self):
#         pass
#
#     def unselect_item(self):
#         pass


class Machine():

    class Item():
        name = str()

        def __init__(self, name: str, price: decimal):
            self.name = name
            self.price = price
            self.widget = Widget()

        def __repr__(self):
            return self.name + ': ' + str(self.price)

        def select_item(self):
            if self in Machine.items.keys() and Machine.items[self] > 0:
                Machine.items[self] -= 1
                Machine.total += self.price
                Machine.selected_items.append(self)

        def unselect_item(self):
            if self in Machine.selected_items:
                Machine.items[self] += 1
                Machine.total -= self.price
                Machine.selected_items.remove(self)

    selected_items = List[Item]
    items = Dict[Item, int]
    total = int()

    def __init__(self, items: Dict[Item, int], cash: dict):
        self.total = 0
        self.items = items
        self.cash = cash
        self.balance = sum(self.cash.values())

    # def select_item(self, item: Item):
    #     if item in self.items.keys() and self.items[item] > 0:
    #         self.items[item] -= 1
    #         self.total += item.price
    #         self.selected_items.append(item)

    # def unselect_item(self, item: Item):
    #     if item in self.selected_items:
    #         self.items[item] += 1
    #         self.total -= item.price
    #         self.selected_items.remove(item)

    def buy_items(self, selected_items: List[Item]):
        return_cash = 0
        for selected_item in selected_items:
            self.total += selected_item.price

        return selected_items, return_cash

