# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Program <Level Game>
# Spesifikasi : Menentukan berapa banyak level tiap kategorinya dan menentukan apakah target 2 level mudah dan 1 level sulit tercapai.

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

main_1 = int(input('Banyak pemain yang memainkan level 1: '))
finish_1 = int(input('Banyak pemain yang berhasil menyelesaikan level 1: '))
main_2 = int(input('Banyak pemain yang memainkan level 2: '))
finish_2 = int(input('Banyak pemain yang berhasil menyelesaikan level 2: '))
main_3 = int(input('Banyak pemain yang memainkan level 3: '))
finish_3 = int(input('Banyak pemain yang berhasil menyelesaikan level 3: '))
main_4 = int(input('Banyak pemain yang memainkan level 4: '))
finish_4 = int(input('Banyak pemain yang berhasil menyelesaikan level 4: '))
main_5 = int(input('Banyak pemain yang memainkan level 5: '))
finish_5 = int(input('Banyak pemain yang berhasil menyelesaikan level 5: '))
mudah = 0
sedang = 0
sulit = 0

persen_1 = finish_1/main_1 * 100
persen_2 = finish_2/main_2 * 100 
persen_3 = finish_3/main_3 * 100 
persen_4 = finish_4/main_1 * 100 
persen_5 = finish_5/main_5 * 100 

if(persen_1 >= 80):
  mudah += 1
elif(persen_1 < 30):
  sulit += 1
else:
  sedang += 1

if(persen_2 >= 80):
  mudah += 1
elif(persen_2 < 30):
  sulit += 1
else:
  sedang += 1

if(persen_3 >= 80):
  mudah += 1
elif(persen_3 < 30):
  sulit += 1
else:
  sedang += 1

if(persen_4 >= 80):
  mudah += 1
elif(persen_4 < 30):
  sulit += 1
else:
  sedang += 1

if(persen_5 >= 80):
  mudah += 1
elif(persen_5 < 30):
  sulit += 1
else:
  sedang += 1

print('Banyak level mudah sebanyak', mudah, 'level sedang sebanyak', sedang, 'dan level sulit sebanyak', sulit)

if(mudah == 2 and sulit == 1):
  print('Target berhasil dicapai.')
else:
  print('Target gagal dicapai.')