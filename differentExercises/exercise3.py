"""
Y beschreibt einen Münzwurf -> Y=0 Kopf, Y=1 Zahl
Z ist uniform verteilt auf [-1,1]. Y und Z sind unabhängig
X = YZ = 0, falls Y=0 und Z, falls Y=1
N=1000 Durchgänge
"""

import random
import matplotlib.pyplot as plt


def main(N: int):
    x = []
    y = []
    z = []
    x_b_val = []
    empiric_val = []
    other_val = []
    for i in range(N):
        z.append(random.uniform(-1, 1))
        y.append(random.randint(0, 1))
        x.append(z[i] * y[i])

    plt.hist(z, density=True, bins=20)
    plt.show()
    plt.hist(x, density=True, bins=20)
    plt.show()

    x_b = -1
    for _ in range(N):
        x_b_val.append(x_b)
        empiric_val.append((sum(i <= x_b for i in x_b_val)) / N)
        x_b = round(x_b + 2 / N, len(str(N)) - 1)

    for x in x_b_val:
        result = 0
        if -1 <= x <= 0:
            result = (x + 1) / 4
        elif 0 < x <= 1:
            result = (x + 3) / 4
        other_val.append(result)

    plt.plot(x_b_val, empiric_val)
    plt.plot(x_b_val, other_val)
    plt.show()


if __name__ == "__main__":
    N = 1000
    main(N)
