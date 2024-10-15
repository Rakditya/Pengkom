# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 10 Oktober 2023
# Nama Program <Rute Kereta>
# Spesifikasi Program : Menentukan stasiun tempat awal perjalanan dan banyaknya stasiun yang dikunjungi.

# KAMUS
# Uang : int
# Stasiun : int

# Algoritma
# Input
Uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))  # Memasukkan input banyak datuang uang Tuan Leo
Stasiun = int(input("Masukkan jumlah stasiun: "))          # Memasukkan input jumlah stasiun yang ada
harga = [0 for i in range(Stasiun)]                        # Inisialisasi list
Rute = [0 for i in range(Stasiun)]                         # Inisialisasi list

for i in range(Stasiun):
    harga[i] = int(input("Masukkan harga stasiun ke-" + str(i+1) + ": ")) # Mengisi list harga stasiun sesuai input user

for i in range(Stasiun):                                    # Loop untuk mengecek berapa stasiun yang bisa di kunjungi Tuan Leo jika dia memulai dari stasiun i
    j = i
    Bayar = 0                                              # Inisialisasi uang yang digunakan Tuan Leo
    while Bayar + harga[j] <= Uang and Rute[i] < Stasiun:
        Rute[i] += 1                                       # Mengisi list rute dengan jumlah stasius yang bisa dikunjungi
        Bayar += harga[j]                                  
        if j == Stasiun - 1:
            j = 0                                          # Jika algoritma mengecek dari tengah, dia akan loop kembali ke awal
        else:
            j += 1                                         

maksimal = 0                        # Inisialisasi jumlah rute maksimal
for i in range(Stasiun):            # Loop untuk mengecek dan mengubah nilai maksimal                   
    if(Rute[i] > maksimal):
        maksimal = Rute[i]
        urut = i + 1                # Menentukan awal mula rute yang ditempuh Tuan Leo

print(f"Tuan Leo dapat mengunjungi, {maksimal} stasiun dimulai dari stasiun ke -{urut}") # Print hasil