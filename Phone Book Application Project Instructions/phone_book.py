from contact import Contact

class Phonebook:
    def __init__(self):
        self._contacts = []
        
    def add_contact(self, contact):
        if isinstance(contact, Contact):
            self._contacts.append(contact)
        else:
            raise TypeError("This is not contact type.")
        
    def remove_contact(self, contact):
        if isinstance(contact, Contact):
            self._contacts.remove(contact)
        else:
            raise TypeError("This is not contact found.")
        
    def update_contact(self, contact, new_name, new_phone_number, new_email):
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        
    def search_contact(self, name):
        for contact in self._contacts:
            if contact.search(name):
                return contact
        return None
    
    def display_all_contact(self):
        for contact in self._contacts:
            print(contact)
            
    def get_total_contact(self):
        return len(self._contacts)
    
    def __add__(self, other):
        new_phone_book = Phonebook()
        new_phone_book._contacts = self._contacts + other._contacts
        return new_phone_book
        
    def __str__(self):
        for contact in self._contacts:
            print(contact)