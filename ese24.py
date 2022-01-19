while True:
    try:
        h = int(input('Altezza: '))
    except ValueError:
        print('non e\' un intero!')
        continue
    if h<1 or h>9:
        print('non e\' compreso tra 1 e 9!')
    else:
        break

for i in range(h):
    cont=1
    for j in range(h+i):
        if j<(h-i-1):
            print(' ', end='')
        elif j<(h-1):
            print(cont, end='')
            cont+=1
        else:
            print(cont, end='')
            cont-=1
    print('')