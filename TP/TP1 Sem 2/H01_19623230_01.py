# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Program <Kecepatan Robot>
# Spesifikasi : Menentukan berapa detik robot tersebut tiba di tujuannya.

# KAMUS

# x1 = integer
# y1 = integer
# x2 = integer
# y2 = integer
# m = integer
# jarak = integer
# waktu = integer

# ALGORITMA

# Input
print('Masukkan koordinat awal robot')
x1 = int(input('X: ')) # Memasukkan input absis awal 
y1 = int(input('Y: ')) # Memasukkan input ordinat awal
print('Masukkan koordinat akhir robot')
x2 = int(input('X: ')) # Memasukkan input absis akhir
y2 = int(input('Y: ')) # Memasukkan input absis akhir
m = int(input('Masukkan nilai M: ')) # Memasukkan input data nilai M

# Proses
if(x1 < x2):
    if (y1 < y2):
        count = (x2 - x1) + (y2 - y1)
    else:
        count = (x2 - x1) + (y1 - y2)
else:
    if (y1 < y2):
        count = (x1 - x2) + (y2 - y1)
    else:
        count = (x1 - x2) + (y1 - y2)

waktu = (count * 1.5) / m

print('Robot akan tiba di tujuan setelah', waktu, 'detik')
