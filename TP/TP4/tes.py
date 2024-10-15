baris = int(input("Masukkan jumlah baris: ")) # Memasukkan jumlah baris dari matriks yang akan di cek
kolom = int(input("Masukkan jumlah kolom: ")) # Memasukkan jumlah kolom dari matriks yang akan di cek

print("Masukan elemen matriks") # Memberikan user arahan untuk menginput elemen dari matriks yang akan dicek
input = [input().split() for b in range(baris)]    # Memasukkan elemen matriks sesuai input user

matriks = [[int(input[b][k]) for k in range (kolom)] for b in range (baris)] # Mengubah elemen matriks yang awalnya string menjadi integer


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
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")