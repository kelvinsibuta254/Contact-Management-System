contacts = []# will serve as our database to store our info since we don't have a db, should also be passed as a parameter
def add_contact(name, number, email):
    contact = {
        "name": name,
        "number": number,
        "email": email
    }
    contacts.append(contact)
    print(f"Contact {name} added successfully")

def view_contact(contacts):
    if not contacts:
        print("No contact found")
        return
    for contact in contacts:
        print(f"Name: {contact["name"]} Number: {contact["number"]} email: {contact["email"]}")

def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name: {contact["name"]} Number: {contact["number"]} email: {contact["email"]}")
            #return
    print(f"{name} not found")

def update_contact(name, new_number=None, new_email = None):#This params are paceholders, its when you call this function is when you're going to provide real details, new_name and new_email replace the old ones that are on the list already
    for contact in contacts:
        if contact["name"]:
            if new_number:
                contact["number"] = new_number# if the number is on the list, replace with the new number
            if new_email:
                contact["email"] = new_email
                return
    print(f"{name} not found")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"]:
            contacts.remove(contact)
            print(f"{name} removed successfully")
            return
        print(f"{name} not found") 