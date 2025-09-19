from computer import Computer
from oo_resale_shop import ResaleShop

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    shop = ResaleShop()
    
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 1999, 1500
    )

    
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    
    print("Buying", computer.description)
    item_id = shop.buy(computer)
    print()

    
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    
    new_OS = "MacOS Monterey"
    print(f"Refurbishing Item ID:{item_id}, updating OS to {new_OS}")
    shop.refurbish(item_id, new_OS)
    print("Done.\n")


    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    
    print(f"Selling Item ID: {item_id}")
    shop.sell(item_id)
    print()
    
    
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")


if __name__ == "__main__":
    main()
