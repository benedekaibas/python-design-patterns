"""Builder-pattern template for Apple factory."""

AppleMacbookPro = "Apple Macbook Pro 13'' 2017"


class MacbookFactory:
    class MacbookPro:
        def __init__(self) -> None:
            self.memory = 16
            self.hdd = 500 
            self.cpu = 3.1
        
        def __str__(self) -> None:
            specs = (
                f'Model: {AppleMacbookPro}',
                f'Memory: {self.memory}',
                f'HDD: {self.hdd}',
                f'CPU: {self.cpu}'
            )
            return '\n'.join(specs)
        
    def buildLaptop(self, model: str) -> None:
        if model == AppleMacbookPro:
            return self.MacbookPro()
        else:
            return f"I am not sure how to build this {model} laptop!"

if __name__ == "__main__":
    macbookBuild = MacbookFactory()
    macbookPro = macbookBuild.buildLaptop(AppleMacbookPro)
    print(macbookPro)