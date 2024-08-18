import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'


def load_contacts():
    """Load contacts from the JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")


def view_contacts(contacts):
    """View the list of contacts."""
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    """Search for a contact by name or phone number."""
    query = input("Enter the name or phone number to search: ")
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details['phone']:
            print(f"\nFound Contact:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            return
    print("Contact not found.")


def update_contact(contacts):
    """Update contact details."""
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")

        contacts[name] = {
            'phone': phone if phone else contacts[name]['phone'],
            'email': email if email else contacts[name]['email'],
            'address': address if address else contacts[name]['address']
        }
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
