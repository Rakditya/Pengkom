a = int(input("Masukkan target jumlah: "))
deret = 1
jml = deret
count = 1

while a > jml:
    count = count + 1
    deret = deret * 10 + (deret % 10 + 1)
    jml = jml + deret

print("Suku terakhir adalah", deret, "dengan jumlah", count, "suku pertama adalah", jml)
