flag=True
while flag:
    ins = input('valore intero n: ')
    flag=False
    try:
        n = int(ins)
    except ValueError:
        print(ins, 'non e\' un intero!')
        flag=True
        continue
    if n<=0:
        print(ins, 'non e\' > 0!')
        flag=True
    
for i in range(n):
    print('*', end='')
print('\nfinito')