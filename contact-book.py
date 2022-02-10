class Contact(object):

    def __init__(self, name):
        self.name = name
        self.surname = None
        self.email = None
        self.mobile_phone = None
        self.address = None

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def email(self):
        return self._email

    @property
    def mobile_phone(self):
        return self._mobile_phone

    @property
    def address(self):
        return self._address


    @name.setter
    def name(self, new_name):
        if new_name is None:
            self._name = new_name
        elif isinstance(new_name, str):
            self._name = new_name
        else:
            print("Name must be a character string")

    @surname.setter
    def surname(self, new_surname):
        if new_surname is None:
            self._surname = new_surname
        elif isinstance(new_surname, str):
            self._surname = new_surname
        else:
            print("Surname must be a character string")

    @email.setter
    def email(self, new_email):
        if new_email is None:
            self._email = new_email
        elif isinstance(new_email, str):
            if '@' not in new_email:
                print("Email must be valid and contain @")
            else:
                self._email = new_email
        else:
            print("Email must be a character string")

    @mobile_phone.setter
    def mobile_phone(self, new_mobile_phone):
        if new_mobile_phone is None:
            self._mobile_phone = new_mobile_phone
        elif isinstance(new_mobile_phone, str):
            self._mobile_phone = new_mobile_phone
        else:
            print("Mobile phone must be a character string")

    @address.setter
    def address(self, new_address):
        if new_address is None:
            self._address = new_address
        elif isinstance(new_address, str):
            self._address = new_address
        else:
            print("Address must be a character string")

    @name.deleter
    def name(self):
        del self._name

    @surname.deleter
    def surname(self):
        del self._surname

    @email.deleter
    def email(self):
        del self._email

    @mobile_phone.deleter
    def mobile_phone(self):
        del self._mobile_phone

    @address.deleter
    def address(self):
        del self._address


# TODO initiate a SQL db
while True:
    print("What do you want to do? \n A-add new contact; M-modify the existing contact, Q-quit")
    ans = input("").lower()

    if ans == 'a':
        print("What's your contact's name?")
        name = input("")
        contact = Contact(name)
        print("What's your contact's surname?")
        surname = input("")
        contact.surname = surname
        print("What's your contact's email address?")
        email = input("")
        contact.email = email
        print("What's your contact's mobile phone number?")
        phone = input("")
        contact.mobile_phone = phone
        print("What's your contact's address?")
        address = input("")
        contact.address = address

        # TODO save the contact to the DB

        print('Your new contact has been added! Do you want to review all the entries? \n Y/N')
        review = input("").lower()
        if review == 'y':
            print(f"New contact's name: {contact.name}")
            print(f"New contact's surname: {contact.surname}")
            print(f"New contact's email: {contact.email}")
            print(f"New contact's mobile phone: {contact.mobile_phone}")
            print(f"New contact's address: {contact.address}")
            print("-----------------------")
            continue
        else:
            print("Thanks, that's all!")
            break

    elif ans == 'm':
        # print("Which contact would you like to modify? Type row number)
        # TODO retrieve all the entries from the SQL db
        print("TBC")

    elif ans == 'q':
        break

    else:
        print("Wrong answer! \n Choose between A-add new contact; M-modify the existing contact, Q-quit")
