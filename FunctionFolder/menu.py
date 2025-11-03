def display_menu():
    '''Display the main menu and handle user input'''
    print("Hello user!\n Welcome to our pokemon data analysis project!\n")
    while True:
        print("--What would you like to do today?--")
        print("Load a specific pokemon and display it's stats (1)")
        print("Find the average stats of pokemon of a given category (2)")
        print("Find the strongest pokemon of a specific stat (3)")
        print("Learn information about types (4)")
        print("Exit the program (5)\n")

        user = input("Please enter your choice here: ").strip()
        if user == "1":
            print(func1)
        elif user == "2":
            print(func2)
        elif user == "3":
            print(func3)
        elif user == "4":
            print(func4)
        elif user == "5":
            break
        else:
            print("Please enter a valid choice \n (1-5)")


display_menu()