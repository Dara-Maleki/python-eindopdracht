# Dictionary van producten met type { string: { price: float } } hierbij is string de naam van het product
products = {
    "Eieren": {
        "price": 4.99,
    },
    "Melk": {
        "price": 1.49,
    },
    "Suiker": {
        "price": 2.99,
    },
}

# Dictionary met verkochte producten van type { string: int } hierbij is string gelijk aan de naam en int gelijk aan het aantal verkocht
sold_products = {
    "Eieren": 17,
    "Melk": 12,
    "Suiker": 21,
}

# Deze funcie neemt een product_name: string en returnd een waarde van { price: float }
# Met de product_name zoekt de functie een product op in de products dictionary
# Als het product niet bestaat geeft het een waarschuwing en returnd het default data
# Als het product wel bestaat returnd de functie de data vann de products dictionary
def get_product_info(product_name):
    product_info = products.get(product_name)
    if not product_info:
        print(f"[WARNING]: Product {product_name} bestaat niet.")
        return { "price": 0.0 }
    return product_info

# Deze functie neemt een debug: bool argument die niet verplicht is en returnd een float
# Als debug gelijk aan True is dan print het de product naam, hoeveel er verkocht zijn, prijs per stuk en het totale incomen van dat specefiek product
# Met een for loop van O(n) returnd het de totale omzet van de winkel
def calculate_net_income(debug = False):
    net_income = 0

    for product_name, amount in sold_products.items():
        product_info = get_product_info(product_name)
        if debug:
            print(f"{product_name} \t ({amount} verkocht) (€%.2f/per stuk) (€%.2f totaal)" % (product_info["price"], (product_info["price"] * amount)))
        net_income += product_info["price"] * amount

    return net_income

print(f"Totale omzet: €%.2f" % calculate_net_income(True))