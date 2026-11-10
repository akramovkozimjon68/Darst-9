import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, color="blue", marker="o", label="Guruh A")
plt.plot(testlar, guruh_b, color="red", marker="s", label="Guruh B")

plt.legend()
plt.title("Ikki guruh test natijalari")
plt.xlabel("Testlar")
plt.ylabel("Ballar")

plt.grid()
plt.show()

print("Guruh A jami:", sum(guruh_a))
print("Guruh B jami:", sum(guruh_b))

if sum(guruh_a) > sum(guruh_b):
    print("Guruh A natijasi yaxshiroq.")
else:
    print("Guruh B natijasi yaxshiroq.")