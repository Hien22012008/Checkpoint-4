nhan_vat = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}

res = nhan_vat["Gold"] + 50
nhan_vat["Backpack"].append('FlintStone')

print(res)
print(nhan_vat)