def average_stats_calculate(pokemon):
    with open (r"E:\1850\课业\1.5\pokemon.csv","r", encoding='utf-8') as infile:
        lines = infile.readlines()[1:]
        empty_list = []
        for line in lines:
            split = line.strip().split(",")
            type_1 = split[2]
            split[4] = int(split[4])
            if type_1 == 'Fire':
                
                empty_list.append(split[4])
                result = sum(empty_list)
        return result
pokemon = input('test: ').title()

print(average_stats_calculate(pokemon))

def average_stats_calculate(pokemon):
    with open ("pokemon.csv","r") as infile:
        lines = infile.readlines()[1:]
        empty_list = []
        count = 0
        result = 0
        for line in lines:
            split = line.strip().split(",")
            type_1 = split[2]
            type_2 = split[3]
            split[4] = int(split[4])
            if type_1 == 'Fire':
                count = count + 1
                empty_list.append(split[4])
                result = sum(empty_list)
                #print(count)
            elif type_2 == 'Fire':
                count = count + 1
                empty_list.append(split[4])
                result = sum(empty_list)
                #print(count)
                #print(empty_list)
            if count > 0:
                avtot = result / count
                print(avtot)
        return result
pokemon = input('test: ').title()
print(average_stats_calculate(pokemon))
