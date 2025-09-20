import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="python-project1"
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return None

def fetch_components(connection, category):
    try:
        cursor = connection.cursor()
        query = "SELECT `Item No`, `Item Name`, `Item Amount`, `Item Cost` FROM partslist WHERE Category = %s"
        cursor.execute(query, (category,))
        components = cursor.fetchall()
        return components
    except mysql.connector.Error as error:
        print(f"Error fetching {category} components from the database: {error}")
        return []

def display_components(components):
    print("Code  | Name                               | Price (Taka) | Quantity")
    print("-" * 70)
    for part in components:
        item_no, name, quantity, price = part  # Unpack the tuple
        print(f"{item_no:<6} | {name:<35} | {price:<12} | {quantity:<8}")

def view_inventory(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM partslist")
        inventory = cursor.fetchall()

        print("Inventory:")
        display_components(inventory)

    except mysql.connector.Error as error:
        print(f"Error fetching inventory from database: {error}")

def calculate_total_cost(selected_components, connection):
    total_cost = 0
    try:
        cursor = connection.cursor()
        for category, code in selected_components.items():
            query = "SELECT `Item Cost` FROM partslist WHERE `Item No` = %s"
            cursor.execute(query, (code,))
            result = cursor.fetchone()
            if result:
                item_cost = result[0]
                total_cost += item_cost
            else:
                print(f"Error: Item with code {code} not found in the database.")
    except mysql.connector.Error as error:
        print(f"Error fetching item cost from database: {error}")
    return total_cost

def build_pc(connection):
    categories = {
        "CPU": "Processor",
        "Motherboard": "Motherboard",
        "CPU Cooler": "Cooler",
        "CPU Casing": "Casing",
        "SSD": "SSD",
        "RAM": "RAM",
        "Power Supply": "PSU",
        "GPU": "GPU",
        "Monitor": "Monitor",
        "Mouse": "Mouse"
    }

    selected_components = {}

    for category, db_category in categories.items():
        print(f"\nChoose a {category}:")
        components = fetch_components(connection, db_category)
        display_components(components)

        valid_choices = [str(comp[0]) for comp in components]  # Collect valid component codes as strings

        while True:
            choice = input("Enter the code of your choice (or press Enter to skip): ").strip()
            if not choice:  # If input is empty (Enter pressed), skip to the next category
                break

            if choice not in valid_choices:
                print("Invalid code. Please choose from the available options.")
                continue

            selected_components[category] = choice
            break

    print("\nSelected Components:")
    for category, code in selected_components.items():
        print(f"{category}: {code}")

    total_cost = calculate_total_cost(selected_components, connection)
    print(f"\nTotal Cost of Build: {total_cost} Taka")

def welcome_message():
    print("Welcome to the Online PC Parts Store!")
    print("What would you like to do?")
    print("1. Build a PC")
    print("2. View Inventory")
    choice = input("Enter your choice (1/2): ")
    return choice

def main():
    connection = connect_to_database()
    if not connection:
        return

    while True:
        choice = welcome_message()
        if choice == "1":
            build_pc(connection)
        elif choice == "2":
            view_inventory(connection)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        # Close the database connection and exit loop if user doesn't want to continue
        option = input("Would you like to continue? (y/n): ")
        if option.lower() != 'y':
            break

    connection.close()
    print("Disconnected from the database")

if __name__ == "__main__":
    main()
