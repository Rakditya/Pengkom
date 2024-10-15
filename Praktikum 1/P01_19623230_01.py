# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 21 September 2023
# Nama Program <Konversi Mata Uang>
# Spesifikasi Program : Mengonversi mata uang Peng dan Kom ke Rupiah dan memilih hasil yang lebih besar

# KAMUS
# Peng : int
# Kom : int
# Konv_Peng : int
# Konv_Kom : int

# ALGORITMA
# Input
Peng = int(input("Banyak uang Peng yang ditawarkan: "))
Kom = int(input("Banyak uang Kom yang ditawarkan: "))
Konv_Peng = Peng * 1000
Konv_Kom = Kom * 5000
print("Konversi mata uang Peng ke rupiah:", Konv_Peng)
print("Konversi mata uang Kom ke rupiah:", Konv_Kom)

if(Konv_Peng > Konv_Kom):
    print("Adik Tuan Kil memilih uang Peng")
elif(Konv_Peng == Konv_Kom):
    if(Peng >  Kom):
        print("Adik Tuan Kil memilih uang Peng")
    else:
        print("Adik Tuan Kil memilih uang Kom")
else:
        print("Adik Tuan Kil memilih uang Kom")

# Proses
