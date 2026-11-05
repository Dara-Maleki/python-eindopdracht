player_class = "Mage"
health = 0
damage = 0

match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
    case "Wizard":
        health = 55
        damage = 35
    case "Gunshooter":
        health = 65
        damage = 44


print(player_class,health,damage)