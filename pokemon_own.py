# dictionary of data types:
all_data_types = {1: 'Total',
                  2: 'HP',
                  3: 'Attack',
                  4: 'Defense',
                  5: 'Sp. Atk',
                  6: 'Sp. Def',
                  7: 'Speed',
                  8: 'Generation',
                  9: 'Legendary'}

# dictionary of types of pokemon
tes_of_pokemon = {1: 'Grass',
                    2: 'Fire',
                    3: 'Water',
                    4: 'Bug',
                    5: 'Normal',
                    6: 'Poison',
                    7: 'Electric',
                    8: 'Ground',
                    9: 'Fairy',
                    10: 'Fighting',
                    11: 'Psychic',
                    12: 'Rock',
                    13: 'Ghost',
                    14: 'Dragon',
                    15: 'Dark',
                    16: 'Ice',
                    17: 'Steel'
                    }

def average_stats_calculate(pokemon):
    with open ("pokemon.csv","r") as infile:
        lines = infile.readlines()[1:]
        empty_list = []
        list = []
        counter = 0
        for i in range(1,18):
            for line in lines:
                split = line.strip().split(",")
                type_1 = split[2]
                type_2 = split[3]
                split[4] = int(split[4])
                if type_1 == tes_of_pokemon[i] or type_2 == tes_of_pokemon[i]:
                    empty_list.append(split[4])
                    counter += 1
                total_data = sum(empty_list) / counter
            list.append(total_data)
    return list

pokemon = input('test: ')
print(average_stats_calculate(pokemon))

#finally it works, this module givs exactlly 17 data outputs in a list and the data looks meaningful
