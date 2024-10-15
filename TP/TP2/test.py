n = int(input("Masukkan nilai N: "))
current_number = 1

for i in range(1, n + 1):
    for j in range(i):
        if i <= n:
            print(current_number, end=" ")
            current_number += 1
    print()
