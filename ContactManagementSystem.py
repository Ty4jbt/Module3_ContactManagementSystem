# Objective: Create a functional command-line based application that simplifies the management of contacts. You will be able to add, edit, delete, and search for contacts, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.

# Task 1

# Imports regex module to validate the name, phone, and email are in the correct format.
import re

# Initializes an empty dictionary to store contacts.
contacts = {}

# Validates that the name is in the correct format.
def validate_name(name):
    return bool(re.match(r'^[A-Za-z\s]+$', name))

# Validates that the phone number is in the correct format.
def validate_phone(phone):
    return bool(re.match(r'^\d{10}$', phone))

# Validates that the email is in the correct format.
def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

# Validates that the contact information is in the correct format using the validate_name, validate_phone, and validate_email functions.
def validate_contact_info(name, phone, email):
    return (
        validate_name(name) and
        validate_phone(phone) and
        validate_email(email)
    )

# Function to display the contact information.
def display_contact(contact_id):
    contact_info = contacts[contact_id]
    print(f"Name: {contact_info['name']}")
    print(f"Phone: {contact_info['phone']}")
    print(f"Email: {contact_info['email']}")
    print(f"Additional Info: {contact_info['additional_info']}")
    print()

# Function to add a new contact.
def add_contact():

    # Prompts the user to enter the contact information.
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information: ")

    # Validates the contact information and adds the contact to the dictionary if valid.
    if validate_contact_info(name, phone, email):

        # If input is valid, the phone number is used as the unique identifier for the contact.
        contact_id = phone

        # Adds the contact information to the contacts dictionary.
        contacts[contact_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "additional_info": additional_info
        }

        # Prints a success message if the contact is added successfully.
        print("Contact added successfully!")
    else:
        # Prints an error message if the contact information is invalid.
        print("Invalid contact information. Please try again.")

# Function to edit an existing contact.
def edit_contact():

    # Prompts the user to enter the phone number of the contact to edit.
    print("\nEditing an existing contact:")
    contact_id = input("Enter the phone number of the contact to edit: ")
    
    # Checks if the contact exists in the contacts dictionary.
    if contact_id in contacts:

        # Displays the current contact information.
        print("Current contact information:")
        display_contact(contact_id)
        
        # Prompts the user to enter the new contact information.
        name = input("Enter new name (press Enter to keep current): ")
        phone = input("Enter new phone number (press Enter to keep current): ")
        email = input("Enter new email address (press Enter to keep current): ")
        additional_info = input("Enter new additional information (press Enter to keep current): ")
        
        # Updates the contact information if the name is valid.
        if name:
            if validate_name(name):
                contacts[contact_id]["name"] = name
            else:
                print("Invalid name. Keeping the current one.")

        # Updates the contact information if the phone number is valid. And changes the identifier to the new phone number.        
        if phone:
            if validate_phone(phone):
                new_contact_id = phone
                contacts[new_contact_id] = contacts.pop(contact_id)
                contacts[new_contact_id]["phone"] = phone
            else:
                print("Invalid phone number. Keeping the current one.")

        # Updates the contact information if the email is valid.
        if email:
            if validate_email(email):
                contacts[contact_id]["email"] = email
            else:
                print("Invalid email address. Keeping the current one.")
        
        # Updates the contact information if the additional information is valid.
        if additional_info:
            contacts[contact_id]["additional_info"] = additional_info
        
        # Prints a success message if the contact is updated successfully.
        print("Contact updated successfully!")
    else:
        # Prints an error message if the contact is not found.
        print("Contact not found.")

# Function to delete a contact.
def delete_contact():
    # Prompts the user to enter the phone number of the contact to delete.
    print("\nDeleting a contact:")
    contact_id = input("Enter the phone number of the contact to delete: ")
    
    # Checks if the contact exists in the contacts dictionary and deletes it if found.
    if contact_id in contacts:
        del contacts[contact_id]

        # Prints a success message if the contact is deleted successfully.
        print("Contact deleted successfully!")
    else:
        # Prints an error message if the contact is not found.
        print("Contact not found.")

# Function to search for a contact.
def search_contact():
    # Prompts the user to enter the name or phone number to search for.
    print("\nSearching for a contact:")
    search_term = input("Enter name or phone number to search: ")
    
    # Creates a list to store the contact IDs of the found contacts.
    found_contacts = []

    # Searches for the contact based on the search term and adds the contact ID to the list if found.
    for contact_id, contact_info in contacts.items():
        # Checks if the search term is present in the name or phone number (case-insensitive). If found, adds the contact ID to the list.
        if search_term.lower() in contact_info["name"].lower() or search_term in contact_info["phone"]:
            found_contacts.append(contact_id)
    
    # Displays the found contacts or a message if no contacts are found.
    if found_contacts:
        print(f"Found {len(found_contacts)} contact(s):")
        for contact_id in found_contacts:
            display_contact(contact_id)
    else:
        print("No contacts found.")

# Function to display all contacts. Unless there are no contacts, in which case it prints a message.
def display_all_contacts():
    if contacts:
        print("\nAll contacts:")
        for contact_id in contacts:
            display_contact(contact_id)
    else:
        print("No contacts found.")

# Function to export contacts to a text file.
def export_contacts():
    filename = input("Enter the filename to export contacts (e.g., contacts.txt): ")
    try:

        # Writes the contact information to the specified file.
        with open(filename, 'w') as file:
            for contact_id, contact_info in contacts.items():
                file.write(f"{contact_id} | {contact_info['name']} | {contact_info['phone']} | {contact_info['email']} | {contact_info['additional_info']}\n")
        print(f"Contacts exported successfully to {filename}")
    # Handles the IOError exception if an error occurs while exporting contacts.
    except IOError:
        print("An error occurred while exporting contacts.")

# Function to import contacts from a text file.
def import_contacts():
    # Prompts the user to enter the filename to import contacts from.
    filename = input("Enter the filename to import contacts from (e.g., contacts.txt): ")

    # Reads the contact information from the specified file and adds it to the contacts dictionary.
    try:
        with open(filename, 'r') as file:
            for line in file:

                # Splits the line into contact data and adds it to the contacts dictionary.
                contact_data = line.strip().split(' | ')

                # Validates the contact data has the correct amount of data and adds it to the contacts dictionary if valid.
                if len(contact_data) == 5:
                    contact_id, name, phone, email, additional_info = contact_data
                    contacts[contact_id] = {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "additional_info": additional_info
                    }
        
        # Prints a success message if the contacts are imported successfully.
        print(f"Contacts imported successfully from {filename}")

    # Handles the IOError exception if an error occurs while importing contacts.
    except IOError:
        print("An error occurred while importing contacts.")

# Main function to display the menu and handle user input.
def main():

    # Displays the menu and handles user input until the user chooses to quit.
    while True:
        print("\nWelcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        
        # Stores the user choice in a variable.
        choice = input("Enter your choice (1-8): ")
        
        # Handles the user choice based on the input. And runs the corresponding function.
        try:
            if choice == '1':
                add_contact()
            elif choice == '2':
                edit_contact()
            elif choice == '3':
                delete_contact()
            elif choice == '4':
                search_contact()
            elif choice == '5':
                display_all_contacts()
            elif choice == '6':
                export_contacts()
            elif choice == '7':
                import_contacts()
            elif choice == '8':
                print("Thank you for using the Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        # Handles the ValueError exception if the input is not a number.
        except ValueError:
            print("Invalid input. Please enter a number.")

        # Instructions to press Enter to continue.
        finally:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()