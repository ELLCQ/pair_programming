def pokemon_load():
    """Load Pokemon data from CSV file and convert to proper types"""
    filename = "pokemon.csv"
    #attempts to open file, gives error message if file not found
    try:
        with open(filename, "r") as infile:
            data = infile.readlines()[1:]
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    pokemon_list = []
    for line in data:
        line = line.strip().split(",")
        for i in range(len(line)):
            line[i] = line[i].strip()
        if line[i] == '':
            continue
        try:
            pokemon = [line[0], line[1], line[2],
            line[3] if len(line[3]) > 0 else None,
            int(line[4]), int(line[5]), int(line[6]), int(line[7]),
            int(line[8]), int(line[9]), int(line[10]),
            int(line[11]), line[12].lower() == 'true']  

            pokemon_list.append(pokemon)
        except ValueError:
            continue
    return pokemon_list


print(pokemon_load())