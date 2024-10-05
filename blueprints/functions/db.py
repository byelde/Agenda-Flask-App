import json

def getContacts():
    with open("contacts.json", "r") as file:
        return json.load(file)


def saveContacts(contacts_list):
    with open("contacts.json", "w") as file:
        file.write(json.dumps(contacts_list, indent=2))


def saveNewContact(new_contac):
    all_contacts_list = getContacts()

    all_contacts_list.append(new_contac)

    with open("contacts.json", "w") as file:
        file.write(json.dumps(all_contacts_list, indent=2))


def deleteContact(id):
    all_contacts_list = getContacts()
    contact = findContact(id)
    all_contacts_list.remove(contact)
    saveContacts(all_contacts_list)


def checkExists(input_contact):
    all_contacts_list = getContacts()

    for contact in all_contacts_list:
        if contact["number"] == input_contact["number"]:
            return True
        
        return False
    

def editContact(id, name, surname, number):
    all_contacts_list = getContacts()

    for contact in all_contacts_list:
        if contact["id"] == id:
            if name: contact["name"] = name
            if surname: contact["surname"] = surname
            if number: contact["number"] = number

    saveContacts(all_contacts_list)

    
def findContact(id):
    all_contacts_list = getContacts()

    for contact in all_contacts_list:
        if contact["id"] == id:
            return contact