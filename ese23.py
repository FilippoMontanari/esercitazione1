import sys

try:
    a = int(input('Lato a: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
try:
    b = int(input('Lato b: '))
except ValueError:
    print('Non e\' un intero!')
    sys.exit()
    
for i in range(b):
    if i==0 or i==(b-1):
        rigaAll=True;
    else:
        rigaAll=False;
    for j in range(a):
        if rigaAll:
            print('*', end=' ')
        elif j==0 or j==(a-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')