"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def get_price_from_receipt(receipt_line: str) -> int:
    """returns the price from the receipt"""
    return float(receipt_line[-4:])


def calculate_price_after_vat(price: int) -> int:
    """Return the new VAT"""
    return price*0.8


def create_tax_receipt(tax_info: list[list], old_total: int) -> str:
    """Returns the tax receipt from delivered info"""
    formatted_receipt = 'VAT RECEIPT\n\n'
    new_total = 0
    for line in tax_info:
        new_line = line[0][:-4] + f"{line[1]:.2f}"
        new_total += line[1]
        formatted_receipt += new_line + '\n'
    formatted_receipt += f"\nTotal: £{new_total:.2f}\nVAT: £{(old_total-new_total):.2f}\nTotal inc VAT: £{old_total:.2f}"
    return formatted_receipt


def generate_invoice(receipt_string: str) -> str:
    receipt_lines = receipt_string.split('\n')
    tax_info = []

    old_total = 0

    for line in receipt_lines[:-1]:
        price = get_price_from_receipt(line)
        old_total += price
        new_price = calculate_price_after_vat(price)
        tax_info.append([line, new_price])

    return create_tax_receipt(tax_info, old_total)  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
