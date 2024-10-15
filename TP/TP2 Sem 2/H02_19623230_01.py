a = int(input("Masukkan banyak halaman buku: "))
b = int(input("Masukkan suatu bilangan: "))
jml = 0

for i in range(a+1):
    if i % b == 0:
        jml = jml + (i % 10)

print("Hasil penjumlahannya adalah", jml)