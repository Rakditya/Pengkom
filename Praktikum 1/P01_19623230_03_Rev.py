jumlah_kain = int(input("Jumlah Kain : "))
jumlah_pita = int(input("Jumlah Pita : "))
kain_l = 2
kain_m = 1.5
kain_s = 1.2
pita_l = 1.3
pita_m = 1
pita_s = 0.8
sisa_kain = jumlah_kain - (kain_l + kain_m + kain_s)
sisa_pita = jumlah_pita - (pita_l + pita_m + pita_s)

if((sisa_kain > 0) and (sisa_pita > 0)):
    banyak_l = 1
    banyak_m = 1
    banyak_s = 1

if((sisa_kain // kain_l > 0) and (sisa_pita // pita_l > 0)):
    if((sisa_kain // kain_l) < (sisa_pita // pita_l)):
        banyak_l += (sisa_kain // kain_l)
    else:
        banyak_l += (sisa_pita // pita_l)
    sisa_kain = sisa_kain - (sisa_kain // kain_l) * kain_l
    sisa_pita = sisa_pita - (sisa_pita // pita_l) * pita_l
elif((sisa_kain // kain_m > 0) and (sisa_pita // pita_m > 0)):
    if((sisa_kain // kain_m) < (sisa_pita // pita_m)):
        banyak_m += (sisa_kain // kain_m)
    else:
        banyak_m += (sisa_pita // pita_m)
    sisa_kain = sisa_kain - (sisa_kain // kain_m) * kain_m
    sisa_pita = sisa_pita - (sisa_pita // pita_m) * pita_m
elif((sisa_kain // kain_s > 0) and (sisa_pita // pita_s > 0)):
    if((sisa_kain // kain_s) < (sisa_pita // pita_s)):
        banyak_s += (sisa_kain // kain_s)
    else:
        banyak_s += (sisa_pita // pita_s)
    sisa_kain = sisa_kain - (sisa_kain // kain_s) * kain_s
    sisa_pita = sisa_pita - (sisa_pita // pita_s) * pita_s
else:
    print("")


if((sisa_kain // kain_m > 0) and (sisa_pita // pita_m > 0)):
    if((sisa_kain // kain_m) < (sisa_pita // pita_m)):
        banyak_m += (sisa_kain // kain_m)
    else:
        banyak_m += (sisa_pita // pita_m)
    sisa_kain = sisa_kain - (sisa_kain // kain_m) * kain_m
    sisa_pita = sisa_pita - (sisa_pita // pita_m) * pita_m
elif((sisa_kain // kain_s > 0) and (sisa_pita // pita_s > 0)):
    if((sisa_kain // kain_s) < (sisa_pita // pita_s)):
        banyak_s += (sisa_kain // kain_s)
    else:
        banyak_s += (sisa_pita // pita_s)
    sisa_kain = sisa_kain - (sisa_kain // kain_s) * kain_s
    sisa_pita = sisa_pita - (sisa_pita // pita_s) * pita_s
else:
    print("")

if((sisa_kain // kain_s > 0) and (sisa_pita // pita_s > 0)):
    banyak_s += (sisa_kain // kain_s)
    sisa_kain = sisa_kain - (sisa_kain // kain_s) * kain_s
    sisa_pita = sisa_pita - (sisa_pita // pita_s) * pita_s

banyak_s = int(banyak_s)
banyak_m = int(banyak_m)
banyak_l = int(banyak_l)


print("Nona Deb dapat membuat", banyak_s, "ukuran S,", banyak_m, "ukuran M,", banyak_l, "ukuran L.")