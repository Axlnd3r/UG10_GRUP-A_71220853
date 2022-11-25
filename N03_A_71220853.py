P = int(input( " Masukkan nilai soal 1 : "))
Q = int(input (" Masukkan nilai soal 2 : "))
R = int(input(" Masukkan nilai soal 3 : "))
umur = int(input(" Masukkan umur Anda :"))

S = (P*(0.5)+ Q*(0.3)+ R*(0.2))
print ( "Rata-rata nilai Anda : ", S)

if umur > 25 and S >= 90:
           print ( " Selamat Anda lulus !")
elif umur <= 25 and S >= 80:
           print (" Selamat Anda lulus !")
else:
    print ("Coba lagi tahun depan!")


