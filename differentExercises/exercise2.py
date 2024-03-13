import numpy as np
from collections import Counter


def main(n: int, k: int, N: int) -> float:
    """
    Zu simulieren sind N-Mal k Zufallszahlen in {1,..., n} und zählen wie oft man k voneinander verschiedene Zahlen
    erhält.
    """
    sample = np.random.randint(low=n, size=(N, k))
    countDifferentNum = 0
    for i in range(N):
        countDifferentNum += (np.unique(sample[i]).shape[0] == k)
    result = countDifferentNum / N
    print("Die Wahrscheinlichkeit das in N sublisten mit k Elementen aus {{1,...n}} k voneinander verschiedene Zahlen"
          f"gezogen werden ist {result}")

if __name__ == "__main__":
    main(n=100, k=10, N=10000)
    # für größeres N nähert sich der Wert 0.629 an
