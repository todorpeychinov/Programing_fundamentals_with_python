class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            species = 'Mammals'
            names = ", ".join(self.mammals)

        elif species == 'fish':
            species = 'Fishes'
            names = ", ".join(self.fishes)

        elif species == 'bird':
            species = 'Birds'
            names = ", ".join(self.birds)

        return f"{species} in {self.name}: {names}\n" \
               f"Total animals: {Zoo.__animals}"


current_zoo_name = input()
number_of_animals = int(input())

current_zoo = Zoo(current_zoo_name)

for current_animal in range(number_of_animals):
    current_species, current_name = input().split()
    current_zoo.add_animal(current_species, current_name)

species_to_be_printed = input()

print(current_zoo.get_info(species_to_be_printed))


