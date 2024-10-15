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
n = int(input("Masukkan nilai N: ")) # Memasukkan nilai jumlah harga jam restorang Mokgnep
harga = [0 for i in range (n)]          # Inisialisasi array harga
for i in range(n):
    harga[i] = int(input(f"Masukkan harga jam ke-{i+1}: "))     # Input nilai harga sesuai user

total = [0 for k in range (n-2)]        # Inisialisasi harga total per 3 jam

# Proses
i = 0   # Inisialisasi indeks i pertama saat awal looping
j = 0   # Inisialisasi indeks j pertama saat awal looping

for j in range (n-2):      # Looping dibatasi hingga n-2. agar tidak dicari indeks n+2 yang mana akan menyebabkan error
        total[j] = harga[i] + harga[i+1] + harga[i+2]   # Mengisi harga total per 3 jam diisi
        j += 1              # Menambah j dengan 1 untuk mengisi indeks lainnya dalam list
        i += 1              # Menambah i dengan 1 untuk menjumlah harga 3 jam selanjutnya untuk input list harga total

min = total[0]              # Inisialisasi harga total minimal adalah harga 3 jam pertama
for j in range (n-2):
      if total[j] < min:
            min = total[j]  # Jika harga di list total ada yang dibawah harga 3 jam pertama, nilai tersebut akan menjadi nilai minimal

print(f"Total harga yang harus dibayar adalah {str(min)}") # Print harga minimal untuk makan di restoran selama 3 jam berturut-turut