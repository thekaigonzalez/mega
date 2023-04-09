# run like 
# python3 loaders/freeksd-sas/main.py please

from Info import check_and_ask
from Send import stringify
from Init import func_init

response = check_and_ask()

if (stringify(response) == 'F_OK'):
    func_init()