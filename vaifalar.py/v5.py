import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(
    mashgulot,
    masofa,
    color="green",
    marker="o",
    linewidth=3
)

plt.title("Sport mashg'ulotlari")
plt.xlabel("Mashg'ulot")
plt.ylabel("Masofa (km)")

plt.grid(linestyle=":")
plt.show()

print("1. Sportchining yugurish masofasi umumiy hisobda oshgan.")
print("2. 3-mashg'ulotda masofa biroz kamaygan, keyin yana oshgan.")