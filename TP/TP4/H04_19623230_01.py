# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 26 Oktober 2023
# Nama Program <Jumlah Maksimum>
# Spesifikasi Program : Menentukan jumlah maksimum submatriks berukuran 2 x 2 yang memiliki elemen ganjil.

# KAMUS
# baris : int
# kolom : int
# matriks : int
# jumlah : int
# max : int

# Algoritma
# Input
baris = int(input("Masukkan jumlah baris: ")) # Memasukkan jumlah baris dari matriks yang akan di cek
kolom = int(input("Masukkan jumlah kolom: ")) # Memasukkan jumlah kolom dari matriks yang akan di cek
matriks = [[0] * kolom for i in range(baris)] # Inisialisasi matriks dengan ukuran baris x kolom

print("Masukan elemen matriks") # Memberikan user arahan untuk menginput elemen dari matriks yang akan dicek
for i in range(baris):          
    for j in range(kolom):      
        matriks[i][j] = int(input(f"Masukan elemen matriks baris {i + 1} kolom {j + 1}: "))    # Mengupdate matriks yang awalnya berisi angka 0 semua sesuai input user

max = 0 # Inisialisasi jumlah maksimum dari submatriks yang diinginkan

# Proses
for i in range(baris - 1):          # Melakukan pengulangan sebanyak baris - 1 kali, sehingga program tidak mengecek indeks diluar input
    for j in range(kolom - 1):      # Melakukan pengulangan sebanyak kolom - 1 kali, sehingga program tidak mengecek indeks diluar input
        if (matriks[i][j] % 2 == 1) or (matriks[i + 1][j] % 2 == 1) or (matriks[i][j + 1] % 2 == 1) or (matriks[i + 1][j + 1] % 2 == 1):    # Mengecek apakah ada elemen ganjil di submatriks
            jumlah = matriks[i][j] + matriks[i + 1][j] + matriks[i][j + 1] + matriks[i + 1][j + 1]      # Menjumlahkan submatriks 2x2
            if jumlah > max:
                max = jumlah    # Mengubah nilai maksimum dengan jumlah submatriks yang dihitung jika nilai maksimum sementara lebih kecil dari jumlah submatriks yang dihitung 

# Output
if max != 0:            
    print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {max}")     # Menampilkan nilai maksimum jika nilai maksimum akhir berbeda dengan nilai maksimum inisialisasi
else:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")      # Menampilkan kalimat keterangan berikut saat tidak ada submatriks yang memenuhi (max == 0)