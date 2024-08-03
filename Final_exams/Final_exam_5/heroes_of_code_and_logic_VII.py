def heal(heroes, hero_name, amount):
    hp_before_recharge = heroes[hero_name]['HP']
    heroes[hero_name]['HP'] += amount
    if heroes[hero_name]['HP'] > 100:
        heroes[hero_name]['HP'] = 100
    hp_after_recharge = heroes[hero_name]['HP']
    recharging_amount = hp_after_recharge - hp_before_recharge
    print(f"{hero_name} healed for {recharging_amount} HP!")

    return heroes



def recharge(heroes, hero_name, amount):
    mp_before_recharge = heroes[hero_name]['MP']
    heroes[hero_name]['MP'] += amount
    if heroes[hero_name]['MP'] > 200:
        heroes[hero_name]['MP'] = 200
    mp_after_recharge = heroes[hero_name]['MP']
    recharging_amount = mp_after_recharge - mp_before_recharge
    print(f"{hero_name} recharged for {recharging_amount} MP!")

    return heroes


def take_damage(heroes, hero_name, damage, attacker):
    heroes[hero_name]['HP'] -= damage
    if heroes[hero_name]['HP'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")
    return heroes


def cast_spell(heroes, hero_name, mp_needed, spell_name):
    if heroes[hero_name]['MP'] >= mp_needed:
        heroes[hero_name]['MP'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return heroes


number_of_heroes = int(input())

heroes = {}

for _ in range(number_of_heroes):
    hero_name, HP, MP = input().split()
    HP = int(HP)
    MP = int(MP)

    if HP > 100:
        HP = 100

    if MP > 200:
        MP = 200

    heroes[hero_name] = {'HP': HP, 'MP': MP}

while True:
    command = input()

    if command == 'End':
        break

    command = command.split(' - ')

    if command[0] == 'CastSpell':

        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        heroes = cast_spell(heroes, hero_name, mp_needed, spell_name)

    elif command[0] == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes = take_damage(heroes, hero_name, damage, attacker)

    elif command[0] == 'Recharge':
        hero_name = command[1]
        amount = int(command[2])

        heroes = recharge(heroes, hero_name, amount)

    elif command[0] == 'Heal':
        hero_name = command[1]
        amount = int(command[2])
        heroes = heal(heroes, hero_name, amount)

for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")