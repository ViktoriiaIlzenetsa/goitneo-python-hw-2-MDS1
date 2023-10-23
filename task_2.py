from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, name):
        self.value = name

class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    def is_valid(self):
        if self.value.isdigit() and len(self.value) == 10:
            return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self, phone):
        self.phone = Phone(phone)
        if self.phone.is_valid():
            self.phones.append(self.phone)

    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                del self.phones[i]

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, new_record):
        self.data[new_record.name.value] = new_record

    def find(self, name):
        return self.data[name]
            
    def delete(self, name):
        del self.data[name]
        
