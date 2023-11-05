laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOk': 12,
    'ASUS': 30
}

name = input('Input a brand:')

if name in laptops:
    print('Available', name+'s', laptops[name])