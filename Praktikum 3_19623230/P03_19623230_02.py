# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 19 Oktober 2023
# Nama Program <Potongan Prima>
# Spesifikasi Program : Mencari jumlah sub-elemen dimana jumlah dari sub-elemen tersebut prima

# KAMUS
# n : int
# angka : int
# total : int
# prima : boolean

# ALGORITMA
# Input
n = int(input("Masukkan nilai N: "))    # Memasukkan banyak nya angka 
angka = [0 for i in range (n)]          # Inisialisasi array angka
for i in range(n):
    angka[i] = int(input(f"Masukkan angka ke-{i+1}: "))     # Input angka sesuai user

count_prima = 0
prima = False

for i in range(n):
    if angka[i] <= 3 and angka > 0 and angka[i] != 1:
        prima = True
        count_prima += 1
    elif angka[i] > 3 and (angka[i] % 2) != 0 and (angka[i] % 3) != 0 and (angka[i] % 5) != 0 and (angka[i] % 7) != 0 and (angka[i] % 11) != 0 and (angka[i] % 13) != 0 and (angka[i] % 17) != 0:
        prima = True
        count_prima += 1
    else:
        prima = False

print(f"Terdapat {count_prima} potongan list yang jumlahnya prima") # Print hasil berapa bilangan prima yang ada
