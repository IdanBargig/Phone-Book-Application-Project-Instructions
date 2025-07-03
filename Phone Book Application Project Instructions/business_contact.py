from contact import Contact

class Business_contact(Contact):
    def __init__(self, name, phone_number, email, business_name):
        super().__init__(name, phone_number, email)
        self.__business_name = business_name
        
    @property
    def business_name(self):
        return self.__business_name
    
    @business_name.setter
    def business_name(self, value):
        if isinstance(value, str):  
            if len(value) > 0:
                self.__business_name = value
    
    def __str__(self):
        return f"{super().__str__()}\nThe business name is: {self.__business_name}"
    
    def search(self, name):
        return super().search(name)