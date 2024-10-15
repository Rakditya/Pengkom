def cek_matriks(m, n, matriks):
    # Fungsi untuk memeriksa matriks
    for i in range(m):
        if matriks[i][0] == 0 and i != m-1 and matriks[i+1][0] != 0:
            return False
        for j in range(n):
            if matriks[i][j] != 0 and matriks[i][j-1] == 0 and matriks[i][j] != 1:
                return False
    return True

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
input = [input() for n in range(n)] 
matriks = [[(input[i][j]) for i in range (n)] for j in range (m)]

if cek_matriks(m, n, matriks):
    print("Matriks sudah sesuai dengan matriks yang diinginkan")
else:
    print("Matriks tidak sesuai dengan matriks yang diinginkan")