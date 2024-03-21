from AddressBook import *


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            self.add_contact()
        elif action == 'search':
            self.search_contact()
        elif action == 'edit':
            self.edit_contact()
        elif action == 'remove':
            self.remove_contact()
        elif action == 'save':
            self.save_address_book()
        elif action == 'load':
            self.load_address_book()
        elif action == 'congratulate':
            self.congratulate_birthdays()
        elif action == 'view':
            self.view_address_book()
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")

    def add_contact(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        self.book.add(record)

    def search_contact(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = self.book.search(pattern, category)
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

    def edit_contact(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        self.book.edit(contact_name, parameter, new_value)

    def remove_contact(self):
        pattern = input("Remove (contact name or phone): ")
        self.book.remove(pattern)

    def save_address_book(self):
        file_name = input("File name: ")
        self.book.save(file_name)

    def load_address_book(self):
        file_name = input("File name: ")
        self.book.load(file_name)

    def congratulate_birthdays(self):
        print(self.book.congratulate())

    def view_address_book(self):
        print(self.book)