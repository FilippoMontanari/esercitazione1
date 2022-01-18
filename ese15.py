import math

x1 = int(input('Inserire x1: '))
y1 = int(input('Inserire y1: '))
print('primo punto: (' + str(x1) + ', ' + str(y1) + ')')

x2 = int(input('Inserire x2: '))
y2 = int(input('Inserire y2: '))
print('secondo punto: (' + str(x2) + ', ' + str(y2) + ')')

dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print('distanza Euclidea:', dist)