# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Deskripsi : Menentukan berapa detik robot tersebut tiba di tujuannya

# Kamus
# x1 : int
# y1 : int
# x2 : int
# y2 : int
# m : int

# Algoritma

# Input
print('Masukkan koordinat awal robot')
x1 = int(input('x : '))  # Memasukkan input absis awal
y1 = int(input('y : '))  # Memasukkan input ordinat awal
print('Masukkan koordinat akhir robot')
x2 = int(input('x : '))  # Memasukkan input absis akhir
y2 = int(input('y : '))  # Memasukkan input ordinat akhir
m = int(input('Masukkan nilai M: '))  # Memasukkan input kecepatan rata-rata

# Proses
# jarak_x = (x1 - x2)
#if(jarak_x < 0):
#    jarak_x = jarak_x * (-1)
#else:
#    jarak_x = jarak_x * 1
#jarak_y = (y1 - y2)
#if(jarak_y < 0):
#    jarak_y = jarak_y * (-1)
#else:
#    jarak_y = jarak_y * 1

if(x1 < x2):
    if(y1 < y2):
        jarak_total = (x2 - x1) + (y2 - y1)
    else: # y1 > y2
        jarak_total = (x2 - x1) + (y1 - y2)
else:
    if(y1 < y2):
        jarak_total = (x1 - x2) + (y2 - y1)
    else: # y1 > y2
        jarak_total = (x1 - x2) + (y1 - y2)

waktu = jarak_total * 1.5 / m

# Output
print("Robot akan tiba di tujuan setelah", waktu, "detik.")