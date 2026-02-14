from computer import Computer

# Defines the ResaleShop class which manages an inventory of computers, so the shop can buy, sell and update their computer details

class ResaleShop:

## a constructor that initializes a resale shop and sets up it's inventory

    def __init__(self):
        self.inventory = []

## adds a computer to the shop's inventory

    def buy(self, computer):
        self.inventory.append(computer)

## Removes a computer from the inventory if it exists and if not the error message is printed

    def sell(self, computer):
    
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Error: Computer not found in inventory.")

## updates the operating system of a computer in the inventory and if its not there an error message is printed

    def update_operating_system(self, computer, new_operating_system: str):
        if computer in self.inventory:
            computer.update_operating_system(new_operating_system)
        else:
            print("Error: Computer not found in inventory.")

## updates the price of the computer in the inventory and if its not there an error message is printed

    def update_price(self, computer, new_price: int):
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Error: Computer not found in inventory.")

## Prints all computers currently in the shop's inventory

    def print_inventory(self):
        if self.inventory:
            for computer in self.inventory:
                print(
                    f"{computer.description} -- Processor Type: {computer.processor_type} "
                    f"Hard Drive Capacity: {computer.hard_drive_capacity} Memory: {computer.memory} "
                    f"Operating System: {computer.operating_system} Year Made: {computer.year_made} "
                    f"Price: {computer.price}"
                )
        else:
            print("No inventory to display.")
    

    ## Refurbishes a computer in the inventory by updating its price and optionally its OS.
    
    def refurbish(self, computer, new_os=None):
        if computer in self.inventory:
            year = computer.year_made

            if year < 2000:
                computer.price = 0
            elif year < 2012:
                computer.price = 250
            elif year < 2018:
                computer.price = 550
            else:
                computer.price = 1000

            if new_os is not None:
                computer.update_operating_system(new_os)
        else:
            print("Computer not found. Please select another item to refurbish.")



