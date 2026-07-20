# MINI CONTACT BOOK PROJECT

import json
import os
contacts = []

# Task 1: Save Contacts

def save_contacts():
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
    except Exception:
        print("Error saving contacts.")



# Task 2: Load Contacts

def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as file:
                contacts = json.load(file)
        except Exception:
            print("Error loading contacts.")
            contacts = []
    else:
        contacts = []

load_contacts()


# Task 3: Add Contact

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
        save_contacts()
        print("Contact saved successfully.")

    else:
        print("Error: Phone number must contain only digits.")



# Task 4: View All Contacts

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n========== ALL CONTACTS ==========")
        for contact in contacts:
            print(f"Name  : {contact['Name']}")
            print(f"Phone : {contact['Phone']}")
            print(f"Email : {contact['Email']}")
            print("---------------------------------")



# Task 5: Search Contact

def search_contact():
    name = input("Enter contact name to search: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print("\n====== CONTACT FOUND ======")
            print(f"Name  : {contact['Name']}")
            print(f"Phone : {contact['Phone']}")
            print(f"Email : {contact['Email']}")
            print("---------------------------")
            return
    print("Contact not found.")



# Task 6: Delete Contact

def delete_contact():
    name = input("Enter contact name to delete: ")
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts()
            print(f"{contact['Name']} deleted successfully.")
            return
    print("Contact not found.")


# Main Menu

while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
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
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Please try again.")
