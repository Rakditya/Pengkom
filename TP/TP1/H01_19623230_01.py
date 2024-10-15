# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 14 September 2023
# Program <Status Kelulusan>
# Spesifikasi : Menentukan Tuan Kil lulus atau tidak lulus

# KAMUS

# nilai_ujian_1 = float
# nilai_ujian_2 = float
# nilai_ujian_3 = float
# nilai_ujian_4 = float
# ratarata_nilai = float
# status = str

# ALGORITMA

# Input
nilai_ujian_1 = float(input('Masukkan nilai ujian 1: ')) # Memasukkan input data nilai ujian 1
nilai_ujian_2 = float(input('Masukkan nilai ujian 2: ')) # Memasukkan input data nilai ujian 2
nilai_ujian_3 = float(input('Masukkan nilai ujian 3: ')) # Memasukkan input data nilai ujian 3
nilai_ujian_4 = float(input('Masukkan nilai ujian 4: ')) # Memasukkan input data nilai ujian 4

# Proses
ratarata_nilai = (nilai_ujian_1 + nilai_ujian_2 + nilai_ujian_3 + nilai_ujian_4)/4 # Menghitung rata-rata nilai ujian

if(nilai_ujian_1 >=50 and nilai_ujian_2 >=50 and nilai_ujian_3 >=50 and nilai_ujian_4 >=50) and ratarata_nilai >=70:
    status = 'lulus'
else: # nilai_ujian_1 or nilai_ujian_2 or nilai_ujian_3 or nilai_ujian_4 <= 50 or ratarata_nilai >=70:
    status = 'tidak lulus' # Menentukan apakah Tuan Kil lulus/tidak lulus 

# Output
print ('Tuan kil', status, 'kelas Tuan Leo.')
print()
print('Program Selesai')