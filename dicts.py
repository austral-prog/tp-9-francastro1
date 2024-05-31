def create_inventory(items):
    inventory = dict()
    for i in items:
        count = items.count(i)
        inventory[i] = count
    return inventory

def add_items(inventory, items):
    for i in set(items):
        count = items.count(i)
        if i in inventory:
            inventory[i] += count
        else:
            inventory[i] = count
    return inventory

def decrement_items(inventory, items):
    for i in items: 
        if i in inventory and inventory[i]>0:
            inventory[i] -= 1
        elif  i in inventory and inventory[i] < 0:
            inventory[i] = 0
    return inventory

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory

def list_inventory(inventory):
    lista = []
    for i, k in inventory.items():
        if k>0:
            tupla = (i,k)
            lista.append(tupla)
    return lista
