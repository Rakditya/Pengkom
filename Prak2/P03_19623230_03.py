# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 5 Oktober 2023
# Nama Program : <Piramida Bilangan>
# Spesifikasi Program : Membuat Piramida Bilangan 

# KAMUS
# p : int
# a : int


# ALGORITMA
# Input
p = int(input("Masukkan panjang piramida: "))
a = int(input("Masukkan selisih: "))

# Inisialisasi
x = 1

if(p > 75):
    p  = 75
else:
    if(p % 2 == 0):
        p = p - 1
    else:
        p = p

# Proses
for i in range(p):
    print("X"*(p - 1 - i), end= "")
    for j in range (p//2):
        if (x > 10):
            x % 10
        print(x)
        x += a
