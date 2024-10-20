import json

class ContactManager:
    def __init__(self, filename="my_contacts.json"):
        self.filename = filename
        try:
            with open(self.filename, "r") as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = {}

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent = 4)

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists..")
        else:
            self.contacts[name] = phone
            self.save_contacts()
            print(f"Contact '{name}' added successfully..")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact '{name}' deleted successfully..")
        else:
            print(f"Contact with name '{name}' not found.. :(")

    def rename_contact(self, old_name, new_name):
        if old_name in self.contacts:
            self.contacts[new_name] = self.contacts.pop(old_name)
            self.save_contacts()
            print(f"Contact '{old_name}' renamed to '{new_name}' successfully..")
        else:
            print(f"Contact with name '{old_name}' not found.. :(")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.. :(")
        else:
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Rename Contact")
        print("4. Display Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            manager.add_contact(name, phone)
        elif choice == "2":
            name = input("Enter name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == "3":
            old_name = input("Enter current name: ")
            new_name = input("Enter new name: ")
            manager.rename_contact(old_name, new_name)
        elif choice == "4":
            manager.display_contacts()
        elif choice == "5":
            print("Exiting the program....")
            break
        else:
            print("Invalid choice. Please enter valid value...")

if __name__ == "__main__":
    main()
