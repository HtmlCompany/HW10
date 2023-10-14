from collections import UserDict


class Field:
    def __init__(self, value:str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    def __init__(self, value:str) -> None:
        super().__init__(value)

    def __str__(self) -> str:
        return super().__str__()

class Phone(Field):
    def __init__(self, value:str) -> None:
        super().__init__(value)
        if (len(value) == 10) and (value.isdigit()):
            self.value = value
        else:
            raise ValueError

class Record:
    def __init__(self, name:str) -> None:
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, f_phone:str):
        for i in self.phones:
            if i.value == f_phone:
                self.phones.remove(i)
                print(f"Deleted phone: {i}")
    
    def edit_phone(self, old_phone: str, new_phone:str):
        counter = 0
        for i in self.phones:
            if i.value == old_phone:
                i.value = new_phone
                print(f"Old phone:{old_phone}, nwe phone: {new_phone}")
            else:
                counter += 1
                if counter == len(self.phones):
                    raise ValueError
            
    def find_phone(self, find_phone:str):
        for i in self.phones:
            if i.value == find_phone:
                return i

            
    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name:Name):
        if name in self.data.keys():
            return self.data[name]
        else:
            return None

    def delete(self, name:Name):
        if name in self.data.keys():
            self.data.pop(name)
            print(f"Deleted {name}")
        else:
            print(f"No contact {name} to delete")

book = AddressBook()

user1 = Record("Ramis")
user1.add_phone("1234567890")
user1.add_phone("2368368240")
user1.edit_phone("2368368240", "2368368241")
user2 = Record("Gela")
user2.add_phone("1234567890")
book.add_record(user1)
book.add_record(user2)

book.delete("Gela")

for name, record in book.data.items():
        print(record)