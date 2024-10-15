# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 19 Oktober 2023
# Nama Program <Tulisan Komi>
# Spesifikasi Program : Memeriksa apakah tulisan Komi sudah benar atau belum

# KAMUS
# n : int
# m : int
# awal : str
# list_awal : chr
# akhir : str
# list_akhir : chr
# sesuai : boolean

# ALGORITMA
# Input
x = 0
n = int(input("Masukkan panjang kata asli: "))
awal = input("Masukkan kata asli: ")
m = int(input("Masukkan panjang kata yang ditulis: "))
akhir = input("Masukkan kata yang ditulis: ")
sesuai = True

akhir_sebenar = ["x" for k in range (n)]

k = 0
for i in range (n):
    print("")
    for j in range(i+1):
        print(awal[j], end="")
        akhir_sebenar[k] = awal[j]
        k += 1

if akhir_sebenar == akhir:
    print("Tulisan Komi sudah benar.")
else:
    print("Tulisan Komi masih salah")
