import os


def band_name_generator():
    clear_screen = os.system("clear || cls")
    clear_screen

    pet_name_input = input("\nEnter your pet's name: ")
    location_input = input("Enter your home town: ")
    result = location_input + " " + pet_name_input

    print(f"Your band's name is: {result}\n")


band_name_generator()