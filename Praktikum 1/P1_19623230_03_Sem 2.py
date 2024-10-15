# Nama : Raka Adhitya Nugraha
# NIM : 19623230
# Tanggal : 4 Maret 2024
# Spesifikasi Program : Menentukan berapa banyak peserta yang masuk kualifikasi dan hadiah yang didapatkan

# KAMUS

# ALGORITMA
# Input
mat = int(input('Nilai Matematika: '))
kim = int(input('Nilai Kimia: '))
fis = input('Nilai Fisika: ')
bio = input('Nilai Biologi: ')

if(mat > 90 and kim > 84 and fis > 86):
    print("Nona Deb dapat memilih Jurusan A.")
elif(mat > 85 and kim > 85 and fis > 80 and bio > 80):
    print("Nona Deb dapat memilih Jurusan B.") 
elif(((mat + fis + kim + bio)/4) > 78 and mat > 70 and bio > 70 and fis > 70 and kim > 85):
    print("Nona Deb dapat memilih Jurusan C.")
else:
    print("Nona Deb tidak dapat memilih di antara ketiga jurusan tersebut.")