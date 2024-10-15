# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 21 September 2023
# Nama Program <Angka Spesial>
# Spesifikasi Program : Menentukan apakah angka yang didapat merupakan angka spesial atau tidak

# KAMUS
# n : int
# digit_1 : int
# digit_2 : int
# digit_3 : int
# digit_4 : int

# ALGORITMA
# Input
n = int(input("Masukkan Angka: "))
digit_1 = n // 1000
digit_2 = (n // 100) % 10
digit_3 = (n // 10) % 10
digit_4 = n % 10

# Proses
if((digit_1 * digit_4) % (digit_2 + digit_3) == 0):
    print(f"Angka", n, "adalah angka spesial")
else:
    print(f"Angka", n, "bukan angka spesial")