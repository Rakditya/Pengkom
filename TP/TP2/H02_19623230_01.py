# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 September 2023
# Nama Program <Cek Perpangkatan>
# Spesifikasi Program : Mengetahui apakah bilangan n merupakan bentuk perpangkatan bilangan k atau bukan

# KAMUS
# n : int
# k : int
# N : int

# ALGORITMA
# Input
n = int(input("Masukkan bilangan N: ")) #Input bilangan N
k = int(input("Masukkan bilangan K: ")) #Input bilangan K
N = n #Variabel untuk menyimpan input awal sebelum diproses dalam looping

# Proses
if k == 1:
    print(N, "bukan perpangkatan dari", k) # Nilai N tetap ketika k = 1
else:
    while n > 1 and n % k == 0: 
        n /= k                      # Selama N masih bisa dibagi K dan lebih dari 1, proses akan terus diulang
    if n == 1:
        print(N,"adalah perpangkatan dari", k) # N dapat di bagi K hingga mencapai 1
    else:
        print(N, "bukan perpangkatan dari", k) # N tidak dapat di bagi K hingga mencapai 1
