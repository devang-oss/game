class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = {}

    def add_item(self, item, quantity=1):
        if self.is_full():
            raise Exception("Inventory is full!")
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]
        else:
            raise Exception("Item not found in inventory!")

    def has_item(self, item):
        return item in self.items

    def get_items(self):
        return self.items.copy()

    def count_items(self):
        return sum(self.items.values())

    def is_full(self):
        return self.count_items() >= self.capacity

    def clear(self):
        self.items.clear()

    def get_space_remaining(self):
        return self.capacity - self.count_items()

    def to_dict(self):
        return self.items

    @classmethod
    def from_dict(cls, items_dict, capacity):
        inventory = cls(capacity)
        inventory.items = items_dict
        return inventory
