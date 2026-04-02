import json
import os
import platform


def clean_screen():
    """
    Clears the terminal screen, regardless of the operating system.
    """
    # Checks the operating system and executes the appropriate command to clear the terminal
    if platform.system() == "Windows":
        os.system('cls')  # Command for Windows
    else:
        os.system('clear')  # Command for Linux and macOS


def files_initializer():
    """
    Creates the accounts JSON file if it doesn't exist, ensuring the program
    always has a place to store user data.
    """
    # Checks if the accounts file does not exist
    if not os.path.exists(USER_ACCOUNTS):
        # Creates the file with an empty list, allowing users to be added later
        with open(USER_ACCOUNTS, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)


def data_save(file, data):
    """
    Adds a new dictionary to the specified JSON file, maintaining previous data.
    """

    # Opens the file for reading and loads existing data
    with open(file, 'r') as f:
        existing_data = json.load(f)

    # Adds the new data (a dictionary) to the list of existing records
    existing_data.append(data)

    # Opens the file again in write mode to overwrite with updated data
    with open(file, 'w') as f:
        json.dump(existing_data, f, indent=4)


def greetings():
    """
    Shows the program's home screen, offering three options to the user:
    - Log in;
    - Sing up;
    - Exit the program.
    """
    print("Welcome to FeiFood\n")
    print("Select one of the options:")
    
    # Loop that maintains the menu until the user chooses a valid option
    while True:
        print("[1] Login / [2] Register / [3] Exit Program")
        initial_option = input("\n> ")
        clean_screen()

        # Redirects according to the user's choice
        if initial_option == "1":
            login()
            break
        elif initial_option == "2":
            sign_up_user()
            break
        elif initial_option == "3":
            exit()  # Terminates the program immediately
        else:
            # Error message for invalid inputs
            print("Please, choose one of the options correctly.\n")



def sign_up_user():
    """
    Performs the registration of a new user in the system.

    The user must choose a name and password (minimum of 8 characters each).
    If the username already exists, another will be requested.
    After registration, the user provides a name, ZIP code, and residential number,
    and the data is saved in the accounts JSON file.
    """

    print("Registration Area.\n")
    print("Type a username and password to enter the account:")
    print("(Your username and password must contain at least 8 characters)\n")

    # Reads all existing accounts
    with open(USER_ACCOUNTS, 'r') as read_accounts:
        user_accounts = json.load(read_accounts)

    # Loop until the registration is valid
    while True:
        register_user = input("Username: ")

        # Checks if the user already exists
        user_already_exists = False
        for list_user in user_accounts:
            if register_user == list_user["Username"]:
                print("\nThis user already exists!")
                user_already_exists = True
                break

        # If it already exists, goes back to the start of the loop
        if user_already_exists:
            continue

        register_password = input("Password: ")

        # Checks minimum size for username and password
        if len(register_user) < 8 or len(register_password) < 8:
            clean_screen()
            print("Username and password must have at least 8 characters.\n")
        else:
            break

    # Saves initial account information
    user_account["Username"] = register_user
    user_account["Password"] = register_password

    print("\nLet's create your profile.")
    name = input("Name: ")

    # Requests ZIP code and residential number, ensuring they are numbers
    while True:
        try:
            print("\nType your ZIP code:")
            zip_code = int(input("ZIP Code: "))

            print("\nType your residential number:")
            residency_number = int(input("Number: "))
            break
        except ValueError:
            clean_screen()
            print("You must type only numbers.\n")

    user_account["Name"] = name
    user_account["ZIP_Code"] = zip_code
    user_account["Residency_Number"] = residency_number

    # Saves the account to the JSON file
    data_save(USER_ACCOUNTS, user_account)
    clean_screen()
    menu()



def login():
    """
    Performs the login of an already registered user.

    Reads the accounts file and checks if the username and password correspond to any record.
    If login fails, the user can try again or return to the main menu.
    """

    with open(USER_ACCOUNTS, 'r') as read_accounts:
        list_users_passwords = json.load(read_accounts)

    clean_screen()
    print("\nLogin Area\n")

    login_user = input("Type your username:\n> ")
    login_password = input("Type your password:\n> ")

    user_found = False

    # Iterates through accounts to check for a match
    for account in list_users_passwords:
        if account["Username"] == login_user and account["Password"] == login_password:
            clean_screen()
            print("Login successful!")
            user_found = True

    # If not found, offers options to the user
    if user_found == False:
        print("\nUsername and/or password not found.")
        print("\nDo you wish to go back to the start?")
        print("[1] Yes")
        print("[2] Try again\n")

        while True:
            choice = input("> ")
            if choice == "1":
                clean_screen()
                greetings()
                break
            elif choice == "2":
                login()  # Calls recursively to try again
                break
            else:
                print("\nPlease, choose an option correctly.")
    else:
        menu()



def menu():
    """
    Displays the main menu after login, allowing:
    - Placing an order;
    - Logging out;
    - Exiting the program.
    """

    print("You are logged in.\n")
    print("Main Menu")
    print("Choose one of the options:\n")

    print("[1] Place Order")
    print("[2] Log out")
    print("[3] Exit Program")

    # Maintains the menu until the user chooses a valid option
    while True:
        choose_option = input("\n> ")

        if choose_option == "1":
            clean_screen()
            order_choice_method()
            break
        elif choose_option == "2":
            greetings()
            break
        elif choose_option == "3":
            exit()
        else:
            print("\nPlease, choose an option correctly.")


def order_choice_method():
    """
    Allows the user to choose how they will place their order:
    - Choose a restaurant and see the menu;
    - Search for food by name;
    - Access the shopping cart.
    """

    print("Choose one of the options below:")
    print("(Type 'b' to go back.)\n")

    print("[1] Choose Restaurant")
    print("[2] Search for Food")
    print("[3] Access My Cart")

    # Maintains the loop until the user chooses or goes back
    while True:
        choose_option = input("> ")

        if choose_option == "b":
            clean_screen()
            menu()
            break
        elif choose_option == "1":
            choose_restaurant()
            break
        elif choose_option == "2":
            clean_screen()
            search_food_by_name()
            break
        elif choose_option == "3":
            clean_screen()
            get_cart()
            break
        else:
            print("\nChoose an option correctly.")



def search_food_by_name():
    """
    Allows the user to search for a food item by name across all available restaurants.
    Displays the full menus, performs the search by food name, and offers the option to 
    add it to the cart if found.
    """

    with open(RESTAURANTS, 'r') as f:
        restaurants = json.load(f)  # Loads data from the JSON file with restaurants

    print("Every food we found in our app:\n")

    # Shows all available food in all restaurants
    for restaurant in restaurants:
        for food in restaurant["Foods"]:
            for key, value in food.items():
                print(f"{key}: {value}")
            print("-" * 30)

    while True:
        print("\nType the name of the food you wish to search: ")
        print("(Type 'b' to go back.)\n")
        search = input("> ").lower()  # Receives the food name and converts to lowercase
        
        if search == "b":
            clean_screen()
            order_choice_method()  # Returns to the previous menu
            break

        found = False  # Flag to check if the food was found
        for restaurant in restaurants:
            for food in restaurant["Foods"]:
                if food["Name"].lower() == search:
                    print(f"\nFound at restaurant {restaurant['Restaurant']}!\n")
                    for key, value in food.items():
                        print(f"{key}: {value}")
                    found = True  # Marks as found
        
        # If the food is not found, repeats the process
        if not found:
            print("\nFood not found in any restaurant.")
            continue
        else:
            search = search.capitalize()  # Adjusts name formatting
            # Asks if the user wants to add the item to the cart
            print("\nDo you wish to add it to the cart?")
            print("[1] Yes")
            print("[2] No")

            while True:
                yes_no = input("\n> ")
                if yes_no == "1":
                    cart.append(search)  # Adds the food to the cart
                    print(f"\n{search} added to the cart.")
                    break
                elif yes_no == "2":
                    print(f"\n{search} was not added.")
                    break
                else:
                    print("\nType an option correctly.")
                    continue


def choose_restaurant():
    """
    Displays the list of available restaurants and allows the user to select one 
    by number. After the choice, the restaurant's menu is opened for food selection.
    """

    clean_screen()
    print("Choose a restaurant by number:")
    print("(Type 'b' to exit)\n")

    with open(RESTAURANTS, 'r') as f:
        restaurants = json.load(f)  # Loads restaurant data

    # Displays all restaurants with their respective indices
    for restaurant_index, r in enumerate(restaurants):
        print(f"[{restaurant_index}] {r['Restaurant']}")

    while True:
        choose_restaurant_input = input("\n> ")
        if choose_restaurant_input == "b":
            clean_screen()
            order_choice_method()  # Returns to the previous menu
            break
        try:
            # Converts choice to number and opens the chosen restaurant's menu
            choose_restaurant_input = int(choose_restaurant_input)
            choose_food_by_restaurant(choose_restaurant_input)
            break
        except (IndexError, ValueError):
            print("\nPlease, type the restaurant INDEX correctly.")


def choose_food_by_restaurant(food_index):
    """
    Displays the menu of a specific restaurant based on the informed index. 
    Allows the user to select a food item and add it to the cart.
    """

    clean_screen()
    specific_food = int(food_index)  # Stores the original restaurant index
    food_index = int(food_index)
    with open(RESTAURANTS, 'r') as f:
        restaurants = json.load(f)  # Loads all restaurants

    print("Menu:\n")

    # Displays all food items from the selected restaurant
    for i, food in enumerate(restaurants[food_index]["Foods"]):
        print(f"[{i}]")  # Shows the food index
        for key, value in food.items():
            print(f"{key}: {value}")
        print("-" * 30)
        food_index += 1  # Increments to iterate (does not affect loop directly)

    print("\nChoose a food by INDEX to add to your cart:")
    print("(Type 'b' to go back.)\n")

    while True:
        place_order = input("> ")
        if place_order.lower() == "b":
            clean_screen()
            order_choice_method()  # Returns to the previous menu
            break
        try:
            # Converts the chosen index and adds the corresponding food to the cart
            specific_index = int(place_order)
            item = restaurants[specific_food]["Foods"][specific_index]["Name"]
            cart.append(item)
            print(f"{item} added to the cart.")
        except (IndexError, ValueError):
            # Handles errors if the user types an invalid index
            print("\nPlease, select a food correctly.")

def show_cart_total_price():
    """
    Calculates and displays the total price of items in the cart.
    For each food item in the cart, searches for the corresponding price
    in the 'restaurants.json' file and adds to the total.
    """

    total = 0.0  # Accumulator for total value

    # Opens the restaurants file
    with open(RESTAURANTS, 'r') as f:
        restaurants = json.load(f)

    # Iterates through each food item in the cart
    for cart_food in cart:
        for restaurant in restaurants:
            for food in restaurant["Foods"]:
                if food["Name"] == cart_food:
                    total += food["Price"]  # Adds price to total

    # Shows the final cart value
    print(f"\nTotal cart value: $ {total:.2f}")


def get_cart():
    """
    Displays the current content of the user's cart and offers options to:
    - Finalize the purchase;
    - Edit (remove items from the cart);
    - Go back to add more food.
    If the cart is empty, allows only returning to the main menu.
    """

    print("My Cart:\n")
    print(*cart, sep=", ")  # Displays cart items separated by commas
    show_cart_total_price()
    
    # If the cart contains items
    if len(cart) > 0:

        print("\nWhat do you wish to do?")
        print("[1] Finalize Purchase")
        print("[2] Edit Cart")
        print("[3] Go Back")

        while True:
            finalize_or_not = input("\n> ")

            # Option to finalize purchase
            if finalize_or_not == "1":
                clean_screen()
                finish_order()
                break

            # Option to edit the cart (remove items)
            elif finalize_or_not == "2":
                clean_screen()
                while True:
                    print("Choose a food you wish to delete:")
                    print("(Type 'b' to go back)\n")

                    # Displays each item with its index
                    for index, food in enumerate(cart):
                        print(f"[{index}] {food}")

                    delete_food = input("> ")

                    # Returns to the cart if the user wants to exit
                    if delete_food == "b":
                        clean_screen()
                        get_cart()
                        break

                    try:
                        delete_food = int(delete_food)  # Converts informed index
                        cart.pop(delete_food)  # Removes the chosen item
                    except (ValueError, IndexError):
                        print("\nType a correct option.")

            # Go back to the order choice menu
            elif finalize_or_not == "3":
                clean_screen()
                order_choice_method()
                break
            else:
                print("\nType an option correctly.")

    # If the cart is empty
    else:
        print("\n[1] Return to Menu.")
        type_one = input("> ")
        if type_one == "1":
            clean_screen()
            menu()


def finish_order():
    """
    Performs the purchase finalization process:
    - Displays payment options;
    - Confirms the chosen method;
    - Allows rating the order or returning to the main menu.
    After finalizing, the cart is emptied.
    """

    print("Time to finalize the purchase!\n")
    print("What will be your payment method?")
    print("(Payment will be made to the delivery person)\n")

    print("[1] Credit Card")
    print("[2] Debit Card")
    print("[3] Pix")
    print("[4] Cash")

    while True:
        choose_payment = input("> ")

        # Checks if the payment option is valid
        if choose_payment in ["1", "2", "3", "4"]:

            clean_screen()
            print("Payment method chosen successfully!")
            print("We are preparing your order and it will soon be on its way!")
            print("Enjoy your meal!")

            print("\nWhat do you wish to do?")
            print("[1] Rate Order")
            print("[2] Return to Menu")

            # After payment, the user can rate the order or go back
            while True:
                rate_or_not = input("> ")

                if rate_or_not == "1":
                    rate_order()
                    break
                elif rate_or_not == "2":
                    cart.clear()  # Clears the cart after finalization
                    clean_screen()
                    menu()
                    break
                else:
                    print("\nPlease, choose an option correctly.")
            break
        else:
            print("\nPlease, choose an option correctly.")



def rate_order():
    """
    Requests a rating (0 to 5) for each unique food item in the cart.
    Updates the average rating in the restaurants JSON and saves the changes.
    """

    # Converts the cart into a set to eliminate duplicate food items
    unique_foods = list(set(cart))
    
    # Opens the restaurants file and loads the data into memory
    with open(RESTAURANTS, 'r') as f:
        restaurants = json.load(f)
    
    # Iterates over each unique food item from the cart
    for food_name in unique_foods:
        while True:
            try:
                # Requests a score from 0 to 5 for the food item
                rating = float(input(f"Rate '{food_name}' from 0 to 5: "))
                if 0 <= rating <= 5:
                    break  # Exits loop if rating is valid
                else:
                    print("Type a number between 0 and 5.")
            except ValueError:
                # Catches error if the user types something that is not a number
                print("Type a valid number.")
        
        # Searches for the food item in the JSON and updates its rating
        for restaurant in restaurants:
            for food in restaurant["Foods"]:
                if food["Name"] == food_name:
                    # Increments the number of ratings for the food item
                    food["Rating_Count"] += 1
                    # Updates the rating average
                    food["Rating"] = (food["Rating"] + rating) / food["Rating_Count"]
    
    # Saves the changes to the restaurants file
    with open(RESTAURANTS, 'w') as f:
        json.dump(restaurants, f, indent=4)
    
    # Clears screen and displays success message
    clean_screen()
    print("\nRatings registered successfully!")
    print("Returning to menu...\n")
    # Empties the cart after ratings
    cart.clear()

    # Returns to the main menu
    menu()


# Paths of the JSON files used by the system
USER_ACCOUNTS = "user_accounts.json"
RESTAURANTS = "restaurants.json"

# Base structure of a user account
user_account = {
    "Username": "",
    "Password": "",
    "Name": "",
    "ZIP_Code": "",
    "Residency_Number": ""
}

# List that temporarily stores the food items selected by the user
cart = []

# Initializes the system, displays the welcome message, and opens the main menu
files_initializer()
greetings()