m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
arr_awal = [[0 for j in range(n)] for i in range(m)]
arr_akhir = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        arr_awal[i][j] = int(input("Masukkan elemen matriks baris" + str(i + 1) + " kolom " + str(j + 1) + ": "))