import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

plt.bar(mahsulotlar, sotuv, color="orange")

eng_kop = max(sotuv)
eng_kam = min(sotuv)

print("Eng ko'p sotilgan:", mahsulotlar[sotuv.index(eng_kop)])
print("Eng kam sotilgan:", mahsulotlar[sotuv.index(eng_kam)])

plt.title("Do'kon haftalik savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan mahsulotlar soni")

plt.show()