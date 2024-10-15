# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 2 November 2023
# Nama Program <Cek Skakmat>
# Spesifikasi Program : k mengidentifikasi apakah pion Raja putih aman dari serangan pion Kuda hitam

# KAMUS
# m : int
# arr : str
# checkmate : boolean
# batasbaris : int
# bataskolom : int

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))     # Menerima input banyak baris dan matriks   
arr = [[" " for j in range(m)] for i in range(m)]        # Inisialisasi matriks awal berisi * untuk semua elemen

for i in range(m):
    for j in range(m):
        arr[i][j] = str(input("Masukkan elemen matriks ke-" + str(i + 1) + " " + str(j + 1) + ": "))
        # Menerima input elemen matriks

# Proses
checkmate = False       # Inisialisasi kondisi pion Raja selalu aman
bataskolom = m-1
batasbaris = m-1
for i in range(m):
    for j in range(m):
        if arr[i][j] == "K":
            while i < batasbaris and j < bataskolom:    # Membuat kondisi agar looping tidak keluar dari indeks
                if arr[i+2][j+1] == "R" or arr[i+2][j-1] == "R" or arr[i-2][j+1] == "R" or arr[i+2][j+1] == "R":
                    checkmate = True
    # Jika ditemukan pion Kuda hitam yang jika berpindah dengan formasi letter L ada di posisi pion Raja, maka pion Raja tidak aman

# Output
print("Hasil papan catur")
for i in range (m):
    for j in range (m):
        print(arr[i][j], end=" ")       # Menampilkan hasil papan catur
    print()
if checkmate:
    print("Raja tidak aman dari serangan kuda.")    # Jika checkmate benar, akan ditampilkan hasil bahwa raja tidak aman
else:
    print("Raja aman dari serangan kuda.")      # Jika checkmate tidak benar, akan ditampilkan hasil bahwa raja aman