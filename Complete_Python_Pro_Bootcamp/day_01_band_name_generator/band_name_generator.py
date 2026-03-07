import os 


def clear_terminal_screen():
    return os.system("clear || cls")


def band_name_generator():
    clear_terminal_screen()

    print("\nWelcome to Band Name Generator!\n")

    user_location_input = str(input("Enter your location: "))
    pet_name_input = str(input("Enter your pet's name: "))

    print(f"Your band's name is: {user_location_input} {pet_name_input}\n")


band_name_generator()