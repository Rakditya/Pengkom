# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 18 April 2024

def non_zero(matrix,m,n):
    for i in range(n):
        if matrix[m][i]==1:
            return True
    return False

def zero(matrix,m,n):
    for i in range(n):
        if matrix[m][i]!=0:
            return False
    return True

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# Inisialisasi matriks dengan nilai 0
matrix = [[0] * n for _ in range(m)]

# Input elemen matriks
for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input("Masukkan elemen matriks baris " + str(i+1) + " kolom " + str(j+1) + ": "))

valid=True
if not non_zero(matrix,0,n):
    valid=False
else:
    for i in range(1,m):
        if not non_zero(matrix,i,n):
            if not zero(matrix,i,n):
                valid=False
            elif not non_zero(matrix,i-1,n):
                valid=False
if valid:
    print("Matriks sudah sesuai dengan matriks yang diinginkan")
else:
    print("Matriks tidak sesuai dengan matriks yang diinginkan")