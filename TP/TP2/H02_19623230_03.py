# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 September 2023
# Nama Program <Perkalian Selang-seling>
# Spesifikasi Program : Menentukan apakah sebuah bilangan dapat dicapai dengan mengalikan secara selang-seling
# KAMUS
# a : int
# b : int
# n : int
# num_1 : int
# num_2 : int
# sukses_a : boolean
#csukses_b : boolean

# ALGORITMA
# Input
a = int(input("Masukkan bilangan A: "))
b = int(input("Masukkan bilangan B: "))
n = int(input("Masukkan bilangan N: "))

# Inisialisasi
num_a = 1
num_b = 1
sukses_a = False
sukses_b = False


# Proses
while num_a < n: 
    num_a *= a
    if(num_a == n):
        sukses_a = True
    num_a *= b
    if(num_a == n):
        sukses_a = True # Terminasi

    # Kasus jika perkalian selang-seling dimulai dari bilangan A

if(sukses_a == False):
    while num_b < n: 
        num_b *= b
        if(num_b == n):
            sukses_b = True
        num_b *= a
        if(num_b == n):
            sukses_b = True # Terminasi

    # Kasus jika perkalian selang-seling dimulai dari bilangan B

if(sukses_a == True or sukses_b == True):
    print("Bilangan", n, "dapat dicapai.")
else:
    print("Bilangan", n, "tidak dapat dicapai.")