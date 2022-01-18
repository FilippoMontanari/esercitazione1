import sys

try:
    num1 = int(input('Inserire primo numero intero: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()

try:
    num2 = int(input('Inserire secondo numero intero: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
try:
    num3 = int(input('Inserire terzo numero intero: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()

print('maggiore:')
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
    
print('minore:')
if num1<num2 and num1<num3:
    print(num1)
elif num2<num1 and num2<num3:
    print(num2)
else:
    print(num3)
    
print('media aritmetica:')
somma = num1+num2+num3;
print(somma/3.0)

print('radice della somma:')
if somma<=0:
    print('La somma non e\' > 0!')
else:
    print(somma**0.5)