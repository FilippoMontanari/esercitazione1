import sys

try:
    mese = int(input('Inserire un valore tra 1 e 12: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()

if mese<1 or mese>12:
    print('Valore non valido!')
    sys.exit()
    
if mese<=3:
    print('Inverno')
elif mese<=6:
    print('Primavera')
elif mese<=9:
    print('Estate')
else:
    print('Autunno')