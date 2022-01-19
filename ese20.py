import sys

try:
    n = int(input('valore intero n: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()

for i in range(n):
    print('*', end='')
print('\nfinito')