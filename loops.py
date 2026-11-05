monster_health = 150
player_damage = 25
attacks = 0

while monster_health > 0:
    monster_health -= player_damage
    attacks += 1

    if monster_health < 0:
        monster_health = 0

    print(monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", attacks)