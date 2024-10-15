# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Deskripsi : Menentukan apakah Tuan Kil memenuhi kebijakan tersebut.

# Kamus
# a : int
# peraturan_1 : bool

# Algoritma
# Input
a = int(input('Masukkan berat tas A: '))   # Memasukkan nilai untuk berat tas A
b = int(input('Masukkan berat tas B: '))
c = int(input('Masukkan berat tas C: '))
max_total = int(input('Masukkan batasan berat tas keseluruhan : '))
max_kabin = int(input('Masukkan batasan berat tas yang dibawa ke kabin: '))

# Proses

if((a + b + c) > max_total):
    peraturan_1 = True  
else:
    peraturan_1 = False

if(a > max_kabin and b > max_kabin and c > max_kabin):
    peraturan_2 = True
else:
    peraturan_2 = False

# Output
if(peraturan_1 and peraturan_2):
    print('Tuan Kil melanggar peraturan 1 dan 2 kebijakan maskapai.')
elif(peraturan_1):
    print('Tuan Kil melanggar peraturan 1 kebijakan maskapai.')
elif(peraturan_2):
    print('Tuan Kil melanggar peraturan 2 kebijakan maskapai.')
else:
    print('Tuan Kil memenuhi kebijakan maskapai.')