# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 Oktober 2023
# Nama Program <Jumlah Pengkombackter>
# Spesifikasi Program : Menentukan jumlah pengkombacter setelah K detik.

# KAMUS
# n : int
# k : int
# detik : int
# jumlah : int
# baru : int

# Algoritma fungsi
def pengkombacter (n, k):
    detik = 0   # Inisialisasi waktu mula-mula t = 0
    jumlah = n  # Inisialisasi jumlah awal = n
    while detik < k:        # Melakukan pengulangan hingga detik k
        baru = 2 * jumlah      # Menghitung jumlah pengkombacter baru hasil reproduksi
        jumlah = n + baru       # Mengupdate jumlah total pengkombacter yang ada
        detik += 1      # Menambah waktu dengan 1 detik untuk melanjutkan pengulangan
    
    return(jumlah)

# Algoritma Utama
# Input
n = int(input("Masukkan N: ")) # Memasukkan jumlah Pengkombacter diawal
k = int(input("Masukkan K: ")) # Memasukkan durasi waktu bakteri bereproduksi

# Output
print(f"Terdapat {pengkombacter(n,k)} Bakteri Pengkombacter.")   