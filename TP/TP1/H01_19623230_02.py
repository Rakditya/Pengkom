# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 14 September 2023
# Program <Gradien Garis>
# Spesifikasi : Menentukan tipe garis atau gradien garis tertentu.

# KAMUS
# X1 = int
# Y1 = int
# X2 = int
# Y2 = int
# rise = float
# run = float
# status = str

# ALGORITMA

# Input
X1 = int(input('Masukkan X1: ')) # Memasukkan input data titik X1
Y1 = int(input('Masukkan Y1: ')) # Memasukkan input data titik Y1
X2 = int(input('Masukkan X2: ')) # Memasukkan input data titik X2
Y2 = int(input('Masukkan Y2: ')) # Memasukkan input data titik Y2

# Proses
rise = Y2 - Y1
run = X2 - X1

if(Y2 == Y1):
    status = "merupakan garis horizontal."
elif(X2 == X1):
    status = "merupakan garis vertikal."
else: # Garis bergradien
    status = "memiliki gradien" # Menentukan tipe garis

if(status == "memiliki gradien"):
    gradien = rise/run # Menghitung gradien garis
else:
    gradien = "" 

# Output
print('Garis tersebut', status, gradien)
print()
print('Program Selesai')