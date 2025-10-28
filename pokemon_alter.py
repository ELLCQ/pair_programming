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

#data_display module
def data_display(pokemon):
    with open ("pokemon.csv","r") as infile:
        
        lines = infile.readlines()[1:]
        for line in lines:
            split = line.strip().split(",")
            for counter in split:
                counter = 4
                datas = []
                datas = datas.append(split[counter])
                counter += 1
                return datas
print(data_display(pokemon))