# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 27 Februari 2024
# Deskripsi : Menentukan berapa banyak level tiap kategorinya dan menentukan apakah target 2 level mudah dan 1 level sulit tercapai.

# Kamus
# main_1 : int
# finish_1 : int

# Algoritma

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

# Proses
if((finish_1 / main_1 * 100) >= 80):
    mudah = 1
    sulit = 0
    sedang = 0
    if((finish_2 / main_2 * 100) >= 80):
        mudah += 1
    elif((finish_2 / main_2 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_3 / main_3 * 100) >= 80):
        mudah += 1
    elif((finish_3 / main_3 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_4 / main_4 * 100) >= 80):
        mudah += 1
    elif((finish_4 / main_4 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_5 / main_5 * 100) >= 80):
        mudah += 1
    elif((finish_5 / main_5 * 100) < 30):
        sulit += 1
    else:
        sedang += 1
elif((finish_1 / main_1 * 100) < 30):
    mudah = 0
    sulit = 1
    sedang = 0
    if((finish_2 / main_2 * 100) >= 80):
        mudah += 1
    elif((finish_2 / main_2 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_3 / main_3 * 100) >= 80):
        mudah += 1
    elif((finish_3 / main_3 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_4 / main_4 * 100) >= 80):
        mudah += 1
    elif((finish_4 / main_4 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_5 / main_5 * 100) >= 80):
        mudah += 1
    elif((finish_5 / main_5 * 100) < 30):
        sulit += 1
    else:
        sedang += 1
else:
    mudah = 0
    sulit = 0
    sedang = 1
    if((finish_2 / main_2 * 100) >= 80):
        mudah += 1
    elif((finish_2 / main_2 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_3 / main_3 * 100) >= 80):
        mudah += 1
    elif((finish_3 / main_3 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_4 / main_4 * 100) >= 80):
        mudah += 1
    elif((finish_4 / main_4 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

    if((finish_5 / main_5 * 100) >= 80):
        mudah += 1
    elif((finish_5 / main_5 * 100) < 30):
        sulit += 1
    else:
        sedang += 1

# Output
print("Banyak level mudah sebanyak,", mudah, "level sedang sebanyak", sedang, "dan level sulit sebanyak", sulit)
      
if(mudah >= 2 and sulit >= 1):
    print("Target berhasil dicapai")
else:
    print("Target gagal dicapai")