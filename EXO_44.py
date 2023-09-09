"""
- Soit l'image suivante: https://imgur.com/a/if5RzBY
- Pouvez vous l'interpreter ?
- A l'aide de mpl, tracer l'histogramme des données suivantes:
x = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4]
"""
import matplotlib.pyplot as plt

x = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4]
plt.hist(x)
plt.title("Histogramme")
plt.show()
