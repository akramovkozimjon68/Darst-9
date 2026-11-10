import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
natijalar = [10, 20, 15, 25, 30, 28, 35]

plt.plot(kunlar, natijalar, marker="o", color="green")

plt.title("Haftalik natijalar")
plt.xlabel("Kunlar")
plt.ylabel("Natijalar")

plt.grid()

plt.savefig("natija.png")
plt.show()