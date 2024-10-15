H = int(input("Masukkan nilai H: "))
nomor = 1

# Proses
if(H % 2 == 0):
    h = H // 2
else:
    h = H // 2 + 1

for i in range(1, h + 1):
    for j in range(1, i + 1):
        print(nomor, end=" ")
        nomor += 1
    print()

for i in range(h, 0, -1):
    for j in range(1, i + 1):
        print(nomor, end=" ")
        nomor += 1
    print()
