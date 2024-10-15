# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 18 April 2024

def header_nama(nama):
    print("Nama pengguna:", nama)

def tampil_makanan(array, n):
    for i in range(n):
        print(str(i+1) + ". " + array[i])

nama_pengguna = input("Masukkan nama pengguna: ")
banyak_makanan = int(input("Masukkan banyaknya makanan favorit: "))
arr = ["*" for i in range (banyak_makanan)]
for i in range(banyak_makanan):
    arr[i] = input("Masukkan makanan favorit ke-" + str(i+1) +": " )

header_nama(nama_pengguna)
print("Makanan favorit", nama_pengguna, "adalah:")
tampil_makanan(arr, banyak_makanan)
