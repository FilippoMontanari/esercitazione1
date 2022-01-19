# ese25, seguendo lo schema di soluzione proposto

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

temp=x
c=0 # numero di cifre del numero x
while temp>0:
    temp = temp//10 # divisione intera
    c+=1
    
acc=x

for i in range(c, 0, -1):
    cifra = acc//(10**(i-1)) # divisione intera: numero / la relativa potenza del 10
    print(cifra, end=' ')
    for j in range(cifra):
        print('*', end='')
    print('')
    acc = acc%(10**(i-1)) # resto della divisione per eliminare la cifra i-esima