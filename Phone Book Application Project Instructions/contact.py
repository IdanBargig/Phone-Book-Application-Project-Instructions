from searchable import Searchable

class Contact(Searchable):
    def __init__(self, name, phone_number, email):
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
    
    @property
    def name(self):
        return self.__name
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def email(self):
        return self.__email
    
    @name.setter
    def name(self, value):
            self.__name = value       
                
    @phone_number.setter
    def phone_number(self, value):
            self.__phone_number = value
                
    @email.setter
    def email(self, value):
            self.__email = value
    
    def __str__(self):
        return f"name: {self.__name}\nphone number: {self.__phone_number}\nemail: {self.__email}"
    
    def search(self, name):
        return self.__name.lower() == name.lower()