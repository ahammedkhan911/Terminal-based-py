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
        print("Error connecting to MySQL database:", error)
        return None

def fetch_components(connection, category):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM partslist WHERE `Item No` LIKE '{category}%'")
        components = cursor.fetchall()
        return components
    except mysql.connector.Error as error:
        print(f"Error fetching {category} components from database:", error)
        return []

def display_components(components):
    print("Code  | Name | Price (Taka) | Quantity")
    print("-" * 70)
    for part in components:
        print(f"{part[0]:<6} | {part[1]:<35} | {part[3]:<12} | {part[2]:<8}")


def view_inventory(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM partslist")
        inventory = cursor.fetchall()
        print("Inventory:")
        print("Code  | Name                               | Price (Taka) | Quantity")
        print("-" * 70)
        for part in inventory:
            print(f"{part[0]:<6} | {part[1]:<35} | {part[3]:<12} | {part[2]:<8}")
    except mysql.connector.Error as error:
        print("Error fetching inventory from database:", error)


def build_pc(connection):
    categories = {
        "CPU": "1",
        "Motherboard": "2",
        "CPU Cooler": "3",
        "CPU Casing": "4",
        "SSD": "5",
        "RAM": "6",
        "Power Supply": "7",
        "GPU": "8",
        "Monitor": "9",
        "Mouse": "11"  # Note: Assuming the mouse category includes entries 1111-1112
    }

    selected_components = {}

    for category, code in categories.items():
        print(f"\nChoose a {category}:")
        components = fetch_components(connection, code)
        display_components(components)
        while True:
            choice = input("Enter the item number of your choice (or press Enter to skip): ")
            if not choice:
                break
            if choice not in [str(comp[0]) for comp in components]:
                print("Invalid item number. Please choose from the available options.")
                continue
            selected_components[category] = choice
            break

    print("\nSelected Components:")
    for category, item_no in selected_components.items():
        print(f"{category}: {item_no}")



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
