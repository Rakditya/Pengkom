n = int(input("Masukkan N: ")) # Memasukkan jumlah Pengkombacter diawal
k = int(input("Masukkan K: ")) # Memasukkan durasi waktu bakteri bereproduksi

detik = 0   # Inisialisasi waktu mula-mula t = 0
jumlah = n  # Inisialisasi jumlah awal = n
while detik < k:        # Melakukan pengulangan hingga detik k
    baru = 2 * jumlah      # Menghitung jumlah pengkombacter baru hasil reproduksi
    jumlah = n + baru       # Mengupdate jumlah total pengkombacter yang ada
    detik += 1      # Menambah waktu dengan 1 detik untuk melanjutkan pengulangan

print(f"Terdapat {jumlah} Bakteri Pengkombacter.")   


"""
Buka Antarmuka Pengguna (Tkinter)
Tampilkan Judul dan Konfigurasi Layar
Inisialisasi Total dan Variabel Penanda Barang
Definisi Fungsi Harga(item)
    Tambahkan item ke Total
    Tambahkan penanda barang
    Perbarui tampilan Total
Definisi Fungsi Reset()
    Atur Total ke 0
    Kosongkan tampilan Total

Tampilkan Frame Jual dan Frame Barang
Tampilkan Label "RINCIAN BARANG" di Frame Barang
Tampilkan Kotak Teks untuk Rincian di Frame Barang

Tampilkan Label "TOTAL" di Frame Hasil
Tampilkan Kotak Teks untuk Total di Frame Hasil
Tampilkan Gambar Produk dan Label Harga di Frame Frame
Tampilkan Tombol "Purchase" dengan Fungsi Harga(5000)

Mulai Antarmuka Pengguna (root.mainloop())
"""