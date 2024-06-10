events_list = input().split('|')

initial_energy = 100
initial_coins = 100
events_flag = True

for event in events_list:
    event_list = event.split('-')
    event_type = event_list[0]
    event_value = int(event_list[1])

    if event_type == 'rest':
        current_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            print("You had to rest!")
            initial_energy += 50



    else:
        if initial_coins >= event_value:
            print(f"You bought {event_type}.")
            initial_coins -= event_value
        else:
            print(f"Closed! Cannot afford {event_type}.")
            events_flag = False
            break

if events_flag:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")


