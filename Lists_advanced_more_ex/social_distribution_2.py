def distribute_wealth(population, minimum_wealth):
    if sum(population) < len(population) * minimum_wealth:
        return 'No equal distribution possible'
    else:
        poorest = min(population)

        while poorest < minimum_wealth:
            richiest = max(population)
            richest_index = population.index(richiest)
            poorest_index = population.index(poorest)

            diff = minimum_wealth - poorest
            population[poorest_index] += diff
            population[richest_index] -= diff

            poorest = min(population)

    return population


population = list(map(int, input().split(', ')))
minimum_wealth = int(input())

result = distribute_wealth(population, minimum_wealth)
print(result)