# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 4 Maret 2024
# Spesifikasi Program : Menentukan berapa banyak peserta yang masuk kualifikasi dan hadiah yang didapatkan

# KAMUS

# ALGORITMA
# Input
n = int(input("Masukkan nilai N: "))
t = int(input("Masukkan nilai T: "))
leo = int(input("Masukkan waktu lari Tuan Leo: "))
deb = int(input("Masukkan waktu lari Nona Deb: "))
sal = int(input("Masukkan waktu lari Nona Sal: "))

# Proses
if leo <= t:
    qualified = 1
else:
    qualified = 0
if deb <= t:
    qualified = qualified + 1
else:
    qualified = qualified + 0
if sal <= t:
    qualified = qualified + 1
else:
    qualified = qualified + 0

hadiah = n // qualified

# Output
if qualified == 0:
    print('Tidak ada peserta yang terkualifikasi')
else:
    print("Terdapat", qualified, "peserta yang terkualifikasi dan masing -masing akan mendapatkan", hadiah,"dollar kompeng.") 