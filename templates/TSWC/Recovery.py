from Boot import BootStruct, System

class Recovery(System):
    def __init__(self, sys_code: int = 0) -> None:
        
        super().__init__(sys_code=sys_code,
                          Name="Recovery")
    
    def onSystemInit(self):
        print("Welcome to recovery! :)")
