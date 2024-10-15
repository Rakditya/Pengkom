# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 Oktober 2023
# Nama Program <Jumlah Kapal>
# Spesifikasi Program : Menghitung banyaknya kapal musuh yang ada.

# KAMUS
# N : int
# M : int
# input : int
# matriks : int
# jumlah : int
# bataskapalhorizontal : int
# bataskapalvertikal : int

# Algoritma
# Input
N = int(input("Masukkan N: ")) # Memasukkan jumlah baris dari matriks yang akan di cek
M = int(input("Masukkan M: ")) # Memasukkan jumlah kolom dari matriks yang akan di cek

print("Masukan peta:") # Memberikan user arahan untuk menginput elemen dari matriks yang akan dicek
input = [input() for n in range(N)]    # Memasukkan elemen matriks sesuai input user

matriks = [[int(input[n][m]) for m in range (M)] for n in range (N)] # Mengubah elemen matriks yang awalnya string menjadi integer

# Proses
jumlah = 0                  # Inisialisasi jumlah kapal di awal
for i in range(N):          # Melakukan pengulangan sebanyak baris - 1 kali, sehingga program tidak mengecek indeks diluar input
    for j in range(M):      # Melakukan pengulangan sebanyak kolom - 1 kali, sehingga program tidak mengecek indeks diluar input
        if (matriks[i][j] == 1):    # Mengecek apakah ada elemen dengan angka 1 di matriks
            jumlah += 1             # Menjumlahkan jumlah kapal yang ada di peta
            if (j) != (M - 1) and matriks[i][j + 1] == 1:   # Mengecek apakah di sebelah kanan elemen yang dicek bernilai 1
                bataskapalhorizontal = j + 1                # Mendekralasikan variabel batas kapal dimana nilai elemen sama dengan 1
                while (bataskapalhorizontal) != (M) and (matriks[i][bataskapalhorizontal] == 1):   # Melakukan pengulangan apabila indeks yang dicek masih dalam range dan bernilai 1
                    matriks[i][bataskapalhorizontal] = 0    # Mengubah nilai menjadi 0 agar tidak dihitung saat pengulangan utama
                    bataskapalhorizontal += 1               # Menambah batas kapal dengan 1 untuk mengecek elemen sebelah kanannya lagi
            elif (i) != (N - 1) and matriks[i + 1][j] == 1: # Mengecek apakah di sebelah bawah elemen yang dicek bernilai 1
                bataskapalvertikal = i + 1                  # Mendekralasikan variabel batas kapal dimana nilai elemen sama dengan 1
                while (bataskapalvertikal) != (N) and (matriks[bataskapalvertikal][j] == 1):       # Melakukan pengulangan apabila indeks yang dicek masih dalam range dan bernilai 1
                    matriks[bataskapalvertikal][j] = 0      # Mengubah nilai menjadi 0 agar tidak dihitung saat pengulangan utama
                    bataskapalvertikal += 1                 # Menambah batas kapal dengan 1 untuk mengecek elemen sebelah bawahnya lagi

# Output
if jumlah != 0:            
    print(f"Terdapat {jumlah} kapal musuh pada peta")     # Menampilkan jumlah kapal pada peta jika jumlah kapal akhir berbeda dengan jumlah kapal inisialisasi
else:
    print("Tidak terdapat kapal musuh pada peta")      # Menampilkan kalimat keterangan berikut saat tidak ada kapal pada peta (jumlah == 0)
            