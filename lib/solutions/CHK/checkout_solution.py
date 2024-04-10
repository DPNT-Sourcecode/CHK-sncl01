import re

ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    letters = re.findall(r"\w", skus)
    count_a = letters.count("A")
    count_b = letters.count("B")
    count_c = letters.count("C")
    count_d = letters.count("D")

    if len(skus) != count_a + count_b + count_c + count_d:
        return -1

    # print(count_a)
    # print(count_b)
    # print(count_c)
    # print(count_d)

    if count_a % 3 == 0

    return (
        count_a * ITEMS["A"]
        + count_b * ITEMS["B"]
        + count_c * ITEMS["C"]
        + count_d * ITEMS["D"]
    )


