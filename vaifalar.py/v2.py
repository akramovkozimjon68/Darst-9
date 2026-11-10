import matplotlib.pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 99, 72, 80, 88]

plt.bar(fanlar, ballar)

plt.title("Fanlardan olingan ballar")
plt.xlabel("Fanlar")
plt.ylabel("Ballar")

plt.show()