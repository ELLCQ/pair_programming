

def strongest_pokemon(pokemon_list):
    '''Finds the highest of each stat'''
    if pokemon_list is None:
        print("No Pokemon data available.")
        return
    ts4 = total_stats.copy()
    for x in range(4,11):
        for pokemon in pokemon_list:
            if pokemon[x] > ts3[x-4]:
                ts3[x-4] = pokemon[x]
                ts3names[x-4] = pokemon[1]

        tot_list = []
        for pokemon in pokemon_list:
            if pokemon[x] == ts3[x-4] and pokemon[1] not in ts3names[x-4]:
                ts3names[x-4] += f", {pokemon[1]}"
        print(f"Highest {ts3stats[x-4]} is {ts3[x-4]} by {ts3names[x-4]}")
        htotal = 0
    return

strongest_pokemon(pokemon_load())
