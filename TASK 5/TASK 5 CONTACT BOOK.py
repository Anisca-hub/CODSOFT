# TASK 5 - CONTACT BOOK
contacts = {}

def add_contact():
    name = input ("👤 Enter name : ").strip()
    if name in contacts:
        print ("⚠️ Contact already exists.")
        return 
    phone = input ("📞 Enter phone number : ").strip()
    email = input ("📧 Enter email : ").strip()
    address = input ("🏠 Enter address : ").strip()
    contacts[name] = {"phone" : phone, "email" : email, "address" : address}
    print ("✅ Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print ("📪 No contacts found.\n")
        return
    print ("\n📘 Contact List : ")
    for name, info in contacts.items():
        print (f"👤 Name : {name}, 📞 Phone : {info['phone']}")
        print ()

def search_contact():
    query = input ("🔍 Enter name or phone number to search : ").strip()
    found = False
    for name, info in contacts.items():
        if query.lower() in name.lower() or query == info['phone']:
            print (f"\n👤 Name : {name}")
            print (f"📞 Phone : {info['phone']}")
            print (f"📧 Email : {info['email']}")
            print (f"🏠 Address : {info['address']}\n")
            found = True
    if not found:
            print ("❌ Contact not found.\n") 

def update_contact():
    name = input ("✏️  Enter the name of the contact to update : ").strip()
    if name not in contacts:
        print ("❌ Contact not found.\n")
        return 
    print ("📝 Leave field empty to keep current value.")
    phone = input (f"📞 Enter new phone number (Current : {contacts[name]['phone']}) : ").strip()
    email = input (f"📧 Enter new email (Current : {contacts[name]['email']}) : ").strip()
    address = input (f"🏠 Enter new address (Current : {contacts[name]['address']}) : ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    print ("✅ Contact updated successfully!\n")

def delete_contact():
    name = input ("🗑️  Enter the name of the contact to delete : ").strip()
    if name in contacts:
        del contacts[name]
        print ("🗑️  Contact deleted successfully!\n")
    else:
        print ("❌ Contact not found.\n")

def main():
    while True:
        print ("📙------ CONTACT BOOK ------📗")
        print ("1️⃣  Add Contact") 
        print ("2️⃣  View Contact List") 
        print ("3️⃣  Search Contact") 
        print ("4️⃣  Update Contact") 
        print ("5️⃣  Delete Contact") 
        print ("6️⃣  Exit")
        choice = input ("👉 Enter your choice : ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print ("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print ("⚠️ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()                               




