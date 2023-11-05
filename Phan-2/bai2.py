name = input('Input a brand:')
amount = int(input('Input amount:'))

laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOk': 12,
    'ASUS': 30
}
laptops[name] = amount
print(laptops)