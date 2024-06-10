fire_cells = input().split('#')

cells_list = []
effort = 0

water_amount = int(input())

for cell in fire_cells:
    cell_list = cell.split(" = ")
    fire_type = cell_list[0]
    cell_value = int(cell_list[1])

    if fire_type == "High" and cell_value >= 81 and cell_value <= 125:
        if water_amount >= cell_value:
            cells_list.append(cell_value)
            water_amount -= cell_value
            effort += cell_value * 0.25
    elif fire_type == "Medium" and cell_value >= 51 and cell_value <= 80:
        if water_amount >= cell_value:
            cells_list.append(cell_value)
            water_amount -= cell_value
            effort += cell_value * 0.25
    elif fire_type == "Low" and cell_value >= 1 and cell_value <= 50:
        if water_amount >= cell_value:
            cells_list.append(cell_value)
            water_amount -= cell_value
            effort += cell_value * 0.25

print("Cells:")
for cell in cells_list:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_list)}")
