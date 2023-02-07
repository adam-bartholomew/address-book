# Embedded file name: addressbook.py
import xml.etree.ElementTree as elementTree


def create_address_book():
    addressbook = elementTree.Element('addressbook')
    doc = elementTree.ElementTree(addressbook)
    return doc


def add_person(addressbook, last_name, first_name, birthday, phone_number, street_address):
    new_person = find_element(addressbook, last_name, first_name)
    if new_person == 1:
        return False
    else:
        new_person = elementTree.SubElement(addressbook, 'person')
        new_person.set('last_name', last_name)
        new_person.set('first_name', first_name)
        new_birthday = elementTree.SubElement(new_person, 'birthday')
        new_birthday.text = birthday
        new_phone = elementTree.SubElement(new_person, 'phone_number')
        new_phone.text = phone_number
        new_street = elementTree.SubElement(new_person, 'street_address')
        new_street.text = street_address
        return True


def remove_person(addressbook, last_name, first_name):
    for person in addressbook:
        last = person.get('last_name')
        first = person.get('first_name')
        if person is not None and last == last_name and first == first_name:
            addressbook.remove(person)
            return True

    return False


def print_person(addressbook, last_name, first_name):
    people = addressbook.findall('person')
    for element in people:
        last = element.get('last_name')
        first = element.get('first_name')
        if last == last_name and first == first_name:
            person = element
            if person is not None:
                print()
                print(first_name, last_name)
                birthday = person.findtext('birthday')
                print('Birthday: ' + birthday)
                phone = person.findtext('phone_number')
                print('Phone Number: ' + phone)
                street = person.findtext('street_address')
                print('Street Address: ' + street)
                return True
    return False


def print_all(addressbook):
    person_list = []
    people = addressbook.findall('person')
    for person in people:
        name = (person.get('last_name'), person.get('first_name'))
        person_list.append(name)

    person_list.sort()
    for name in person_list:
        print_person(addressbook, name[0], name[1])


def find_element(addressbook, last_name, first_name):
    for element in addressbook:
        last = element.get('last_name')
        first = element.get('first_name')
        if last == last_name and first == first_name:
            return 1

    return None


def update_person(addressbook, last_name, first_name, birthday, phone_number, street_address):
    people = addressbook.findall('person')
    for person in people:
        last = person.get('last_name')
        first = person.get('first_name')
        if last == last_name and first == first_name:
            person.find('birthday').text = birthday
            person.find('phone_number').text = phone_number
            person.find('street_address').text = street_address
            return True
    return False


def find_person(addressbook, last_name, first_name):
    for person in addressbook.findall('person'):
        if last_name == person.get('last_name') and first_name == person.get('first_name'):
            return True
    return False


def find_group(addressbook, title):
    groups = addressbook.findall('group')
    for element in groups:
        group_title = element.get('title')
        if group_title == title:
            return 1
    return None


def add_group(addressbook, title):
    new_group = find_group(addressbook, title)
    if new_group == 1:
        return False
    else:
        new_group = elementTree.SubElement(addressbook, 'group')
        new_group.set('title', title)
        return True


def remove_group(addressbook, title):
    groups = addressbook.findall('group')
    for group in groups:
        group_title = group.get('title')
        if group_title == title:
            addressbook.remove(group)
            return True
    return False


def find_member(addressbook, title, last_name, first_name):
    groups = addressbook.findall('group')
    for group in groups:
        if group.get('title') == title:
            for member in group.findall('member'):
                last = member.get('last_name')
                first = member.get('first_name')
                if last == last_name and first == first_name:
                    return 1


def add_member(addressbook, title, last_name, first_name):
    if not find_person(addressbook, last_name, first_name):
        return 5

    groups = addressbook.findall('group')
    if find_member(addressbook, title, last_name, first_name) is None:
        for group in groups:
            if group.get('title') == title:
                for member in group.findall('member'):
                    last = member.get('last_name')
                    first = member.get('first_name')
                    if last == last_name and first == first_name:
                        return 1
                new_member = elementTree.SubElement(group, 'member')
                new_member.set('last_name', last_name)
                new_member.set('first_name', first_name)
                return 2
        return 3
    return 4


def remove_member(addressbook, title, last_name, first_name):
    groups = addressbook.findall('group')
    if find_member(addressbook, title, last_name, first_name) is not None:
        for group in groups:
            if group.get('title') == title:
                for member in group.findall('member'):
                    if last_name == member.get('last_name') and first_name == member.get('first_name'):
                        group.remove(member)
                        return 1
                return 2
        return 3
    return 4


def print_group_members(addressbook):
    groups = addressbook.findall('group')
    for group in groups:
        print(f"\nMEMBERS OF GROUP \"{group.get('title')}\":")
        for member in group.findall('member'):
            print(f"{member.get('last_name')}, {member.get('first_name')}")
