import random

def pokemon_name_search(pokemon_list):
    """Search for a specific Pokemon by name"""
    name = input("Enter the name of the Pokemon: ").strip().lower()
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
