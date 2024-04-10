import re

ITEMS = {"A": 50, "B": 30, "C": 20, "D": 15, "AAA": 130, "BB": 45}


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
    price_a_items = count_a * ITEMS["A"]

    if (count_a >= 3) and count_a % 3 == 0:
        price_a_items = int(count_a / 3) * ITEMS["AAA"]
    elif (count_a >= 3) and count_a % 3 != 0:
        price_a_items = (
            int(count_a / 3) * ITEMS["AAA"]
            + (count_a - int(count_a / 3)) * ITEMS["A"]
        )

    print(price_a_items)

    price_b_items = (
        int(count_b / 2) * ITEMS["BB"]
        if count_b >= 2
        else count_b * ITEMS["B"]
    )

    return (
        price_a_items
        + price_b_items
        + count_c * ITEMS["C"]
        + count_d * ITEMS["D"]
    )






