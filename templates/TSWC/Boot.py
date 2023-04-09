import uuid


# system construct
# define a function when the system loads (to be overridden) and
# a unique identifier.
class System:
    def __init__(self, sys_code: int = 0x01,
                codeName = None, Name = "A Regular System") -> None:
        self.name = Name
        self.code = sys_code

        self.uuid = uuid.uuid1().hex
        
        ## A codename
        ## Used when adding the system
        ## IF no codename is used, it will lower the name
        ## and remove the spaces.
        ## for example: the name "A Regular System"
        ## if no codename is specified it would default to
        ## aregularsystem

        self.codename = (codeName if codeName is not None else self.name.lower().replace(" ", ""))

    def onSystemInit(self):
        pass

# define a boot construct
# this contains a table with a dict
# the dict has [name] = SystemClass
# a regular table would look like
# [recovery] = Recovery(System)
# [dsh] = DSH(System) 
# (System) is the derivative.
class BootStruct:
    def __init__(self) -> None:
        self.systems: dict[str, System]
        self.systems = {}
        
    def add_system(self, sys: System):
        self.systems[sys.codename] = sys
    
    def run_system(self, name: str):
        if (self.systems.get(name) is not None):
            self.systems[name].onSystemInit();

    def get_systems(self) -> list[System]:
        return self.systems.values()
    
    def has_system(self, sysname: str) -> bool:
        return self.systems.get(str) != None
