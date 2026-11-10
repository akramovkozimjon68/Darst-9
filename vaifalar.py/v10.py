import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="skyblue")

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

print("Eng yuqori ball:", eng_yuqori)
print("Eng yuqori ball egasi:", ismlar[ballar.index(eng_yuqori)])

print("Eng past ball:", eng_past)
print("Eng past ball egasi:", ismlar[ballar.index(eng_past)])

print("O'rtacha ball:", ortacha)

plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")

plt.grid(axis="y")

plt.savefig("oquvchilar_natijasi.png")
plt.show()

print("\n3 ta xulosa:")
print("1. Aziza eng yuqori natija ko'rsatdi.")
print("2. Sardor eng past natija ko'rsatdi.")
print("3. Sinfning o'rtacha bali 81.83 ga teng.")