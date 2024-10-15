sum_prima = 0
count_ganjil = 0

while count_ganjil < 3:
    num = int(input("Masukkan bilangan: "))
    if num % 2 == 0:
        count_ganjil = 0
        if num == 2:
            sum_prima += num
    else:
        count_ganjil += 1
        if num == 1:
            sum_prima += 0
        else:
            not_prima = False
            i = 2
            while i < num:
                if num % i == 0:
                    not_prima = True
                    i += 1
                else:
                    i += 1
            if not_prima == False:
                sum_prima += num

print("Jumlah bilangan prima adalah", sum_prima)