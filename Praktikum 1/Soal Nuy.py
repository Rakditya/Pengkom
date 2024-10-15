# Input
lower_interval1 = int(input("Interval Awal Bilangan: "))
upper_interval1 = int(input("Interval Akhir Bilangan: "))
lower_interval2 = int(input("Interval Awal Bilangan: "))
upper_interval2 = int(input("Interval Akhir Bilangan: "))
lower_interval3 = int(input("Interval Awal Bilangan: "))
upper_interval3 = int(input("Interval Akhir Bilangan: "))


# Mencari batas bawah irisan

lower_bound = None
if lower_interval1 >= lower_interval2 and lower_interval1 >= lower_interval3:
    lower_bound = lower_interval1
elif lower_interval2 >= lower_interval1 and lower_interval2 >= lower_interval3:
    lower_bound = lower_interval2
else:
    lower_bound = lower_interval3

# Mencari batas atas irisan
upper_bound = None
if upper_interval1 <= upper_interval2 and upper_interval1 <= upper_interval3:
    upper_bound = upper_interval1
elif upper_interval2 <= upper_interval1 and upper_interval2 <= upper_interval3:
    upper_bound = upper_interval2
else:
    upper_bound = upper_interval3

# Memeriksa apakah ada irisan
if lower_bound > upper_bound:
    print("Tidak ada irisan antara ketiga interval")
else:
    print("Irisan antara ketiga interval:", (lower_bound, upper_bound))