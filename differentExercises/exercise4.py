"""
n = 10⁶ Paare (Ti, Ui) mit i = 1...n Zufallsvariablen die Exponentialverteilt sind.
T = min(X,Y) und U = 1_{X<Y}
"""

import numpy as np

"""
Aus dem Hinweis geht hervor, dass man den Gillespie-Algorithmus anwenden darf, um die Aufgabe zu lösen.
1. Simuliere X,Y und berechne T = min(X,Y), Falls X<Y sei P = p und ansonsten P = q. Simulieren U ~ B(n,P) und berichte T,U
2. Simuliere T ~ exp(mu + nu) und P, wobei P = p mit mu/(mu+nu) und annsonsten P = q. Simuliere B(n,p) und berichte (T,U)
"""


def gillespie_approach_one(mu: int, nu: int, n: int):
    X = np.random.exponential(scale=1 / mu, size=n)  # X ist exponentialverteilt
    Y = np.random.exponential(scale=1 / nu, size=n)  # Y ist exponentialverteilt
    T = np.minimum(X, Y)
    U = (X < Y)  # Indikatorfunktion U wird ausgewertet (Falls True = 1 ansonsten False = 0)
    return np.vstack((T, U))  # used to display the values in 2D. (rowwise)


def gillespie_approach_two(mu: int, nu: int, n: int):
    T = np.random.exponential(scale=1 / (mu + nu), size=n)  # nun ist T exponentialverteilt zu den Paramtern mu, nu
    U = np.random.random(size=n)
    U_res = (U < mu / (mu + nu))
    return np.vstack((T, U_res))  # used to display the values in 2D. (rowwise)


if __name__ == "__main__":
    n = 10 ** 6
    mu = 1
    nu = 2

    print(gillespie_approach_one(mu, nu, n))
    print(gillespie_approach_two(mu, nu, n))
