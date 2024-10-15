# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 19 Oktober 2023
# Nama Program <Harga Minimal>
# Spesifikasi Program : Mengetahui berapa banyak uang yang harus dikeluarkan untuk makan di restoran selama 3 jam 

# KAMUS
# n : int
# harga : int

# ALGORITMA
# Input

n = int(input("Masukkan panjang kata asli: "))
awal = input("Masukkan kata asli: ")
m = int(input("Masukkan panjang kata yang ditulis: "))
akhir = input("Masukkan kata yang ditulis: ")

for i in range (n):
    print("")
    for j in range(i+1):
        print(awal[j], end='')