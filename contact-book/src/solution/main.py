class Contact_book():

    def __init__(self):
        self.contacts = {}

    def create_contact(self, name:str, phone:str = None, email:str = None):
        """
        Adds a new contact to the contact book.

        :param str name: The name of the contact
        :param str phone: The phone number of the contact
        :param str email: The email address of the contact
        :param str address: The physical address of the contact
        """
        if name in self.contacts:
            print("contact is already exist")
        else:
            self.contacts[name] = {}
            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email


    def view_contact(self,name:str):
        """
        view all contact that create in contact book
        :param str name: The name of the contact
        """
        if name in self.contacts:
            for name , info in self.contacts.items():
                print(f"name: {name}")
                print(f"phone: {info['phone']}")
                print(f"email: {info['email']}")

        else:
           print("contact doesn't exist")


    def delete_contact(self,name:str):
        """
        delete a contact from contact book
        :param str name: The name of the contact
        """
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} has been deleted.")
        else:
            print(f"No contact found with the name {name} to delete.")


    def update_contact(self,name:str ,phone:str, email:str):
        """
        update a contact in contact book
        :param str name: The name of the contact
        :param str phone: The phone number of the contact
        :param str email: The email address of the contact
        :param str address: The physical address of the contact
        """
        if name in self.contacts:
            if phone: 
                self.contacts[name]['phone'] = phone

            if email:
               self.contacts[name]['email'] = email


if __name__ == "__main__":
  book = Contact_book()
  while True:
    
    
    print("1: create a contact number")
    print("2: view a contact number")
    print("3: delete a contact number")
    print("4: update a contact number ")
    print("5: quit") 
    choices =input("choose an option: ")

    if choices == "1":
        name = input("give a name: ")
        phone = input("give a phone number: ")
        email = input("give an email: ")
        book.create_contact(name,phone,email)

    elif choices == "2": 
        name = input("give a name: ")  
        book.view_contact(name)

    elif choices == "3":
        name = input("give a name: ")  
        book.delete_contact(name)

    elif choices == "4":
        name = input("give a name: ")
        phone = input("give a phone number: ")
        email = input("give an email: ")
        book.update_contact(name,phone,email)

    else:
        break    





                

                               

       