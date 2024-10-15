# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 5 Oktober 2023
# Nama Program : <Pembagian Kegiatan>
# Spesifikasi Program : Menghitung banyak kegiatan di gedung A dan gedung B

# KAMUS
# n : int
# banyak_a : int
# banyak_b : int
# x : int
# y : int

# ALGORITMA
n = int(input("Masukkan nilai N: "))

# Inisialisasi
banyak_a = 0
banyak_b = 0
y = 1

# Proses
while (banyak_b < 3): 
        x = int(input(f"Masukkan peserta kegiatan ke-{y}: ")) # Menginput jumlah peserta kegiatan
        if (x < n):
            if(banyak_a < 5):
                banyak_a += 1       # Menjumlah kegiatan di A jika jumlah peserta kurang dari N dan jumlah kegiatan A kurang dari 5
            else:
                banyak_b += 1       # Menjumlah kegiatan di B jika jumlah kegiatan di A sudah 5 kegiatan
        else:
            banyak_b += 1           # Menjumlah kegiatan di B
        y += 1      

# Output
print("Terdapat", banyak_a, "kegiatan di gedung A dan", banyak_b, "kegiatan di gedung B.")