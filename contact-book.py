import sqlite3

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# # initiate the db
# cursor.execute("CREATE TABLE contacts (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, email TEXT, phone_number TEXT, address TEXT)")
# data_person_name = [('Michael', 'Fox', "miacheal.fox@email.com", "01234567890", "Mike's address"),
#                     ('Adam', 'Miller', "adam.miller@email.com", "01234567890", "Adam's address"),
#                     ('Andrew', 'Peck', "andrew.peck@email.com", "01234567890", "Andy's address"),
#                     ('James', 'Shroyer', "james.shrover@email.com", "01234567890", "James' address"),
#                     ('Eric', 'Burger', "eric.burger@email.com", "01234567890", "Eric's address")
#                     ]
# cursor.executemany('INSERT INTO contacts(name, surname, email, phone_number, address) VALUES (?, ?, ?, ?, ?)', data_person_name)
# conn.commit()


while True:
    print("What do you want to do? \n A-add new contact; M-modify the existing contact, D-delete an entry, S-show all entries,  Q-quit")
    ans = input("").lower()

    if ans == 's':
        rows = cursor.execute("SELECT *  FROM contacts").fetchall()
        [print(row) for row in rows]
    elif ans == 'a':
        print("What's your contact's name?")
        name = input("")

        print("What's your contact's surname?")
        surname = input("")

        print("What's your contact's email address?")
        email = input("")

        print("What's your contact's mobile phone number?")
        phone = input("")

        print("What's your contact's address?")
        address = input("")

        # save the answers in db
        new_entry = [(name, surname, email, phone, address)]
        cursor.executemany("INSERT INTO contacts(name, surname, email, phone_number, address) VALUES (?, ?, ?, ?, ?)", new_entry)
        conn.commit()

        # next steps
        print('Your new contact has been added! Do you want to review all the entries? \n Y/N')
        review = input("").lower()
        if review == 'y':
            print(f"New contact's name: {name}")
            print(f"New contact's surname: {surname}")
            print(f"New contact's email: {email}")
            print(f"New contact's mobile phone: {phone}")
            print(f"New contact's address: {address}")
            print("-----------------------")
            continue
        else:
            print("Thanks, that's all!")
            break

    elif ans in ['m', 'd']:
        print("Which contact would you like to modify? Type ID")
        rows = cursor.execute("SELECT * FROM contacts").fetchall()
        [print(row) for row in rows]

        select_id = input("")
        selected_list = cursor.execute(
            "SELECT * FROM contacts WHERE id = ?",
            (select_id,)).fetchall()

        selected_tuple = selected_list[0]
        num_rows = len(selected_list)

        if num_rows < 1:
            print("There's no such name, try again")
            continue
        else:
            if ans == 'd':
                print(f"You're going to delete the following entry: \n {selected_tuple}")
                cursor.execute(
                    "DELETE FROM contacts WHERE id = ?",
                    (select_id))
                conn.commit()
                print("Entry deleted")

            else:
                print(f"You're going to modify the following entry: \n {selected_tuple}")
                print("Now, which entry would you like to modify? \n N-name; S-surname; E-email; P-phone number; A-adrress; Q-finished")
                choice = input("").upper()

                if choice == 'Q':
                    print("All finished, thanks!")
                    break
                elif choice in ["N", "S", "E", "P", "A"]:
                    print("What's the new value")
                    entry = input("")

                    lookup_dict = {"N": "name", "S": "surname", "E": "email", "P": "phone_number", "A": "address"}
                    mod_dict = {"id": select_id, "name": selected_tuple[1], "surname": selected_tuple[2], "email": selected_tuple[3], "phone_number": selected_tuple[4], "address": selected_tuple[5]}

                    mod_dict[lookup_dict[choice]] = entry
                    sql = ''' UPDATE contacts SET 
                                    name =:name,
                                    surname =:surname,
                                    email =:email,
                                    phone_number =:phone_number,
                                    address =:address
                                    WHERE id =:id'''
                    cursor = conn.execute(sql, mod_dict)
                    conn.commit()

                    selected_list = cursor.execute(
                        "SELECT name, surname, email, phone_number, address FROM contacts WHERE id = ?",
                        (select_id, )).fetchall()
                    selected_tuple = selected_list[0]
                    print("Entry updated!")
                    print(selected_tuple)
                    continue
                else:
                    print("Your answer doesn't contain either of N, S, E, P, A or Q. Try again")
                    continue
    elif ans == 'q':
        if conn:
            conn.close()
        break

    else:
        print("Wrong answer! \n Choose between A-add new contact; M-modify the existing contact, Q-quit")



