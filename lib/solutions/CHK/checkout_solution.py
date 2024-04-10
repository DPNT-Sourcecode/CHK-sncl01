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
    count_e = letters.count("E")

    if len(skus) != count_a + count_b + count_c + count_d + count_e:
        return -1

    e_pairs = int(count_e / 2)
    count_b = count_b - e_pairs if count_b and e_pairs else count_b
    price_a_items = count_a * ITEMS["A"]
    price_b_items = count_b * ITEMS["B"]
    price_e_items = count_e * ITEMS["E"]

    if count_a >= 3:
        if count_a >= 5:
            price_a_items = int(count_a / 5) * ITEMS["AAAAA"]
            remaining = count_a % 5
            if remaining >= 3:
                next_remaining = remaining % 3
                if next_remaining:
                    price_a_items += ITEMS["AAA"] + next_remaining * ITEMS["A"]
                else:
                    next_remaining * ITEMS["A"]
            else:
                price_a_items += (
                    int(remaining / 3) * ITEMS["AAA"]
                    if remaining % 3 == 0
                    else remaining * ITEMS["A"]
                )
        else:
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
        + price_e_items
    )



