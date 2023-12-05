import csv

purchases = [
    {'nome': 'ryzen 7', 'valor': 'R$ 2.700'},
    {'nome': 'intel core i7', 'valor': 'R$ 3.000'},
    {'nome': 'geforce rtx 3050', 'valor': 'R$ 5.000'},
    {'nome': 'cooler master', 'valor': 'R$ 500'}
]


with open('data.csv', 'w', encoding="utf-8", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'valor'])
    writer.writeheader()
    writer.writerows(purchases)


with open('data.csv', 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print("All Purchases:")
    for row in reader:
        print(row)

    purchase_to_find = 'ryzen 7'
    f.seek(0)
    for row in reader:
        if row['nome'] == purchase_to_find:
            print(f"\nFound Purchase: {row}")
            break
    else:
        print(f"\nPurchase '{purchase_to_find}' not found.")
