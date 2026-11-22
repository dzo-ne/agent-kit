STOCK = {}


def add_item(name, qty):
    STOCK[name] = STOCK.get(name, 0) + qty


def remove_item(name, qty):
    STOCK[name] = STOCK.get(name, 0) - qty
