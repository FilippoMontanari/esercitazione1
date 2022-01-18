import sys

try:
    e = int(input('Inserire un numero (> 0): '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
if e<=0:
    print('Non e\' > 0!')
else:
    radice = e**0.5
    print('radice quadrata:', radice)

