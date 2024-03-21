from datetime import datetime as dt
import re
from abc import ABC, abstractmethod


class Record:

    def __init__(self, name, phones='', birthday='', email='', status='', note=''):
        self.birthday = birthday
        self.name = name
        self.phones = phones
        self.email = email
        self.status = status
        self.note = note

    def days_to_birthday(self):
        current_datetime = dt.now()
        birthday = self.birthday.replace(year=current_datetime.year)
        if birthday < current_datetime:
            birthday = birthday.replace(year=current_datetime.year + 1)
        return (birthday - current_datetime).days


class Field(ABC):

    def __init__(self, value=''):
        self._value = self.get_value(value)

    @property
    def value(self):
        return self._value

    @abstractmethod
    def get_value(self, value):
        pass


class Name(Field):
    def get_value(self, value):
        return value.strip()


class Phone(Field):

    def get_value(self, value):
        while True:
            if value:
                values = value
            else:
                values = input("Phones(+38..........) (multiple phones can be added with space between them. +38 pattern has 9 symbols after code): ")
            try:
                return [number for number in values.split() if re.match(r'^\+48\d{9}$', number) or re.match(r'^\+38\d{10}$', number) or number == '']
            except ValueError:
                print('Incorrect phone number format! Please provide correct phone number format.')


class Birthday(Field):

    def get_value(self, value):
        while True:
            if value:
                date = value
            else:
                date = input("Birthday date(dd/mm/YYYY): ")
            try:
                if re.match(r'^\d{2}/\d{2}/\d{4}$', date):
                    return dt.strptime(date.strip(), "%d/%m/%Y")
                elif not date:
                    return ''
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')


class Email(Field):

    def get_value(self, value):
        while True:
            if value:
                email = value
            else:
                email = input("Email: ")
            try:
                if re.match(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', email) or not email:
                    return email
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')


class Status(Field):

    def get_value(self, value):
        status_types = ['', 'family', 'friend', 'work']
        while True:
            if value:
                status = value
            else:
                status = input("Type of relationship (family, friend, work): ")
            if status in status_types:
                return status
            print('There is no such status!')


class Note(Field):
    def get_value(self, value):
        return value.strip()


class UserInterface(ABC):
    @abstractmethod
    def show_record(self, record: Record):
        pass

    @abstractmethod
    def show_notes(self, notes: list):
        pass

    @abstractmethod
    def show_help(self):
        pass


class ConsoleInterface(UserInterface):
    def show_record(self, record: Record):
        print("Name:", record.name)
        print("Phones:", record.phones)
        print("Birthday:", record.birthday)
        print("Email:", record.email)
        print("Status:", record.status)
        print("Note:", record.note)

    def show_notes(self, notes: list):
        for i, note in enumerate(notes):
            print(f"{i + 1}. {note}")

    def show_help(self):
        print("Available commands:")
        print("1. show <contact_name> - Show details of a contact")
        print("2. list - List all contacts")
        print("3. notes - Show all notes")
        print("4. help - Show available commands")