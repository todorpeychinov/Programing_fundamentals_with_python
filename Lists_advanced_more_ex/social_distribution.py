def distribute_wealth(population, minimum_wealth):
    for index in range(len(population)):
        if population[index] < minimum_wealth:
            diff = minimum_wealth - population[index]
            while population[index] < minimum_wealth:
                max_index = population.index(max(population))
                if index == max_index:
                    break
                population[index] += 1
                population[max_index] -= 1

    if any(current for current in population if current < minimum_wealth):
        return 'No equal distribution possible'
    else:
        return population


population = list(map(int, input().split(', ')))
minimum_wealth = int(input())

result = distribute_wealth(population, minimum_wealth)
print(result)