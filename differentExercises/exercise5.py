"""
Übergangsmatrix
|0      .5      .5      0      0|
|.33    0       .33     .33    0|
|0      .5      0       0      .5|
|0      0       0       0       1|
|1      0       0       0       0|
"""

import numpy as np

"""
Wir erhalten die Verteilug von X_t durch t-faches multiplizieren der Übergangsmatrix
"""


def main():
    P = np.array([[0, .5, .5, 0, 0],
                  [.33, 0, .33, .33, 0],
                  [0, .5, 0, 0, .5],
                  [0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0]]
                 )
    init_dist = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # in the beginning we got the same probability for every entry in
    # the matrix which is 1/n in our case 1/5
    new_dist_100 = init_dist @ np.linalg.matrix_power(P, 100)  # multiply the array 100 times with it self
    new_dist_1000 = init_dist @ np.linalg.matrix_power(P, 1000) # multiply the array 1000 times with it self
    return (new_dist_100, new_dist_1000)


if __name__ == "__main__":
    print(main())
