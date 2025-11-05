def generation_stats(pokemon_list):
    '''Compares the average stats of pokemon across generations'''
    if pokemon_list is None:
        print("No Pokemon data available for generation stats.")
        return
    genA = input("Enter the first generation to compare (1-6): ").strip()
    genB = input("Enter the second generation to compare (1-6): ").strip()
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
    print(f"   Speed:    {GenAavg["Speed"]} vs {GenBavg["Speed"]}")

#generation_stats(pokemon_load())
