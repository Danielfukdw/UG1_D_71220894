print ('================================ KASIR ================================')
harga = int (input('Harga Barang :'))
k = input('Apakah anda membeli barang lagi? [yes/no] :')


if k == ('yes'):
    x = int(input('Harga Barang :'))
    y =harga + x
    print (y)
elif k == ('no'):
    print ('Total Belanja :',)
else :
    print (" INVALID")
