
#pokemon statistical analysis
#- Load and display Pokemon data with proper type conversion
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
#mythical pokemon don't count as legendary
#functions to implement:
#menu display
#load pokemon to list
#search pokemon by name or random
#display pokemon details
#load list of pokemon of a given type
#find average stats of a type
#find strongest pokemon in each stat category
#compare average stats of each generation
#generate type effectiveness insights

import random
total_stats = {"Total": 0, "HP": 0, "Attack": 0, "Defense": 0, "Sp. Atk": 0, "Sp. Def": 0, "Speed": 0}
ts3 = [0,0,0,0,0,0,0]
ts3stats = ["Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
ts3names = ["","","","","","",""]
list_type = ['Grass','Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Ice', 'Steel']

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

def pokemon_name_search(pokemon_list):
    """Search for a specific Pokemon by name"""
    name = input("\nEnter the name of the Pokemon: ").strip().lower()
    for pokemon in pokemon_list:
        if pokemon[1].lower() == name:
            print(f"'{name}' has been found!")
            return pokemon
    print(f"'{name}' has not been found!")
    pokemon = None
    return pokemon

def pokemon_random_search(pokemon_list):
    """Select a random Pokemon from the list"""
    if not pokemon_list:
        return None
    pokemon = random.choice(pokemon_list)
    name = pokemon[1]
    print(f"Randomly selected Pokemon: '{name}'")
    return pokemon

def pokemon_display(pokemon):
    """Display detailed information about a Pokemon"""
    if pokemon is None:
        print("No Pokemon to display.")
        return
    print(f"-- {pokemon[1]} --")
    print(f"Pokedex no.: {pokemon[0]}")
    

    types = pokemon[2]
    type2 = pokemon[3]
    if len(type2 or "") > 0:
        types = f"{types} / {type2}"
    print(f"Type: {types}")
    
    print(f"Generation: {pokemon[11]}")
    print(f"Legendary: {'Yes' if pokemon[12] == True else 'No'}")

    print(f"\nBase Stats:")
    print(f"  HP:        {pokemon[5]}")
    print(f"  Attack:    {pokemon[6]}")
    print(f"  Defense:   {pokemon[7]}")
    print(f"  Sp. Atk:   {pokemon[8]}")
    print(f"  Sp. Def:   {pokemon[9]}")
    print(f"  Speed:     {pokemon[10]}")
    print(f"  Total:     {pokemon[4]}\n")
    user1 = input("Press Enter to continue...")
    return

#pokemon_display(pokemon_name_search(pokemon_load()))
#pokemon_display(pokemon_random_search(pokemon_load()))

#pokemon type stat average function
#
#
#
#
#
#
#


#generation stat comparison
def generation_stats(pokemon_list):
    '''Compares the average stats of pokemon across generations'''
    if pokemon_list is None:
        print("No Pokemon data available for generation stats.")
        return
    genA = input("Enter the first generation to compare (1-6): ").strip()
    genB = input("Enter the second generation to compare (1-6): ").strip()
    if genA == genB:
        print("Please enter two different generations.\n")
        generation_stats(pokemon_list)
        return
        
    ts1 = total_stats.copy()
    ts2 = total_stats.copy()
    countA = 0
    countB = 0
    for pokemon in pokemon_list:
        gen = str(pokemon[11])
        if gen == genA:
            ts1["Total"] += pokemon[4]
            ts1["HP"] += pokemon[5]
            ts1["Attack"] += pokemon[6]
            ts1["Defense"] += pokemon[7]
            ts1["Sp. Atk"] += pokemon[8]
            ts1["Sp. Def"] += pokemon[9]
            ts1["Speed"] += pokemon[10]
            countA += 1
        elif gen == genB:
            ts2["Total"] += pokemon[4]
            ts2["HP"] += pokemon[5]
            ts2["Attack"] += pokemon[6]
            ts2["Defense"] += pokemon[7]
            ts2["Sp. Atk"] += pokemon[8]
            ts2["Sp. Def"] += pokemon[9]
            ts2["Speed"] += pokemon[10]
            countB += 1
    if countA == 0 or countB == 0:
        print("One of the generations has no Pokemon data.")
        return
    GenAavg = {k: round(v / countA, 2) for k, v in ts1.items()}
    GenBavg = {k: round(v / countB, 2) for k, v in ts2.items()}
    print(f"\nAverage stats for {countA} gen {genA} pokemon vs {countB} gen {genB} pokemon:")
    print(f"   Total:   {GenAavg["Total"]} vs {GenBavg["Total"]}")
    print(f"   HP:       {GenAavg["HP"]} vs {GenBavg["HP"]}")
    print(f"   Attack:   {GenAavg["Attack"]} vs {GenBavg["Attack"]}")
    print(f"   Defense:  {GenAavg["Defense"]} vs {GenBavg["Defense"]}")
    print(f"   Sp. Atk:  {GenAavg["Sp. Atk"]} vs {GenBavg["Sp. Atk"]}")
    print(f"   Sp. Def:  {GenAavg["Sp. Def"]} vs {GenBavg["Sp. Def"]}")
    print(f"   Speed:    {GenAavg["Speed"]} vs {GenBavg["Speed"]}\n")
    user3 = input("Press Enter to continue...")

#generation_stats(pokemon_load())

def strongest_pokemon(pokemon_list):
    '''Finds the highest of each stat'''
    if pokemon_list is None:
        print("No Pokemon data available.")
        return
    ts4 = ts3.copy()
    ts4names = ts3names.copy()
    for x in range(4,11):
        for pokemon in pokemon_list:
            if pokemon[x] > ts4[x-4]:
                ts4[x-4] = pokemon[x]
                ts4names[x-4] = pokemon[1]

        tot_list = []
        for pokemon in pokemon_list:
            if pokemon[x] == ts4[x-4] and pokemon[1] not in ts4names[x-4]:
                ts4names[x-4] += f", {pokemon[1]}"
        print(f"Highest {ts3stats[x-4]} is {ts4[x-4]} by {ts4names[x-4]}")
        htotal = 0
    user4 = input("\nPress Enter to continue...")
    return

#strongest_pokemon(pokemon_load())

#find weakest pokemon function

def weakest_pokemon(pokemon_list):
    '''Finds the lowest of each stat'''
    if pokemon_list is None:
        print("No Pokemon data available.")
        return
    ts5 = [999,999,999,999,999,999,999]
    ts5names = ts3names.copy()
    for x in range(4,11):
        for pokemon in pokemon_list:
            if pokemon[x] < ts5[x-4]:
                ts5[x-4] = pokemon[x]
                ts5names[x-4] = pokemon[1]

        tot_list = []
        for pokemon in pokemon_list:
            if pokemon[x] == ts5[x-4] and pokemon[1] not in ts5names[x-4]:
                ts5names[x-4] += f", {pokemon[1]}"
        print(f"Lowest {ts3stats[x-4]} is {ts5[x-4]} by {ts5names[x-4]}")
        htotal = 0
    user5 = input("\nPress Enter to continue...")
    return

#weakest_pokemon(pokemon_load())

#genrate type effectiveness  - this is on ice for the moment

def type_info():
    '''Generates type effectiveness insights'''
    Type = input("Enter a Pokemon type to get effectiveness info: ").strip().title()
    if Type not in list_type:
        print("Invalid type entered.")
        return
    match Type:
        case 'Normal':
            print("Normal type is strong against nothing, and is resisted by Rock, and Steel, and can't hit Ghost.")
        case 'Fire':
            print("Fire type is strong against Grass, Bug, Ice, and Steel, and is resisted by Fire, Water, Rock, and Dragon.")
        case 'Water':
            print("Water type is strong against Fire, Ground, and Rock, and is resisted by Water, Grass, and Dragon.")
        case 'Electric':
            rint("Electric type is strong against Water and Flying, and is resisted by Electric, Grass, and Dragon, and can't hit Ground.")
        case 'Grass':
            print("Grass type is strong against Water, Ground, and Rock, and is resisted by Fire, Grass, Poison, Flying, Bug, Dragon, and Steel.")
        case 'Ice':
            print("Ice type is strong against Grass, Ground, Flying, and Dragon, and is resisted by Fire, Water, Ice, and Steel.")
        case 'Fighting':
            print("Fighting type is strong against Normal, Ice, Rock, Dark, and Steel, and is resisted by Poison, Flying, Psychic, Bug, and Fairy, and can't hit Ghost.")
        case 'Poison':
            print("Poison type is strong against Grass and Fairy, and is resisted by Poison, Ground, Rock, and Ghost, and can't hit Steel.")
        case 'Ground':
            print("Ground type is strong against Fire, Electric, Poison, Rock, and Steel, and is resisted by Grass and Bug, and can't hit Flying.")
        case 'Flying':
            print("Flying type is strong against Grass, Fighting, and Bug, and is resisted by Electric, Rock, and Steel.")
        case 'Psychic':
            print("Psychic type is strong against Fighting and Poison, and is resisted by Psychic and Steel, and can't hit Dark.")
        case 'Bug':
            print("Bug type is strong against Grass, Psychic, and Dark, and is resisted by Fire, Fighting, Poison, Flying, Ghost, Steel, and Fairy.")
        case 'Rock':
            print("Rock type is strong against Fire, Ice, Flying, and Bug, and is resisted by Fighting, Ground, and Steel.")
        case 'Ghost':
            print("Ghost type is strong against Psychic and Ghost, and is resisted by Dark, and can't hit Normal.")
        case 'Dragon':
            print("Dragon type is strong against Dragon, and is resisted by Steel, and can't hit Fairy.")
        case 'Dark':
            print("Dark type is strong against Psychic and Ghost, and is resisted by Fighting, Dark, and Fairy.")
        case 'Steel':
            print("Steel type is strong against Ice, Rock, and Fairy, and is resisted by Fire, Water, Electric, and Steel.")
        case 'Fairy':
            print("Fairy type is strong against Fighting, Dragon, and Dark, and is resisted by Fire, Poison, and Steel.")
        case _:
            print("Type effectiveness information not available.")
    print("")
    choice4 = input("Press Enter to continue...")
    return

#type_info()

#menu display function

def display_menu():
    '''Display the main menu and handle user input'''
    print("Hello user!\n Welcome to our pokemon data analysis project!\n")
    while True:
        print("--What would you like to do today?--")
        print("Load a pokemon and display it's stats (1)")
        print("Get information on the average stats of pokemon of a given category (2)")
        print("Find the strongest/weakest pokemon of every stat (3)")
        print("Learn information about types (4)")
        print("Exit the program (5)\n")

        user = input("Please enter your choice here: ").strip()
        if user == "1":
            choice1 = input("Would you like to search by name (1) or randomly (2)? ").strip()
            if choice1 == "1":
                pokemon_display(pokemon_name_search(pokemon_load()))
            elif choice1 == "2":
                pokemon_display(pokemon_random_search(pokemon_load()))
            else:
                print("Invalid choice. Returning to main menu.\n")
        elif user == "2":
            choice2 = input("Would you like search by type or compare generations? (type/gen) ").strip().lower()
            if choice2 == "type":
                print("This is where type average stats function will go.\n")
            elif choice2 == "gen":
                generation_stats(pokemon_load())
            else:
                print("Invalid choice. Returning to main menu.\n")
        elif user == "3":
            choice3 = input("Would you like to find the strongest (1) or weakest (2) pokemon? ").strip()
            print("")
            if choice3 == "1":
                strongest_pokemon(pokemon_load())
            elif choice3 == "2":
                weakest_pokemon(pokemon_load())
            else:
                print("Invalid choice. Returning to main menu.\n")
        elif user == "4":
            type_info()
        elif user == "5":
            break
        else:
            print("Please enter a valid choice \n (1-5)")


#display_menu()
