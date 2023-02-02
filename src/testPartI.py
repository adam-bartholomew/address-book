# Embedded file name: testPartI.py
import addressbook as ab

def testPartI():
    doc = ab.createAddressBook()
    addressbook = doc.getroot()
    print(ab.addPerson(addressbook, 'Aardvark', 'Anthony', 'January 14, 1765', '860-341-9000', '827 Abbey Road'))
    print(ab.addPerson(addressbook, 'Buffalo', 'Boris', 'July 4, 1234', '098-612-7777', '3478 Made Up Way'))
    print(ab.addPerson(addressbook, 'Cat', 'Charlene', 'December 23, 2044', '132-465-8790', '10 Road Street'))
    print(ab.addPerson(addressbook, 'Dog', 'Donna', 'October 31, 1134', '246-824-6824', '900 Spooner Street'))
    print(ab.addPerson(addressbook, 'Elephant', 'Emily', 'November 29, 1994', '756-102-9458', '67 Normandy Avenue'))
    print(ab.addPerson(addressbook, 'Fox', 'Frederick', 'April 29, 1867', '143-729-0000', '132 Lampard Way'))
    print(ab.removePerson(addressbook, 'Cat', 'Charlene'))
    print(ab.printPerson(addressbook, 'Dog', 'Donna'))
    print(ab.removePerson(addressbook, 'Gopher', 'Gus'))
    print(ab.printPerson(addressbook, 'Cat', 'Charlene'))
    ab.printAll(addressbook)


testPartI()
