

# 2. 🛒 Internet-do‘kon
# Product va Shop classlaridan foydalaning.
# Imkoniyatlar:
# Mahsulot qo‘shish
# Mahsulotni o‘chirish
# Mahsulot qidirish
# Narx bo‘yicha saralash
# Savatchaga mahsulot qo‘shish
# Savatchadan o‘chirish
# Umumiy narxni hisoblash
# Chegirma qo‘llash
# Buyurtma berish
# Ombordagi mahsulot sonini kamaytirish

products = []
cart = []


products.append(["Telefon", 3000000, 5])
products.append(["Noutbuk", 7000000, 3])
products.append(["Sichqoncha", 100000, 10])


print(products)


for product in products:
    if product[0] == "Telefon":
        print("Topildi:", product)

for product in products:
    if product[0] == "Telefon":
        cart.append(product)

print("Savatcha:", cart)


total = 0

for product in cart:
    total += product[1]

print("Umumiy narx:", total)


total = total - total * 10 / 100

print("Chegirmadan keyin:", total)

for product in cart:
    product[2] -= 1

print("Buyurtma berildi")
print("Omborda Telefon:", products[0][2])


cart.clear()

print("Savatcha:", cart)
