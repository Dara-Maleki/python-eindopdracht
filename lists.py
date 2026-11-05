products = [
    "Eieren",
    "Melk",
    "Suiker",
    "Coca Cola",
    "Sushi",
]

def add_product(product_name):
    products.append(product_name)

def remove_product(product_name):
    products.remove(product_name)

def contains_product(product_name):
    return product_name in products

def print_products():
    longest_name = max(products, key=len)
    padding = round(len(longest_name))
    print(f"{"-" * padding} Boodschappenlijst {"-" * padding}")
    for product in products:
        print(f"|{" " * (padding)}{product}{" " * ((padding * 2 + 19) - (padding + 2 + len(product)))}|")
    print("-" * (padding * 2 + 19))

add_product("Framboos Taart")
add_product("Pepsi")
remove_product("Coca Cola")

print(f"Aantal producten: {len(products)}", "\n")

has_cola = contains_product("Coca Cola")
has_pepsi = contains_product("Pepsi")
print(f"Het boodschappenlijste bevat {"" if has_cola else "geen" } Coca Cola", "\n")

print_products()