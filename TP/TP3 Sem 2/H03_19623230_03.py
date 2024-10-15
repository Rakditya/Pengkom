bnyk = int(input("Masukkan banyaknya elemen: "))
arr = ["0" for j in range(bnyk)]

for i in range(bnyk):
    arr[i] = int(input("Masukkan data ke-" + str(i+1) + ": "))

new_arr = [0 for j in range(bnyk)]

for i in range (bnyk):
    if i == 0:
        if arr[i] > arr[i+1]:
            new_arr[i] = arr[i]
        else:
            new_arr[i] = arr[i+1]
    elif i == (bnyk - 1):
        if arr[i] > arr[i-1]:
            new_arr[i] = arr[i]
        else:
            new_arr[i] = arr[i-1]
    else:
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            new_arr[i] = arr[i]
        elif arr[i-1] > arr[i+1] and arr[i-1] > arr[i]:
            new_arr[i] = arr[i-1]
        else:
            new_arr[i] = arr[i+1]

print("Kondisi Awal:", arr)
print("Kondisi Akhir:", new_arr)