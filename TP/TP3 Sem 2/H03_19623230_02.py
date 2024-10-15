bnyk = int(input("Masukkan nilai banyak data: "))
arr = ["0" for j in range(bnyk)]

for i in range(bnyk):
    arr[i] = int(input("Masukkan data ke-" + str(i+1) + ": "))

target_nilai = int(input("Masukkan nilai yang dicari: "))
target_posisi = int(input("Masukkan nilai N: "))
count = 0
i = 0  
while i < bnyk and count < target_posisi:
    if arr[i] == target_nilai:
        count += 1
        posisi = i
    i += 1  

if count < target_posisi:
    print("Tidak cukup nilai", target_nilai, "ditemukan.")
else:
    print("Nilai", target_nilai, "ke-" + str(target_posisi), "berada pada indeks", posisi, ".")