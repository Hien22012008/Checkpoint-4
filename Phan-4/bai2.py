name = input('Input a brand:')
amount = int(input('Input amount:'))

price_laptops = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

price = price_laptops[name] * amount

print(price)
