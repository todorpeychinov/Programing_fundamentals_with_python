dwarfs = []

while True:
    current_dwarf = input().split(' <:> ')

    if current_dwarf[0] == 'Once upon a time':
        break

    dwarf_name = current_dwarf[0]
    dwarf_hat_color = current_dwarf[1]
    dwarf_physics = int(current_dwarf[2])

    is_already_exists = False
    for dwarf in dwarfs:
        if dwarf['name'] == dwarf_name:
            is_already_exists = True
            if dwarf['hat_color'] != dwarf_hat_color:
                dwarfs.append({'name': dwarf_name,'hat_color': dwarf_hat_color, 'physics': dwarf_physics})
            else:
                if dwarf['physics'] < dwarf_physics:
                    dwarf['physics'] = dwarf_physics
        if is_already_exists:
            break
    else:
        dwarfs.append({'name': dwarf_name,'hat_color': dwarf_hat_color, 'physics': dwarf_physics})

hat_color_count = {}
for dwarf in dwarfs:
    hat_color = dwarf['hat_color']
    if hat_color not in hat_color_count:
        hat_color_count[hat_color] = 0
    hat_color_count[hat_color] += 1

ordered_dwarfs = sorted(dwarfs, key=lambda x: (-x['physics'], hat_color_count[x['hat_color']]))

for dwarf in ordered_dwarfs:
    print(f"({dwarf['hat_color']}) {dwarf['name']} <-> {dwarf['physics']}")


