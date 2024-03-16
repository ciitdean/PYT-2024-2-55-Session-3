import csv

# Function to load contacts from CSV file
def load_contacts(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("The contacts file does not exist. Creating a new one.")
        return []

# Function to save contacts to CSV file
def save_contacts(filename, contacts):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(contacts)

# Function to display contacts
def display_contacts(contacts):
    print("\n{:<20} {:<15} {:<30}".format("Name", "Phone", "Email"))
    print("-" * 65)
    for contact in contacts:
        print("{:<20} {:<15} {:<30}".format(contact['Name'], contact['Phone'], contact['Email']))

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"Name": name, "Phone": phone, "Email": email})

# Function to update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Phone'] = input(f"Enter new phone for {name}: ")
            contact['Email'] = input(f"Enter new email for {name}: ")
            found = True
            print(f"Contact '{name}' updated successfully.")
            break
    if not found:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    original_length = len(contacts)
    contacts[:] = [contact for contact in contacts if contact['Name'].lower() != name.lower()]
    if original_length > len(contacts):
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")

# Main function to run the contact management system
def run_contact_manager():
    contacts_file = 'contacts.csv'
    contacts = load_contacts(contacts_file)

    while True:
        print("\nContact Manager")
        print("1. Display Contacts")
        print("2. Add a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts_file, contacts)
        elif choice == '3':
            update_contact(contacts)
            save_contacts(contacts_file, contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts_file, contacts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Running the contact manager
run_contact_manager()
