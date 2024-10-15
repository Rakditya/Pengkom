# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 2 November 2023
# Nama Program <Matriks Nona Deb>
# Spesifikasi Program : Membuat matriks baru yang merupakan hasil penjumlahan elemen-elemen di sekitar matriks awal

# KAMUS
# m : int
# n : int
# arr_awal : int
# arr_akhir : int
# batasbaris : int
# bataskolom : int

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))     # Menerima input banyak baris matriks   
n = int(input("Masukkan nilai n: "))     # Menerima input banyak kplom matriks
arr_awal = [[0 for j in range(n)] for i in range(m)]        # Inisialisasi matriks awal berisi 0 untuk semua elemen
arr_akhir = [[0 for j in range(n)] for i in range(m)]       # Inisialisasi matriks akhir berisi 0 untuk semua elemen

for i in range(m):
    for j in range(n):
        arr_awal[i][j] = int(input("Masukkan elemen matriks baris " + str(i + 1) + " kolom " + str(j + 1) + ": "))
        # Menerima input elemen matriks awal

# Proses
batasbaris = m-1    # Inisialisasi batas baris agar pengulangan tidak keluar dari indeks
bataskolom = n-1    # Inisialisasi batas kolom agar pengulangan tidak keluar dari indeks
for i in range (m):
    for j in range(n):
        if i == 0 and j == 0:
            arr_akhir[i][j] = arr_awal[i][j+1] + arr_awal [i+1][j]
        elif i == batasbaris and j == 0:
            arr_akhir[i][j] = arr_awal[i][j+1] + arr_awal [i-1][j]
        elif i == 0 and j == bataskolom:
            arr_akhir[i][j] = arr_awal[i][j-1] + arr_awal [i+i][j]
        elif i == batasbaris and j == bataskolom:
            arr_akhir[i][j] = arr_awal[i][j-1] + arr_awal [i-1][j]
        # Jika elemen matriks ada di sudut, maka hanya akan ditambahkan 2 elemen saja
        elif i == 0:
            arr_akhir[i][j] = arr_awal[i][j-1] + arr_awal [i+1][j] + arr_awal[i][j+1]
        elif i == batasbaris:
            arr_akhir[i][j] = arr_awal[i][j-1] + arr_awal [i-1][j] + arr_awal[i][j+1]
        elif j == 0:
            arr_akhir[i][j] = arr_awal[i-1][j] + arr_awal [i+1][j] + arr_awal[i][j+1]
        elif j == bataskolom:
            arr_akhir[i][j] = arr_awal[i-1][j] + arr_awal [i+1][j] + arr_awal[i][j-1]
        # Jika elemen matriks ada di sisi-sisi luar, akan ditambahkan 3 elemen
        else:
            arr_akhir[i][j] = arr_awal[i-1][j] + arr_awal [i+1][j] + arr_awal[i][j-1] + arr_awal[i][j+1]
        # Jika elemen matriks ada di tengah-tengah, akan ditambahkan 4 elemen

# Output
for i in range (m):
    for j in range (n):
        print(arr_akhir[i][j], end=" ") # Menampilkan matriks akhir
    print()