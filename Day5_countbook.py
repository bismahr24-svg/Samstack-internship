# -MINI COUNTBOOK PROJECT-

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


# Task 1: Project Structure & Loop

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice.Try again.")


