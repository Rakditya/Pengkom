pnjgpsn = int(input("Masukkan panjang pesan: "))
psn = input("Masukkan pesan Tuan Kil: ")
c = input("Masukkan karakter pengganti spasi: ")
pesan = ["*" for i in range (pnjgpsn)]

for i in range (pnjgpsn):
    if psn[i] == c:
        pesan[i] = " "
    else:
        pesan[i] = psn[i]

for i in range (pnjgpsn):
    print(pesan[i], end="")