# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Program <Bagasi Pesawat>
# Spesifikasi : Menentukan apakah Tuan Kil memenuhi kebijakan maskapai penerbangan.
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
a = int(input('Masukkan berat tas A: '))
b = int(input('Masukkan berat tas B: '))
c = int(input('Masukkan berat tas C: '))
max_tot = int(input('Masukkan batasan berat tas keseluruhan:  '))
max_cab = int(input('Masukkan batasan berat tas yang dibawa ke kabin:  '))
langgar_1 = False
langgar_2 = False

if(a + b + c > max_tot):
  langgar_1 = True
else:
  langgar_1 = False

if(a > max_cab and b > max_cab and c > max_cab):
  langgar_2 = True
else:
  langgar_2 = False

if(langgar_1 and langgar_2):
  print('Tuan Kil melanggar peraturan 1 dan 2 kebijakan maskapai')
elif(langgar_1):
  print('Tuan Kil melanggar peraturan 1 kebijakan maskapai')
elif(langgar_2):
  print('Tuan Kil melanggar peraturan 2 kebijakan maskapai')
else:
  print('Tuan Kil memenuhi kebijakan maskapai')