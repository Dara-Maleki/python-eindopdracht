cijfer_aardrijkkunde = 5.5
cijfer_engels = 8.0
cijfer_scheikunde = 4.5

# Array van type [ float ] elke float is gelijk aan een cijfer van en vak
cijfers = [
    cijfer_aardrijkkunde,
    cijfer_engels,
    cijfer_scheikunde
]

# Deze functie neemt een array van type [ float ] en berekent de gemiddelde
def calculate_average(array):
    return sum(array) / len(array)

# Print of je met deze cijfers geslaagd of gezakt bent
print("Gezakt" if calculate_average(cijfers) < 5.5 or any(x < 4 for x in cijfers) else "Geslaagd")