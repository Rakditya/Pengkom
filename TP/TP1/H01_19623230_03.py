# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal: 14 September 2023
# Program <Tipe dan Harga Tiket>
# Spesifikasi : Menentukan kelas dan harga tiket

# KAMUS
# Nomor_Kursi = int
# Posisi_Kursi = str
# status = str
# harga = int

# ALGORITMA

# Input
Nomor_Kursi = int(input('Masukkan Nomor Kursi: ')) # Memasukkan input data nomor kursi
Posisi_Kursi = (input('Masukkan Posisi Kursi: ')) # Memasukkan input data posisi kursi

# Proses
if(Nomor_Kursi >=1 and Nomor_Kursi <=20) or (Nomor_Kursi >=51 and Nomor_Kursi <=60):
    status = "Hot Seat"
else: # Nomor_Kursi >= 21 and Nomor_Kursi <=50 or Nomor_Kursi >=61 and Nomor_Kursi <=100
    status = "Reguler" # Menentukan kelas tiket yang dipilih

if(status == "Hot Seat"):
    if(Posisi_Kursi == "A" or Posisi_Kursi == "F"):
        harga = 1600000
    elif(Posisi_Kursi == "B" or Posisi_Kursi == "E"):
        harga = 1550000
    else:
        harga = 1500000
else:
    if(Posisi_Kursi == "A" or Posisi_Kursi == "F"):
        harga = 1000000
    elif(Posisi_Kursi == "B" or Posisi_Kursi == "E"):
        harga = 950000
    else: # Posisi_Kursi == "C" or Posisi_Kursi == "D"
        harga = 900000 # Menentukan harga tiket yang dipilih

# Output

print('Tuan Kil memilih kursi', status, "dengan harga", harga) # Menampilkan hasil kelas dan harga tiket
print()
print('Program Selesai')