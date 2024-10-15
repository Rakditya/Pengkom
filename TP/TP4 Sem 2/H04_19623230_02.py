# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 18 April 2024

def cek_prima (n):
    if n <= 1:
        return False
    for i in range (2, (n//2)+1):
        if n % i == 0:
            return False
    return True
    
def maksimum (x, y):
    if x > y:
        return x
    else:
        return y
    
def faktor_prima_terbesar (x):
    max_factor = 0
    for i in range (2, x+1):
        if x % i == 0 and cek_prima (i):
            max_factor = maksimum(max_factor, i)
    return max_factor
    
def jumlah_faktor_prima (m, n):
    total = 0
    for i in range (m, n+1):
        total += faktor_prima_terbesar (i)
    return total

m = int(input("Masukkan nilai m : "))
n = int(input("Masukkan nilai n : "))
print("Jumlah faktor prima terbesar adalah", jumlah_faktor_prima (m, n))