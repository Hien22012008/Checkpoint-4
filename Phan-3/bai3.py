price_laptops = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}
name = input('Input a brand:')

if name in price_laptops:
    print('Price of', name, price_laptops[name])