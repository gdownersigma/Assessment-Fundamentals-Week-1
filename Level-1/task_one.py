
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def format_money(price: int) -> str:
    """Returns a string of the nicely formatted price."""
    if price == 0:  # EDGE CASE 'item should be free'
        return 'Free'

    return f"£{price:.2f}"


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    if len(basket) == 0:  # EDGE CASE empty basket
        return "Basket is empty"
    receipt_to_send = ''
    total = 0
    for item in basket:
        total += item['price']
        receipt_to_send += item['name'] + ' - ' + \
            format_money(item['price']) + '\n'

    receipt_to_send += f"Total: {format_money(total)}"
    return receipt_to_send  # return the receipt string


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
