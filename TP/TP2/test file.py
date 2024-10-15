
h = int(input("Masukkan bilangan h: "))  # Setel nilai n sesuai dengan tinggi segitiga yang diinginkan
current_number = 1
row = 1

while row <= h:
    for i in range(row):
        if current_number > h:
            print()
            row = h + 1
        else:
            print(current_number, end=" ")
            current_number += 1
    print()
    row += 1
