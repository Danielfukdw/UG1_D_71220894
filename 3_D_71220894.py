x = int (input('Masukan Angka : '))
for y in range (x):
    print (' '*(x-y),'*'*(y*2+1))
for y in range (x-2,-1,-1):
    print (' '*(x-y),'*'*(y*2+1))