# Embedded file name: menu.py
import os
import xml.etree.ElementTree as elementTree
import addressbook as ab
from termcolor import colored, cprint

def menu():
    addressbook = None
    doc = None
    while True:
        os.system('cls')
        print(colored('MY ADDRESS BOOK', 'blue', attrs=['bold', 'underline']) + colored(':', 'blue', attrs=['bold']))
        print(colored('A. Create Empty Addressbook', 'white'))
        print(colored('B. Read Addressbook from a File', 'white'))
        print(colored('C. Add Person to Addressbook', 'white'))
        print(colored('D. Remove a Person', 'white'))
        print(colored('E. Print a Specific Person', 'white'))
        print(colored('F. Print All People', 'white'))
        print(colored('G. Write Address Book to a File', 'white'))
        print(colored('H. Update a Specific Person', 'white'))
        print(colored('I. Create a New Group', 'white'))
        print(colored('J. Remove a Group', 'white'))
        print(colored('K. Add Member to a Group', 'white'))
        print(colored('L. Remove a Member from a Group', 'white'))
        print(colored('M. Print Names of Group Members', 'white'))
        print(colored('X. Exit Program', 'light_red'))
        print()
        selected = input('Enter menu selection: ').upper()
        if selected in 'ABCDEFGHIJKLMX':
            if selected == 'A':
                doc = ab.createAddressBook()
                addressbook = doc.getroot()
                print()
                print('NEW EMPTY ADDRESSBOOK CREATED')
            elif selected == 'B':
                name = input('Please enter name of file to read from: ')
                if os.path.exists(name) and name.endswith('.xml'):
                    doc = elementTree.parse(name)
                    addressbook = doc.getroot()
                    print()
                    print('FILE: ' + name + ' :OPENED')
                elif os.path.exists(name) and name.endswith('.csv'):
                    doc = ab.createAddressBook()
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
                        ab.addPerson(addressbook, last_name, first_name, birthday, phone_number, street_address)
                        line = csv.readline()
                        line = line.replace('\n', '')

                    print()
                    print('FILE: ' + name + ' :OPENED')
                else:
                    print()
                    print('SORRY, FILE: ' + name + ' :NOT FOUND')
            elif selected == 'C':
                if addressbook is not None:
                    last_name = input("Please enter last name of person: ").capitalize()
                    first_name = input("Please enter first name of person: ").capitalize()
                    birthday = input('Please enter birthday of person: ')
                    phone_number = input('Please enter phone number of person: ')
                    street_address = input('Please enter street address of person: ')
                    new_person = ab.addPerson(addressbook, last_name, first_name, birthday, phone_number, street_address)
                    if new_person:
                        print()
                        print('CONTACT: ' + first_name + ' ' + last_name + ' :SUCCESSFULLY ADDED')
                    else:
                        print()
                        print('CONTACT: ' + first_name + ' ' + last_name + ' :ALREADY EXISTS')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'D':
                if addressbook is not None:
                    last_name = input("Please enter last name of person: ").capitalize()
                    first_name = input("Please enter first name of person: ").capitalize()
                    if ab.removePerson(addressbook, last_name, first_name):
                        print()
                        print('CONTACT: ' + first_name + ' ' + last_name + ' :HAS BEEN REMOVED')
                    else:
                        print()
                        print('SORRY, CONTACT: ' + first_name + ' ' + last_name + ' :NOT FOUND')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'E':
                if addressbook is not None:
                    last_name = input('Please enter last name of person: ').capitalize()
                    first_name = input('Please enter first name of person: ').capitalize()
                    print()
                    print('CONTACT INFORMATION')
                    if ab.printPerson(addressbook, last_name, first_name):
                        print()
                    else:
                        print()
                        print('SORRY, CONTACT: ' + first_name + ' ' + last_name + ' :NOT FOUND')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'F':
                if addressbook is not None:
                    print()
                    print('ALL CONTACT INFORMATION')
                    ab.printAll(addressbook)
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'G':
                if addressbook is not None:
                    name = input('Please enter name of file to write to: ')
                    if name.endswith('.xml'):
                        doc.write(name)
                        print()
                        print('FILE SAVE TO: ' + name + ' :SUCCESSFUL')
                    elif name.endswith('.csv'):
                        f = open(name, 'wt')
                        f.write('last_name,first_name,birthday,phone_number,street_address\n')
                        for person in addressbook:
                            last_name = person.get('last_name')
                            first_name = person.get('first_name')
                            birthday = person.findtext('birthday')
                            phone = person.findtext('phone_number')
                            street = person.findtext('street_address')
                            f.write(last_name + ',' + first_name + ',' + birthday + ',' + phone + ',' + street + '\n')

                        f.close()
                        print()
                        print('FILE SAVE TO: ' + name + ' :SUCCESSFUL')
                    else:
                        print()
                        print('PLEASE ENTER A VALID FILE WITH CORRECT EXTENSION')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'H':
                if addressbook is not None:
                    last_name = input('Please enter last name of person: ').capitalize()
                    first_name = input('Please enter first name of person: ').capitalize()
                    birthday = input('Please enter new birthday of person: ')
                    phone_number = input('Please enter new phone number of person: ')
                    street_address = input('Please enter new street address of person: ')
                    updated_person = ab.updatePerson(addressbook, last_name, first_name, birthday, phone_number, street_address)
                    if updated_person:
                        print()
                        print('CONTACT: ' + first_name + ' ' + last_name + ' :UPDATED')
                    else:
                        print()
                        print('SORRY PERSON: ' + first_name + ' ' + last_name + ' :DOES NOT EXIST')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'I':
                if addressbook is not None:
                    group_name = input('Please enter name of the new group: ')
                    group = ab.addGroup(addressbook, group_name)
                    if not group:
                        print()
                        print('GROUP: ' + group_name + ' :ALREADY EXISTS')
                    elif group:
                        print()
                        print('GROUP: ' + group_name + ' :ADDED')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'J':
                if addressbook is not None:
                    group_name = input('Please enter name of the new group: ')
                    group = ab.removeGroup(addressbook, group_name)
                    if group:
                        print()
                        print('GROUP: ' + group_name + ' :REMOVED')
                    else:
                        print()
                        print('GROUP: ' + group_name + ' :DOES NOT EXIST')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'K':
                if addressbook is not None:
                    title = input('Please enter the title of the group you wish to add to: ')
                    last_name = input('Please enter the last name of the new member: ')
                    first_name = input('Please enter the first name of the new member: ')
                    group = ab.findGroup(addressbook, title)
                    if group == 1:
                        new = ab.addMember(addressbook, title, last_name, first_name)
                        if new == 1:
                            print()
                            print('MEMBER: ' + last_name + ' ' + first_name + ' :ALREADY EXISTS IN GROUP: ' + title)
                        elif new == 2:
                            print()
                            print('MEMBER: ' + last_name + ' ' + first_name + ' :ADDED TO GROUP: ' + title)
                    else:
                        print()
                        print('GROUP: ' + title + ' :DOES NOT EXIST')
                else:
                    print()
                    print('PLEASE CHOOSE A FILE FIRST')
            elif selected == 'X':
                if addressbook is None:
                    print('PROGRAM TERMINATED')
                    return selected
                ans = input('Would you like to save your addressbook? (Y/N): ').upper()
                if ans == 'Y' or ans == 'YES':
                    name = input('Save your addressbook as: ')
                    if name.endswith('.xml'):
                        doc.write(name)
                        print()
                        print('YOUR ADDRESS BOOK HAS BEEN SAVED AS: ' + name)
                        return selected
                    if name.endswith('.csv'):
                        f = open(name, 'wt')
                        f.write('last_name,first_name,birthday,phone_number,street_address\n')
                        for person in addressbook:
                            last_name = person.get('last_name')
                            first_name = person.get('first_name')
                            birthday = person.findtext('birthday')
                            phone = person.findtext('phone_number')
                            street = person.findtext('street_address')
                            f.write(last_name + ',' + first_name + ',' + birthday + ',' + phone + ',' + street + '\n')

                        f.close()
                        print()
                        print('YOUR ADDRESS BOOK HAS BEEN SAVED AS: ' + name)
                        print('PROGRAM TERMINATED')
                        return selected
                    print()
                    print('PLEASE ENTER A VALID FILE NAME WITH CORRECT EXTENSION')
                else:
                    if ans == 'N' or ans == 'NO':
                        print()
                        print('ADDRESS BOOK NOT SAVED')
                        print('PROGRAM TERMINATED')
                        return selected
                    print()
                    print('PLEASE ENTER CORRECT RESPONSE')
            print()
            print(input(colored('Press RETURN to continue', 'light_green', attrs=['blink'])))
        else:
            print('PLEASE ENTER A VALID SELECTION')
            print(input(colored('Press RETURN to continue', 'light_green', attrs=['blink'])))

    return


if __name__ == "__main__":
    menu()
