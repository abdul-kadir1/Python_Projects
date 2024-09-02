# Initialize an empty list to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    # Create a dictionary for the contact and add it to the contacts list
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to search for a contact by name
def search_contact():
    search_name = input("Enter the name of the contact to search: ")
    
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found.")

# Function to delete a contact by name
def delete_contact():
    delete_name = input("Enter the name of the contact to delete: ")
    
    for contact in contacts:
        if contact['name'].lower() == delete_name.lower():
            contacts.remove(contact)
            print(f"Contact '{delete_name}' deleted successfully.")
            return
    print("Contact not found.")

# Function to display the menu and handle user choices
def contact_book_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the contact book menu
contact_book_menu()
