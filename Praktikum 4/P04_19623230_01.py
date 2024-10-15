# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 2 November 2023
# Nama Program <Nilai Praktikum>
# Spesifikasi Program :  Mengecek apakah bobot nilai valid dan menghitung nilai praktikum jika bobot valid

# KAMUS
# a : float
# b : float
# c : float
# Nilai1 : int 
# Nilai2 : int
# Nilai3 : int
# valid : boolean
# hasil : float

# ALGORITMA SUBPROGRAM CEKVALID
# KAMUS LOKAL
# x : float
# y : float
# z : float

def cekvalid(x, y, z):
    if x < 0 or y < 0 or z < 0 or (x + y + z != 1):  
        return False    # Jika bobot nilai ada yang negatif atau jumlahnya tidak sama dengan satu, maka bobot tidak valid
    else:
        return True     # Bobot valid jika jumlah sama dengan satu dan tidak ada yang negatif

# ALGORITMA SUBPROGRAM HITUNG
# KAMUS LOKAL
# x : float
# y : float
# z : float
# n1 : int
# n2 : int
# n3 : int

def hitung(x, y, z, n1, n2, n3):
    validitas = cekvalid(x, y, z)   # Mengecek validitas bobot
    if validitas == False:
        return print("bobot tidak valid")   # Jika bobot tidak valid, akan ditampilkan kalimat "bobot tidak valid"
    else:
        score = x * n1 + y * n2 + z * n3    # Menghitung nilai tugas praktikum
        return print(f"Nilai tugas praktikum adalah {int(score)}")  # Jika bobot valid, akan dihitung nilai tugas praktikum

# ALGORITMA UTAMA
# Input
a = float(input("Masukkan nilai a: "))      # Menerima input bobot soal 1
b = float(input("Masukkan nilai b: "))      # Menerima input bobot soal 2
c = float(input("Masukkan nilai c: "))      # Menerima input bobot soal 3
Nilai1 = int(input("Masukkan nilai soal 1: "))      # Menerima input nilai soal 1
Nilai2 = int(input("Masukkan nilai soal 2: "))      # Menerima input nilai soal 2
Nilai3 = int(input("Masukkan nilai soal 3: "))      # Menerima input nilai soal 3

# Output
hitung(a, b, c, Nilai1, Nilai2, Nilai3) # Menggunakan subprogram hitung untuk menampilkan hasil akhir dari nilai praktikum