# - MINI CONTACT BOOK PROJECT -

contacts = []

# Task 2: Add Contact Functionality

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    if phone.isdigit():
        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email
        }
        contacts.append(contact)
        print("Contact saved successfully.")
    else:
        print("Error: Phone number must contain only digits.")


# Task 3: View All Contacts

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found")
    else:
        print("\n--- All Contacts ---")
        for contact in contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("--------------------")


# Task 4: Search Contact

def search_contact():
    name = input("Enter the name of the contact you want to search for: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print("\n--- Contact Found ---")
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("--------------------")
            return
    print("Contact not found.")


# Task 5: Delete Contact

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact", contact["Name"], "deleted successfully.")
            return
    print("Cannot delete: Contact not found.")


# Main Menu

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Try again.")
      
