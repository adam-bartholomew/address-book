# Embedded file name: menu.py
import os
import xml.etree.ElementTree as elementTree
import addressbook as ab
from termcolor import colored

MSG_NO_ADDRESSBOOK = "\nNO ADDRESSBOOK IN USE"
INPUT_LAST_NAME = "Please enter last name of person: "
INPUT_FIRST_NAME = "Please enter first name of person: "


def menu():
    addressbook = None
    doc = None
    while True:
        os.system("cls")
        print(colored("MY ADDRESS BOOK", 'blue', attrs=['bold', 'underline']) + colored(':', 'blue', attrs=['bold']))
        print(colored("A. Create Empty Addressbook", 'white'))
        print(colored("B. Read Addressbook from a File", 'white'))
        print(colored("C. Add Person to Addressbook", 'white'))
        print(colored("D. Remove a Person", 'white'))
        print(colored("E. Print a Specific Person", 'white'))
        print(colored("F. Print All People", 'white'))
        print(colored("G. Write Address Book to a File", 'white'))
        print(colored("H. Update a Specific Person", 'white'))
        print(colored("I. Create a New Group", 'white'))
        print(colored("J. Remove a Group", 'white'))
        print(colored("K. Add Member to a Group", 'white'))
        print(colored("L. Remove a Member from a Group", 'white'))
        print(colored("M. Print Names of Group Members", 'white'))
        print(colored("X. Exit Program", 'light_red'))
        print()
        selected = input("Enter menu selection: ").upper()
        if selected in 'ABCDEFGHIJKLMX':
            if selected == 'A':
                doc = ab.create_address_book()
                addressbook = doc.getroot()
                print("\nNEW EMPTY ADDRESSBOOK CREATED")
            elif selected == 'B':
                name = input("Please enter name of file to read from: ")
                if os.path.exists(name) and name.endswith('.xml'):
                    doc = elementTree.parse(name)
                    addressbook = doc.getroot()
                    print("\nFILE: {name} :OPENED")
                elif os.path.exists(name) and name.endswith('.csv'):
                    doc = ab.create_address_book()
                    addressbook = doc.getroot()
                    csv = open(name, 'rt')
                    csv.readline()
                    line = csv.readline()
                    line = line.replace('\n', '')
                    while len(line) > 0:
                        split = line.split(',')
                        last_name = split[0].capitalize()
                        first_name = split[1].capitalize()
                        birthday = split[2]
                        phone_number = split[3]
                        street_address = split[4]
                        ab.add_person(addressbook, last_name, first_name, birthday, phone_number, street_address)
                        line = csv.readline()
                        line = line.replace('\n', '')

                    print(f"\nFILE: {name} :OPENED")
                else:
                    print(f"\nSORRY, FILE: {name} :NOT FOUND")
            elif selected == 'C':
                if addressbook is not None:
                    last_name = input(INPUT_LAST_NAME).capitalize()
                    first_name = input(INPUT_FIRST_NAME).capitalize()
                    birthday = input("Please enter birthday of person: ")
                    phone_number = input("Please enter phone number of person: ")
                    street_address = input("Please enter street address of person: ")
                    new_person = ab.add_person(addressbook, last_name, first_name, birthday, phone_number, street_address)
                    if new_person:
                        print(f"\nCONTACT: {first_name} {last_name} :SUCCESSFULLY ADDED")
                    else:
                        print(f"\nCONTACT: {first_name} {last_name} :ALREADY EXISTS")
                else:
                    print(f"\nPLEASE CHOOSE A FILE FIRST")
            elif selected == 'D':
                if addressbook is not None:
                    last_name = input(INPUT_LAST_NAME).capitalize()
                    first_name = input(INPUT_FIRST_NAME).capitalize()
                    if ab.remove_person(addressbook, last_name, first_name):
                        print(f"\nCONTACT: {first_name} {last_name} :HAS BEEN REMOVED")
                    else:
                        print(f"\nSORRY, CONTACT: {first_name} {last_name} :NOT FOUND")
                else:
                    print(f"\nPLEASE CHOOSE A FILE FIRST")
            elif selected == 'E':
                if addressbook is not None:
                    last_name = input(INPUT_LAST_NAME).capitalize()
                    first_name = input(INPUT_FIRST_NAME).capitalize()
                    print(f"\nCONTACT INFORMATION")
                    if ab.print_person(addressbook, last_name, first_name):
                        print()
                    else:
                        print(f"\nSORRY, CONTACT: {first_name} {last_name} :NOT FOUND")
                else:
                    print(f"\nPLEASE CHOOSE A FILE FIRST")
            elif selected == 'F':
                if addressbook is not None:
                    print(f"\nALL CONTACT INFORMATION")
                    ab.print_all(addressbook)
                else:
                    print(f"\nPLEASE CHOOSE A FILE FIRST")
            elif selected == 'G':
                if addressbook is not None:
                    name = input("Please enter name of file to write to: ")
                    if name.endswith('.xml'):
                        doc.write(name)
                        print(f"\nFILE SAVE TO: {name} :SUCCESSFUL")
                    elif name.endswith('.csv'):
                        f = open(name, 'wt')
                        f.write('last_name,first_name,birthday,phone_number,street_address,groups\n')
                        for person in addressbook:
                            last_name = person.get('last_name')
                            first_name = person.get('first_name')
                            birthday = person.findtext('birthday')
                            phone = person.findtext('phone_number')
                            street = person.findtext('street_address')
                            f.write(last_name + ',' + first_name + ',' + birthday + ',' + phone + ',' + street + ',' + 'groups' + '\n')

                        f.close()
                        print(f"\nFILE SAVE TO: {name} :SUCCESSFUL")
                    else:
                        print(f"\nPLEASE ENTER A VALID FILE WITH CORRECT EXTENSION")
                else:
                    print(f"\nPLEASE CHOOSE A FILE FIRST")
            elif selected == 'H':
                if addressbook is not None:
                    last_name = input(INPUT_LAST_NAME).capitalize()
                    first_name = input(INPUT_FIRST_NAME).capitalize()
                    birthday = input("Please enter new birthday of person: ")
                    phone_number = input("Please enter new phone number of person: ")
                    street_address = input("Please enter new street address of person: ")
                    updated_person = ab.update_person(addressbook, last_name, first_name, birthday, phone_number, street_address)
                    if updated_person:
                        print(f"\nCONTACT: {first_name} {last_name} :UPDATED")
                    else:
                        print(f"\nPERSON: {first_name} {last_name} :DOES NOT EXIST")
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'I':
                if addressbook is not None:
                    group_name = input("Please enter name of the new group: ")
                    group = ab.add_group(addressbook, group_name)
                    if not group:
                        print(f"\nGROUP: {group_name} :ALREADY EXISTS")
                    elif group:
                        print(f"\nGROUP: {group_name} :ADDED")
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'J':
                if addressbook is not None:
                    group_name = input("Please enter name of the new group: ")
                    group = ab.remove_group(addressbook, group_name)
                    if group:
                        print("\nGROUP: {group_name} :REMOVED")
                    else:
                        print("\nGROUP: {group_name} :DOES NOT EXIST")
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'K':
                if addressbook is not None:
                    title = input("Please enter the title of the group you wish to add to: ")
                    last_name = input("Please enter the last name of the new member: ")
                    first_name = input("Please enter the first name of the new member: ")
                    group = ab.find_group(addressbook, title)
                    if group == 1:
                        new = ab.add_member(addressbook, title, last_name, first_name)
                        if new == 1:
                            print()
                            print(f"MEMBER: {last_name}, {first_name} :ALREADY EXISTS IN GROUP: {title}")
                        elif new == 2:
                            print(f"\nMEMBER: {last_name}, {first_name} :ADDED TO GROUP: {title}")
                        elif new == 4:
                            print(f"\nMEMBER {last_name}, {first_name} DOES NOT EXIST")
                    else:
                        print(f"\nGROUP: {title} :DOES NOT EXIST")
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'L':
                if addressbook is not None:
                    title = input("Please enter the title of the group you wish to remove from: ")
                    last_name = input("Please enter the last name of the member to be removed: ")
                    first_name = input("Please enter the first name of the member to be removed: ")
                    group = ab.find_group(addressbook, title)
                    if group:
                        msg = ab.remove_member(addressbook, title, last_name, first_name)
                        if msg == 1:
                            print(f"MEMBER {last_name}, {first_name} WAS REMOVED FROM GROUP {title}")
                        elif msg == 3:
                            print(f"GROUP {title} WAS NOT FOUND")
                        else:
                            print(f"PERSON {last_name}, {first_name} WAS NOT FOUND")
                    else:
                        print(f"\nGROUP {title} WAS NOT FOUND")
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'M':
                if addressbook is not None:
                    ab.print_group_members(addressbook)
                else:
                    print(MSG_NO_ADDRESSBOOK)
            elif selected == 'X':
                if addressbook is None:
                    print("PROGRAM TERMINATED")
                    return selected
                ans = input('Would you like to save your addressbook? (Y/N): ').upper()
                if ans == 'Y' or ans == 'YES':
                    name = input('Save your addressbook as: ')
                    if name.endswith('.xml'):
                        doc.write(name)
                        print(f"\nYOUR ADDRESS BOOK HAS BEEN SAVED AS: {name}")
                        return selected
                    if name.endswith('.csv'):
                        f = open(name, 'wt')
                        f.write('last_name,first_name,birthday,phone_number,street_address\n')
                        for person in addressbook:
                            last_name = person.get('last_name')
                            first_name = person.get('first_name')
                            birthday = person.findtext('birthday')
                            phone = person.findtext('Phone_number')
                            street = person.findtext('street_address')
                            f.write(last_name + ',' + first_name + ',' + birthday + ',' + phone + ',' + street + '\n')

                        f.close()
                        print(f"\nYOUR ADDRESS BOOK HAS BEEN SAVED AS: {name}")
                        print(f"PROGRAM TERMINATED")
                        return selected
                    print(f"\nPLEASE ENTER A VALID FILE NAME WITH CORRECT EXTENSION")
                else:
                    if ans == 'N' or ans == 'NO':
                        print(f"\nADDRESS BOOK NOT SAVED")
                        print(f"PROGRAM TERMINATED")
                        return selected
                    print(f"\nPLEASE ENTER CORRECT RESPONSE")
            print()
            print('\n', input(colored("Press RETURN to continue", 'light_green', attrs=['blink'])))
        else:
            print(f"PLEASE ENTER A VALID SELECTION")
            print(input(colored("Press RETURN to continue", 'light_green', attrs=['blink'])))


if __name__ == "__main__":
    menu()
