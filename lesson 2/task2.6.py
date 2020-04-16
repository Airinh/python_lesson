products = []
test = 'да'
number = 1
product_n = {'название':"товар", 'цена':0, 'количество':0, 'единица измерения':"шт"}
while test == 'да':
    for key in product_n:
        product_n[key] = input(f' {key}: ')
    test = input('Хотите добавить еще товар (да/нет) ')
    test = test.lower()
    products.append((number, product_n))
    number += 1
print(products)

