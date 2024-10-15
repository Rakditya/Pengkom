# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 10 Oktober 2023
# Nama Program <Cek Kehadiran>
# Spesifikasi Program : Menentukan nomor-nomor perwakilan yang tidak mendatangi acara secara terurut naik

# KAMUS
# N : int
# M : int
# tabel : int
# perwakilan : int

# Algoritma
# Input
x = 0
N = int(input("Masukkan nilai N: ")) # Memasukkan input banyak orang yang diundang
M = int(input("Masukkan nilai M: ")) # Memasukkan input banyak orang yang hadir
undang = [0 for i in range (N)]     # Inisialisasi list orang yang diundang
for i in  range (N):
    undang [i] = i + 1              # Mengisi list orang yang diundang
datang = [0 for i in range (M)]     # Inisialisasi list orang yang hadir
for i in  range (M):
    datang[i] = int(input(f"Masukkan data ke-{i+1}: "))     # Mengisi list orang yang hadir sesuai input
absen = [0 for i in range (N-M)]     # Inisialisasi list orang yang tidak hadir
for i in range(N):
    hadir = False                    # Inisialisasi semua element pada array orang diundang dianggap tidak hadir
    j = 0
    while j < M:
        if undang[i] == datang[j]:   # Mengecek list array orang yang diundang dengan list kehadiran 
            hadir = True             # Jika element pada array orang diundang ada di array hadir, maka kehadiran diubah menjadi true
        j += 1                       # Menambah satu agar mengecek data selanjutnya di array orang yang hadir
    if hadir == False:
        absen[x] = undang[i]         # Jika element pada array orang diundang tidak ada di array hadir, maka akan dimasukkan ke array baru
        x += 1                       # Menambah satu untuk mengubah nilai dari 0 ke element array orang diundang tidak ada di array hadir

print("Nomor perwakilan yang tidak datang:", end=" ")
for i in range(N-M):
    print(absen[i], end= " ")  # Print list orang yang tidak hadir