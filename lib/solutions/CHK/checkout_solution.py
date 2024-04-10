import re

ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    letters = re.findall(r"\w", skus)

    print(letters)


