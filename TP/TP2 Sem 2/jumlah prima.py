cek_prima = True
num = int(input("Masukkan bilangan: "))
if num == 1:
    cek_prima = False
elif num == 2:
    cek_prima = True
else:
    while cek_prima:
        if num % i == 0:
            cek_prima = False
            i = num
        else:
            cek_prima = True

print(cek_prima)