def addToInventory(inventory, addedItems):
    total_items = 0
    for k in dragonLoot:
        if (inventory.get(k, 0) == 0):
            inventory[k] = 1
        else:
            inventory[k] += 1
    for v in inventory.values():
        total_items += v
    return inventory, total_items

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv, total_items = addToInventory(inv, dragonLoot)
print(inv, '\n','Total number of items:', total_items)
