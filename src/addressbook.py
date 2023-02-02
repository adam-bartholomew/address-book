# Embedded file name: addressbook.py
import xml.etree.ElementTree as elementTree

def createAddressBook():
    addressbook = elementTree.Element('addressbook')
    doc = elementTree.ElementTree(addressbook)
    return doc


def addPerson(addressbook, last_name, first_name, birthday, phone_number, street_address):
    newPerson = findElement(addressbook, last_name, first_name)
    if newPerson == 1:
        return False
    else:
        newPerson = elementTree.SubElement(addressbook, 'person')
        newPerson.set('last_name', last_name)
        newPerson.set('first_name', first_name)
        newBirthday = elementTree.SubElement(newPerson, 'birthday')
        newBirthday.text = birthday
        newPhone = elementTree.SubElement(newPerson, 'phone_number')
        newPhone.text = phone_number
        newStreet = elementTree.SubElement(newPerson, 'street_address')
        newStreet.text = street_address
        return True


def removePerson(addressbook, last_name, first_name):
    for person in addressbook:
        last = person.get('last_name')
        first = person.get('first_name')
        if person is not None and last == last_name and first == first_name:
            addressbook.remove(person)
            return True

    return False


def printPerson(addressbook, last_name, first_name):
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


def printAll(addressbook):
    person_list = []
    people = addressbook.findall('person')
    for person in people:
        name = (person.get('last_name'), person.get('first_name'))
        person_list.append(name)

    person_list.sort()
    for name in person_list:
        printPerson(addressbook, name[0], name[1])


def findElement(addressbook, last_name, first_name):
    for element in addressbook:
        last = element.get('last_name')
        first = element.get('first_name')
        if last == last_name and first == first_name:
            return 1

    return None


def updatePerson(addressbook, last_name, first_name, birthday, phone_number, street_address):
    people = addressbook.findall('person')
    person = 0
    for element in people:
        last = element.get('last_name')
        first = element.get('first_name')
        person = 0
        if last == last_name and first == first_name:
            person = element
            bText = person.findtext('birthday')
            bText = birthday
            bChild = person.find('birthday')
            bChild.text = bText
            pText = person.findtext('phone_number')
            pText = phone_number
            pChild = person.find('phone_number')
            pChild.text = pText
            sText = person.findtext('street_address')
            sText = street_address
            sChild = person.find('street_address')
            sChild.text = sText
            return True
        person += 1

    if person >= 1:
        return False


def findGroup(addressbook, title):
    groups = addressbook.findall('group')
    for element in groups:
        group_title = element.get('title')
        if group_title == title:
            return 1

    return None


def addGroup(addressbook, title):
    new_group = findGroup(addressbook, title)
    if new_group == 1:
        return False
    else:
        new_group = elementTree.SubElement(addressbook, 'group')
        new_group.set('title', title)
        return True


def removeGroup(addressbook, title):
    groups = addressbook.findall('group')
    for group in groups:
        group_title = group.get('title')
        if group_title == title:
            addressbook.remove(group)
            return True
    return False


def findMember(addressbook, last_name, first_name):
    groups = addressbook.findall('group')
    for e1 in groups:
        group = e1
        members = group.findall('member')
        for e2 in members:
            member = e2
            last = member.get('last_name')
            first = member.get('first_name')
            if last == last_name and first == first_name:
                return 1
            return 0


def addMember(addressbook, title, last_name, first_name):
    groups = addressbook.findall('group')
    if findMember(addressbook, last_name, first_name) is not None:
        for e1 in groups:
            if e1.get('title') == title:
                group = e1
                members = group.findall('member')
                for e2 in members:
                    last = e2.get('last_name')
                    first = e2.get('first_name')
                    if last == last_name and first == first_name:
                        return 1
                    new_member = elementTree.SubElement(group, 'member')
                    new_member.set('last_name', last_name)
                    new_member.set('first_name', first_name)
                    return 2

            else:
                return 3
