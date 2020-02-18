
def discounted(price, discount, max_discount = 50):
    max_discount = abs(float(max_discount))
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)
product = {'name': 'sams', 'stock': 20, 'price': 10000, 'discount': -5}

product['with_discout'] = discounted(product['price'], product['discount'])

print(product)