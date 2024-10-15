# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 5 Oktober 2023
# Nama Program : <>
# Spesifikasi Program : 

# KAMUS
# x : int
# y : int


# ALGORITMA
# Input
x = int(input("Masukkan X: "))
y = int(input("Masukkan Y: "))


# Inisialisasi
a = 1
b = 0

# Proses
for i in range (x):
    if(a % y != 0):
        print(a, end = " ")
        a += 1 
        if(a % y == 0):
            while (a != 1):
                a -= 1
                print((a - 1), end = " ")

    else:
        print(a)
        a += 1