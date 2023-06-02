# python---mongodb

pymongo变了挺多的，所以这是核心编程的改编版本，还是老老实实用python2吧，python3有需求再说  

```python

# !python2
# coding:utf8

from distutils.log import warn as printf
from random import randrange as rand
from pymongo import MongoClient, errors

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
DBNAME = 'test'


NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina', 7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

COLLECTION = 'users'

class MongoTest(object):
    def __init__(self):
        try:
            cxn = MongoClient()
        except errors.AutoReconnect:
            raise RuntimeError()
        self.client = cxn
        self.db = cxn[DBNAME]
        self.users = self.db[COLLECTION]

    def insert(self):
        self.users.insert(
            dict(login=who, userid=uid, projid=rand(1, 5)) for who, uid in randName()
        )

    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        i = -1
        for i, user in enumerate(self.users.find({'projid': fr})):
            self.users.update(user, {'$set': {'projid': to}})
        return fr, to, i+1

    def delete(self):
        rm = rand(1, 5)
        i = -1
        for i, user in enumerate(self.users.find({'projid': rm})):
            self.users.remove(user)
        return rm, i+1

    def dbDump(self):
        printf('\n%s' % ''.join(map(cformat, FIELDS)))
        for user in self.users.find():
            printf(''.join(map(tformat, (user[k] for k in FIELDS))))

    def finish(self):
        self.client.close()


def main():
    printf('*** Connect to %r database' % DBNAME)
    try:
        mongo = MongoTest()
    except RuntimeError:
        printf('\nERROR: MongoDB server unreachable, exit')
        return

    printf('\n*** Insert names into table')
    mongo.insert()
    mongo.dbDump()

    printf('\n*** Move users to a random group')
    fr, to, num = mongo.update()
    printf('\t(%d) users moved from (%d) to (%d)' %(num, fr, to))
    mongo.dbDump()

    printf('\n*** Randomly delete group')
    rm, num = mongo.delete()
    printf('\t(group #%d; %d users removed)' % (rm, num))
    mongo.dbDump()

    printf('\n*** Drop users table')
    mongo.db.drop_collection(COLLECTION)
    printf('\n*** Close cxns')
    mongo.finish()

if __name__ == '__main__':
    main()

```


2018/11/5  
