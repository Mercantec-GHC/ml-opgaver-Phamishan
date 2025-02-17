import matplotlib.pyplot as plt
import numpy as np
data = [];

def CoinFlip(): 
    flip = np.random.randint(low=0,high=2, size=1)
    return flip[0]
flipamount = 0
plat = 0
totalFlip = 0
chance = 0
for x in range(100):
    for x in range(100):
        flip = CoinFlip()
        plat += flip
        flipamount += 1
        if flipamount == 100:
            chance = plat / (flipamount +(100 * totalFlip))
            data.append(chance)
            flipamount = 0
            print(totalFlip, " ", chance)
            totalFlip += 1

plt.figure(figsize=(5, 5))

plt.ylim(0.4, 0.6)
plt.title("Møntkast")
plt.xlabel("Antal af kast")
plt.ylabel("Sandsynlighed")

plt.plot(data,marker='o', color='r')

plt.show()