flag=True
while flag:
    ins = input('inserire un intero > 0: ')
    flag=False
    try:
        x = int(ins)
    except ValueError:
        print(ins, 'non e\' un intero!')
        flag=True
        continue
    if x<=0:
        print(ins, 'non e\' > 0!')
        flag=True

for i in ins:
    cifra=int(i)
    print(cifra, end=' ')
    for j in range(cifra):
        print('*', end='')
    print('')