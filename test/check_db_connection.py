from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="localhost", dbname='addressbook2', username="super", password="1111")


try:
    l = db.get_contacts_in_group(Group(id="63"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()