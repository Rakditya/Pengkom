# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 4 Maret 2024
# Spesifikasi Program : Menentukan berapa banyak peserta yang masuk kualifikasi dan hadiah yang didapatkan

# KAMUS

# ALGORITMA
# Input
penumpang = int(input('Jumlah penumpang (orang): '))
penggunaan = int(input('Lama penggunaan (jam): '))
supir = input('Apakah menggunakan supir (Ya atau Tidak): ')

if(penumpang <= 4):
    mobil_a = 1
    bayar = 450
    if(penggunaan > 12):
        bayar = (penggunaan - 12) * 50
        if(supir == "Ya"):
            bayar = bayar + penggunaan * 15
        else:
            bayar = bayar + 0
    if(supir == "Ya"):
            bayar = bayar + penggunaan * 15
    else:
     bayar = bayar + 0
elif(penumpang <= 8):
  mobil_b = 1
  bayar = 700
  if(penggunaan > 12):
    bayar = (penggunaan - 12)*80
    if(supir == "Ya"):
       bayar = bayar + penggunaan * 15
    else:
       bayar = bayar + 0
  if(supir == "Ya"):
            bayar = bayar + penggunaan * 15
  else:
     bayar = bayar + 0
else:
   mobil_b = penumpang // 8
   bayar = (penumpang // 8) * 700
   if((penumpang % 8) >= 5):
     mobil_b = mobil_b + 1
     bayar = bayar + 700
     if(penggunaan > 12):
        bayar = (penggunaan - 12) * 80 * (penumpang // 8 + 1)
        if(supir == "Ya"):
         bayar = bayar + (penggunaan * 15)
        else:
         bayar = bayar + 0
     if(supir == "Ya"):
            bayar = bayar + penggunaan * 15
     else:
        bayar = bayar + 0
   else:
     mobil_a = 1
     bayar = bayar + 450
     if(penggunaan > 12):
        bayar = (penggunaan - 12) * 80 * (penumpang // 8) + (penggunaan - 12) * 50
        if(supir == "Ya"):
         bayar = bayar + penggunaan * 15
        else:
         bayar = bayar + 0
     if(supir == "Ya"):
            bayar = bayar + penggunaan * 15
     else:
        bayar = bayar + 0

# Output
if(mobil_a == 1):
   print("Tuan Leo akan memesan 1 buah mobil A dengan total harga", bayar,"ribu.")
elif(mobil_b == 1):
   print("Tuan Leo akan memesan 1 buah mobil B dengan total harga", bayar,"ribu.")
else:
   print("Tuan Leo akan memesan", mobil_a, "buah mobil A dan", mobil_b, "buah mobil B dengan total harga", bayar,"ribu.")