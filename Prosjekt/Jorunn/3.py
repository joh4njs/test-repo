# Norge

import matplotlib.pyplot as plt

år = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
innbyggertall = [3,3,3,4,4,3,3,4,5,5]

plt.figure(facecolor='lavender')
ax = plt.axes()

ax.set_facecolor("lavender")

plt.plot(år, innbyggertall, color="purple")
plt.show()