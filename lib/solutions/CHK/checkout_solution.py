import re

ITEMS = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "AAA": 130,
    "AAAAA": 200,
    "BB": 45,
}


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

    price_a_items = count_a * ITEMS["A"]
    price_b_items = count_b * ITEMS["B"]

    if count_a >= 3:
        price_a_items = (
            int(count_a / 3) * ITEMS["AAA"]
            if count_a % 3 == 0
            else int(count_a / 3) * ITEMS["AAA"]
            + (count_a - int(count_a / 3) * 3) * ITEMS["A"]
        )

    if count_b >= 2:
        price_b_items = (
            int(count_b / 2) * ITEMS["BB"]
            if count_b % 2 == 0
            else int(count_b / 2) * ITEMS["BB"] + ITEMS["B"]
        )

    return (
        price_a_items
        + price_b_items
        + count_c * ITEMS["C"]
        + count_d * ITEMS["D"]
    )



