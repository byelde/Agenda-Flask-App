import json
from uuid import uuid4


def getContactList():
    with open("contacts.json", "r") as file:
        return json.load(file)


def saveContacts(contacts_list):
    with open("contacts.json", "w") as file:
        json.dump(contacts_list, file, indent=2)


def checkExists(contact_number):
    contacts_list = getContactList()

    for contact in contacts_list:
        if contact["number"] == contact_number:
            return True

        return False


def saveNewContact(new_contact):
    contacts_list = getContactList()
    new_contact["id"] = str(uuid4())

    contacts_list.append(new_contact)

    saveContacts(contacts_list)


def deleteContact(id):
    contacts_list = getContactList()
    contact = getContact(id)
    contacts_list.remove(contact)
    saveContacts(contacts_list)


def getContact(id):
    contacts_list = getContactList()

    for contact in contacts_list:
        if contact["id"] == id:
            return contact


def editContact(id, name, surname, number):
    contacts_list = getContactList()

    for contact in contacts_list:
        if contact["id"] == id:
            if name:
                contact["name"] = name
            if surname:
                contact["surname"] = surname
            if number:
                contact["number"] = number

    saveContacts(contacts_list)
