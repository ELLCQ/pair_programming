#pokemon statistical analysis
#- Load and display Pokemon data with proper type conversion
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

def pokemon_load(pokemon):
    ''' Opens the pokemon.csv file and checks if the user input matches with the name of any pokemon.
        If it does, the type/types are retuned along with the name '''
    try:
        load = 0
        type3 = ""
        with open ("pokemon.csv","r") as infile:
            lines = infile.readlines()[1:]
            for line in lines:
                split = line.strip().split(",")
                name = split[1]
                Type_1 = split[2]
                if pokemon == name:
                    print(f"{pokemon} has been loaded")
                    load = 1
                    type_2 = split[3]
                    if len(type_2) == 0:
                        type3 = [Type_1]
                    else:
                        type3 = [Type_1, type_2]
                    return pokemon, type3
            if load == 0:
                print("No pokemon with that name has been found")
    except FileNotFoundError:
        print("File not found.")

pokemon = input("What pokemon do you want to load: ").title()
print(pokemon_load(pokemon))


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

#data_display module
def data_display(pokemon):
    with open ("pokemon.csv","r") as infile:
        lines = infile.readlines()[1:]
        #found_mark = False
        for line in lines:
            split = line.strip().split(",")
            name = split[1]
            if pokemon == name:
                #found_mark = True
                #print(line)
                datas = split[4:]
                '''
                counter = 1
                for i in split[4:]:
                    datas = [f'{d[counter]}:{i}']
                # it's possible to pair up each data with the type
                '''
                return datas
print(data_display(pokemon))
