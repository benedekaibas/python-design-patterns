"""We configure our own laptop using the builder pattern structure."""


class Computer:
    def __init__(self, serial_number: str) -> None:
        self.serial_number = serial_number
        self.memory = None
        self.hdd = None
        self.cpu = None
    
    def __str__(self) -> None:
        