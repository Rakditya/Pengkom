# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 September 2023
# Nama Program <Segitiga Angkat>
# Spesifikasi Program : Membuat segitiga istimewa kembar tercermin sehingga membentuk sebuah segitiga sama kaki

# KAMUS
# h : int
# n : int

# ALGORITMA
# Input
H = int(input("Masukkan nilai H: ")) # Input tinggi segitiga

# Inisialisasi
n = 1

# Proses
if(H % 2 == 0):
    Hu = H // 2         # Menentukan tinggi bagian segitiga angka dengan yang terpendek diatas
    Hl = H // 2         # Menentukan tinggi bagian segitiga angka dengan yang terpendek dibawah
else:
    Hu = H // 2 + 1     # Menentukan tinggi bagian atas segitiga angka dengan yang terpendek diatas
    Hl = H // 2         # Menentukan tinggi bagian bawah segitiga angka dengan yang terpendek dibawah


for i in range(1, Hu+1):
    for j in range(1, i + 1):
        print(n, end=" ")
        n += 1
    print()                     # Terminasi, membeeri output segitiga angka bagian atas

for i in range(Hl, 0, -1):
    for j in range(1, i + 1):
        print(n, end=" ")
        n += 1
    print()                     # Terminasi, membeeri output segitiga angka bagian bawah
