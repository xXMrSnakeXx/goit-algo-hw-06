from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
           super().__init__(value)
        else: 
            raise ValueError ("Give me name")   
        
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
         super().__init__(value)
        else:
            raise ValueError ("Not valid format") 
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        for current_phone in self.phones:
            if current_phone.value == phone:
                self.phones.remove(current_phone)
                
    def edit_phone(self, old_phone, new_phone):
        Phone(new_phone)
        for current_phone in self.phones:
            if current_phone.value == old_phone:
                current_phone.value = new_phone
                break  
        else:
            raise ValueError('Phone not found')             
    
    def find_phone(self, phone):
        for current_phone in self.phones:
            if current_phone.value == phone:
                return current_phone
                            

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
       return self.data.get(name)
   
    def delete(self, name):
        if name in self.data:
            del self.data[name]  
     





book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) 

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}") 

book.delete("Jane")