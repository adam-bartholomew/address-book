# Embedded file name: test_part1.py
import addressbook as ab


def test_part1():
    doc = ab.create_address_book()
    addressbook = doc.getroot()
    print(ab.add_person(addressbook, 'Aardvark', 'Anthony', 'January 14, 1765', '860-341-9000', '827 Abbey Road'))
    print(ab.add_person(addressbook, 'Buffalo', 'Boris', 'July 4, 1234', '098-612-7777', '3478 Made Up Way'))
    print(ab.add_person(addressbook, 'Cat', 'Charlene', 'December 23, 2044', '132-465-8790', '10 Road Street'))
    print(ab.add_person(addressbook, 'Dog', 'Donna', 'October 31, 1134', '246-824-6824', '900 Spooner Street'))
    print(ab.add_person(addressbook, 'Elephant', 'Emily', 'November 29, 1994', '756-102-9458', '67 Normandy Avenue'))
    print(ab.add_person(addressbook, 'Fox', 'Frederick', 'April 29, 1867', '143-729-0000', '132 Lampard Way'))
    print(ab.remove_person(addressbook, 'Cat', 'Charlene'))
    print(ab.print_person(addressbook, 'Dog', 'Donna'))
    print(ab.remove_person(addressbook, 'Gopher', 'Gus'))
    print(ab.print_person(addressbook, 'Cat', 'Charlene'))
    ab.print_all(addressbook)


test_part1()
