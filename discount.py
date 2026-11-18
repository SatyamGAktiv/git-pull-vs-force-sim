def get_discount(price):
    if price < 0:
        return 0
    return price * 0.10

def get_tax(price):
    return price
