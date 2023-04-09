from Boot import System

class MainSystem(System):
    def __init__(self, sys_code: int = 1, codeName=None, Name="Main System") -> None:
        super().__init__(sys_code, codeName, Name)
    def onSystemInit(self):
        print("Hello, system world!")