def check_ticket(ticket):
    wining_symbols = ['@', '#', '$', '^']

    if len(ticket) != 20:
        return 'invalid ticket'

    left_side = ticket[:10]
    right_side = ticket[10:]


    for symbol in wining_symbols:
        for number_of_symbols in range(10, 5, -1):
            uninterrupted_symbols = symbol * number_of_symbols
            if uninterrupted_symbols in left_side and uninterrupted_symbols in right_side:
                if number_of_symbols == 10:
                    return f'ticket "{ticket}" - {number_of_symbols}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {number_of_symbols}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]

for ticket in tickets:
    print(check_ticket(ticket))