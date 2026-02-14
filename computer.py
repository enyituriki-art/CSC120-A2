# Defines the Computer class with attributes 

class Computer:
 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

## constructor that initializes a new computer object with all attributes
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):

        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

## updates the resale price of the computer
    def update_price (self , new_price : int):
       self.price = new_price

## updates the operating system of the computer
    def update_operating_system (self, new_operating_system : str):
       self.operating_system = new_operating_system


       
    
        