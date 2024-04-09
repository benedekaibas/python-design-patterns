"""We configure our own laptop using the builder pattern structure."""


class Computer:
    def __init__(self, serial_number: str) -> None:
        self.serial_number = serial_number
        self.memory = None
        self.hdd = None
        self.cpu = None
    
    def __str__(self) -> None:
        specs = (
            f'Memory: {self.memory}GB',
            f'HDD: {self.hdd}GB',
            f'CPU: {self.cpu}GHz'
            )
        return '\n'.join(specs)

class ComputerBuild:
    def __init__(self) -> None:
        self.computer = Computer("THIS IS A SERIAL NUMBER PLACEHOLDER!")
    
    def configure_memory(self, memory_size):
        self.computer.memory = memory_size
    
    def configure_hdd(self, hdd_size):
        self.computer.hdd = hdd_size

    def configure_cpu(self, cpu_performance):
        self.computer.cpu = cpu_performance

class HardwareConfigure:
    def __init__(self):
        self.build = None

    def computer_construct(self, memory, hdd, cpu):
        self.build = ComputerBuild()
        building_steps = (
            self.build.configure_memory(memory),
            self.build.configure_hdd(hdd),
            self.build.configure_cpu(cpu)
        )
        [step for step in building_steps]

    @property
    def computer(self):
        return self.build.computer

def main():
    configuration = HardwareConfigure()
    configuration.computer_construct(
        memory = 16,
        hdd = 500,
        cpu = 3.1
    )
    configured_computer = configuration.computer
    print(configured_computer)


if __name__ == "__main__":
    main()


