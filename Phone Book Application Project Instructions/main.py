from contact import Contact
from business_contact import Business_contact
from phone_book import Phonebook

def main():
    phone_book = Phonebook()
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice: ")
    
        if choice == "1":
            name = input("\nEnter The Name: ")
            phone = input("Enter The Phone number: ")
            email = input("Enter The Email address: ")
            contact = Contact(name, phone, email)
            phone_book.add_contact(contact)
            print("Contact added successfully!")
        
        elif choice == "2":
            name = input("\nEnter the name of the contact to remove: ")
            contact = phone_book.search_contact(name)
            if contact:
                phone_book.remove_contact(contact)
                print("Contact Removed successfully!")
            else:
                print("Contact not found")

        elif choice == "3":
            name = input("\nEnter The name: ")
            contact = phone_book.search_contact(name)
            if contact:
                new_name = input("Enter The new Name: ")
                new_phone = input("Enter The new Phone number: ")
                new_email = input("Enter The new Email address: ")
                phone_book.update_contact(contact, new_name, new_phone, new_email)
                print("Contact Updeta successfully!")
            else:
                print("Contact not found")
                
        elif choice == "4":
            name = input("\nEnter the name of the contact to search: ")
            contact = phone_book.search_contact(name)
            if contact:
                print(f"\nThe name contact is: \n{contact}")
            else:
                print("\nThe name contact not found!")
                
        elif choice == "5":
            print("\nAll contacts:")
            phone_book.display_all_contact()
            
        elif choice == "6":
            total_contacts = phone_book.get_total_contact()
            print(f"\nTotal Contacts: {total_contacts}")
        
        
        elif choice == "7":
            name = input("\nEnter The Name: ")
            phone = input("Enter The Phone number: ")
            email = input("Enter The Email address: ")
            business_name = input("Enter The Business name: ")
            business_contact = Business_contact(name, phone, email, business_name)
            phone_book.add_contact(business_contact)
            print("\nBusiness contact added successfully!")
            
        elif choice == "8":
            print("\nExiting the program...")
            break
            
        else:
            print("\nInvalid choice.\nPlease try again.")
        
        



def display_menu():
    print("\nWelcome to my Phone Book Applicatin:")
    print()
    print("Here are your options:")
    print("\t1. Add Contact")
    print("\t2. Remove Contact")
    print("\t3. Uptate Contact")
    print("\t4. Search Contact")
    print("\t5. Display All Contacts")
    print("\t6. Total Contacts")
    print("\t7. Add Business Contact")
    print("\t8. Exit")

if __name__ == "__main__":
    main()