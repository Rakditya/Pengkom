# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 10 Oktober 2023
# Nama Program <Nilai Terbesar>
# Spesifikasi Program : Menentukan nilai terbesar dalam array

# KAMUS
# B : int
# N : int

# Algoritma
B = int(input("Masukkan banyak data: "))  # Memasukkan input banyak data
N = int(input("Masukkan nilai N: "))      # Memasukkan input bilangan ke N terbesar yang ingin di cari
tabel = [0 for i in range(B)]             # Inisialisasi list 

for i in range(B):
    tabel[i] = int(input("Masukkan nilai ke-" + str(i + 1) + ": ")) # Mengisi list sesuai input user

for j in range(B - 1):
    for i in range(B - 1):
        if(tabel[i] < tabel[i + 1]):
            temp = tabel[i]
            tabel[i] = tabel[i + 1]
            tabel[i + 1] = temp         # Mengurutkan dari bilangan terbesar sampai bilangan terkecil


print("Nilai terbesar ke-" + str(N) + " adalah", tabel[N - 1]) # Print hasil