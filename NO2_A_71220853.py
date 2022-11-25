print ("==== Selamat datang di Toko Andi Tersenyum, selamat belanja ====")

p = int(input( "Total belanja :Rp. "))
q = p-p*2/100
r = p-p*5/100
s = p-(p*10/100)

if p >= 1000000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", s)
elif p >= 500000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", r)
elif p >= 100000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", q)
else :
    print (" Tidak ada diskon ! Maka yang anda bayarkan adalah : ", p)



    

