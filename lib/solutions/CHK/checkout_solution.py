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

    print(len(skus))

    print(count_a)
    print(count_b)
    print(count_c)
    print(count_d)
