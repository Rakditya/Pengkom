# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 21 September 2023
# Nama Program <Menghitung Baju>
# Spesifikasi Program : Mmenghitung jumlah baju yang dapat dibuat berdasarkan kain dan pita yang tersedia
# jumlah_kain : int
# jumlah_pita : int
# sisa_kain : float
# sisa_pita : float
# jumlah_s : int
# jumlah_m : int
# jumlah_l : int

# ALGORITMA
# Input
jumlah_kain = int(input("Jumlah Kain : "))
jumlah_pita = int(input("Jumlah Pita : "))

# Proses
if(jumlah_kain >= 4.7 and jumlah_pita >= 3.1):
    jumlah_l = 1
    jumlah_m = 1
    jumlah_s = 1
else:
    print("Bahan tidak cukup untuk membuat baju.")
sisa_kain = jumlah_kain - 4.7
sisa_pita = jumlah_pita - 3.1
if(sisa_kain >=  2 and sisa_pita >= 1.3):
    if(sisa_kain < sisa_pita):
        jumlah_l += sisa_kain // 2
    else:
        jumlah_l += sisa_pita // 1.3
elif(sisa_kain >=  1.5 and sisa_pita >= 1):
    if(sisa_kain < sisa_pita):
        jumlah_m += sisa_kain // 1.5
    else:
        jumlah_m += sisa_pita // 1
elif(sisa_kain >=  1.5 and sisa_pita >= 1):
    if(sisa_kain < sisa_pita):
        jumlah_s += sisa_kain // 1
    else:
        jumlah_s += sisa_pita // 0.8
else:
    print()

if(sisa_kain >=  2 and sisa_pita >= 1.3):
    sisa_kain = sisa_kain - (sisa_kain // 2) * jumlah_l
    sisa_pita = sisa_pita - (sisa_pita // 1.3) * jumlah_l
elif(sisa_kain >=  1.5 and sisa_pita >= 1):
    sisa_kain = sisa_kain - (sisa_kain // 1.5) * jumlah_m
    sisa_pita = sisa_pita - (sisa_pita // 1) * jumlah_m
else:
    print()

if(sisa_kain >=  1.5 and sisa_pita >= 1):
    if(sisa_kain < sisa_pita):
        jumlah_m += sisa_kain // 1.5
    else:
        jumlah_m += sisa_pita // 1
else:
    if(sisa_kain < sisa_pita):
        jumlah_s += sisa_kain // 1
    else:
        jumlah_s += sisa_pita // 0.8

if(sisa_kain >=  1.5 and sisa_pita >= 1):
    sisa_kain = sisa_kain - (sisa_kain // 1.5) * jumlah_m
    sisa_pita = sisa_pita - (sisa_pita // 1) * jumlah_m
else:
    print()

if(sisa_kain >= 1 and sisa_pita >= 0.8):
    jumlah_s += sisa_kain // 1
else:
    jumlah_s += sisa_pita // 0.8

jumlah_s = int(jumlah_s)
jumlah_m = int(jumlah_m)
jumlah_l = int(jumlah_l)

print("Nona Deb dapat membuat", jumlah_s, "ukuran S,", 1 + jumlah_m, "ukuran M,", (1 + jumlah_l), "ukuran L.")
