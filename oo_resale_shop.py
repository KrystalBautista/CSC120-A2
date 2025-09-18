from computer import *

class ResaleShop:

    
    def __init__(self):
        self.inventory = []
        self.next_id = 0
        

    def buy(self, computer:Computer):
        self.inventory.append(computer)
        item_id = self.inventory.index(computer)
        return item_id


    def sell(self, item_id: int):
        if 0 <= item_id < len(self.inventory) and self.inventory[item_id] is not None:
            self.inventory[item_id] = None
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")    


    def update_price(self, item_id:int, new_price:int):
        if 0 <= item_id < len(self.inventory) and self.inventory[item_id] is not None:
            self.inventory[item_id].update_price(new_price)
        else:
            print(f"Item {item_id} not found. Cannto update price.")




    def refurbish(self, item_id:int, new_os:str = None):
        if 0 <= item_id < len(self.inventory) and self.inventory [item_id] is not None:
            computer = self.inventory[item_id]
            computer.refurbish()
            if new_os:
                computer.update_os(new_os)
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")

    def print_inventory(self):
        for item_id, computer in enumerate(self.inventory):
            if computer is not None:
                print(f"Item ID: {item_id} : {vars(computer)}")
            else:
                print(f"Item {item_id} sold!")