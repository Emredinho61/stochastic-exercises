import random


def main(a: int) -> float:
    """
    {1,...,M}
    M ist teilbar durch 2,3,7, das heißt M muss das Produkt sein aus 2*3*7*a sein, wobei a eine natürliche Zahl ist.
    """
    m = 2 * 3 * 7 * a
    randomnumbers = random.randint(a=1, b=m)  # generate a random int between {1,...,M}
    dividable_by_two_three_seven_counter = 0
    if randomnumbers % 2 == 0 or randomnumbers % 3 == 0 or randomnumbers % 7 == 0:
        dividable_by_two_three_seven_counter = 1
    return dividable_by_two_three_seven_counter


if __name__ == "__main__":
    numberOfDiv = []
    numOfIterations = 100000
    for _ in range(numOfIterations):
        numberOfDiv.append(main(10))
    print(f"Die Wahrscheinlichkeit, dass eine ausgewählte Zahl aus der Menge {{1,...,M}} durch 2 oder 3 oder 7 teilbar"
          f" ist, ist: {sum(numberOfDiv) / numOfIterations}")

    # für höhere Anzahl an Iterationen nähert sich der Wert an 0.714
