"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def get_price_from_receipt(receipt_line: str) -> int:
    """returns the price from the receipt"""
    return float(receipt_line[-4:])


def calculate_price_after_vat(price: int) -> int:
    """Return the new VAT"""
    return price*0.8


def generate_invoice(receipt_string: str) -> str:
    receipt_lines = receipt_string.split('\n')
    tax_info = []

    old_total = 0

    for line in receipt_lines[:-1]:
        price = get_price_from_receipt(line)
        old_total += price
        new_price = calculate_price_after_vat(price)
        tax_info.append([line, new_price])

    print(tax_info)

    return  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
