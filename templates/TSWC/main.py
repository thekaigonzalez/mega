from Boot import BootStruct
from Recovery import Recovery
from MainSystem import MainSystem

boot = BootStruct()

recovery = Recovery() # called ' recovery ' in the run_system()
main = MainSystem()   # called ' mainsystem ' in the run_system()

boot.add_system(recovery)
boot.add_system(main)

boot.run_system("mainsystem")
# boot.run_system("recovery")

### The most basic usage of the system
### Mess around with boot.run_system
