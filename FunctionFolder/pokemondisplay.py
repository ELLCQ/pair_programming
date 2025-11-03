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
    print(f"  Total:     {pokemon[4]}")