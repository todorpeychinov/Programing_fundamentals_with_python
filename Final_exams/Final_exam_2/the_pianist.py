def change_key(pieces, new_key):
    if piece in pieces:
        pieces[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def add_piece(pieces, piece, composer, key):
    if piece in pieces:
        print(f"{piece} is already in the collection!")
    else:
        pieces[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return pieces


def remove_piece(pieces, piece):
    if piece in pieces:
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    current_piece, composer, key = input().split('|')
    pieces[current_piece] = {'composer': composer, 'key': key}

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split('|')

    if command[0] == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]

        pieces = add_piece(pieces, piece, composer, key)

    elif command[0] == 'Remove':
        piece = command[1]
        pieces = remove_piece(pieces, piece)

    elif command[0] == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        pieces = change_key(pieces, new_key)

for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")