import sys

# **** mese ****
try:
    mese = int(input('Inserire mese (valore tra 1 e 12): '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
if mese<1 or mese>12:
    print('Valore non valido!')
    sys.exit()

# **** giorno ****    
try:
    giorno = int(input('Inserire giorno del mese: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
if giorno<1 or giorno>31:
    print('Valore non valido!')
    sys.exit()
    
if mese==2 and giorno>29:
    print('Valore non valido!')
    sys.exit()
elif mese in [4, 6, 9, 11] and giorno>30:
    print('Valore non valido!')
    sys.exit()

# **** stagione ****
if (mese==12 and giorno>=22) or mese<3 or (mese==3 and giorno<21):
    print('Inverno')
elif mese<6 or (mese==6 and giorno<21):
    print('Primavera')
elif mese<9 or (mese==9 and giorno<23):
    print('Estate')
else:
    print('Autunno')