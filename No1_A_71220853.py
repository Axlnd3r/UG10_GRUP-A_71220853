nama = input(" Masukkan nama Mahasiswa : ")
Nim = str(input(" Masukkan Nim-nya : "))
c = int(Nim[2:4])
d = int (Nim [0:2])

if c== 20 or c== 21 or c== 22 and d==71 :
    print (nama, "Merupakan mahasiswa angkatan 20 hingga 22")
else : 
    print (nama, "bukan merupakan mahasiswa angkatan 20 hingga 22")
    
    

