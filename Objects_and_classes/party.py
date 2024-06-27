class Party:

    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.people.append(name)

    def print_total(self):
        return f'Going: {", ".join(self.people)}' \
               f'\nTotal: {len(self.people)}'


current_party = Party()

while True:
    name = input()

    if name == 'End':
        result = current_party.print_total()
        print(result)
        break

    current_party.add_people(name)

