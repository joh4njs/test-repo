import matplotlib.pyplot as plt

innbyggertall_danmark = [5.806015, 5.818553, 5.836339, 5.857510, 5.879197, 5.899107]
årstall = [2019, 2020, 2021, 2022, 2023, 2024]

plt.ylabel("Antall millioner innebyggere")
plt.xlabel("Årstall")
plt.title("Innbyggertall i Danmark fra 2019-2024")
plt.plot(årstall, innbyggertall_danmark, color = "red")
plt.show()