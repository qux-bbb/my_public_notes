# python---SQLObject例子

需要安装SQLObject模块  
```r
pip install sqlobject
```

```python
# !python2
# coding:utf8

from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlobject import *

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'s': 'sqlite', 'm': 'mysql'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16

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

def setup():
    return RDBMSs[(raw_input('''
Choose a database system:

(M)ySQL
(S)QLite

Enter choice: ''')).strip().lower()[0]]

DSNs = {
    'mysql': 'mysql://root:root@localhost/%s' % DBNAME,
    'sqlite': 'sqlite:///:memory:',
}


class Users(SQLObject):
    login = StringCol(length=NAMELEN)
    userid = IntCol()
    projid = IntCol()
    def __str__(self):
        return ''.join(map(tformat, (self.login, self.userid, self.projid)))


class SQLObjectTest(object):
    def __init__(self, dsn):
        try:
            cxn = connectionForURI(dsn)
        except ImportError:
            raise RuntimeError()
        try:
            cxn.releaseConnection(cxn.getConnection())
        except dberrors.OperationalError:
            cxn = connectionForURI(dirname(dsn))
            cxn.query('CREATE DATABASE %s' % DBNAME)
            cxn = connectionForURI(dsn)
        self.cxn = sqlhub.processConnection  =cxn

    def insert(self):
        for who, userid in randName():
            Users(login=who, userid=userid, projid=rand(1, 5))

    def update(self):
        fr = rand(1, 5)
        to = rand(1, 5)
        i = -1
        users = Users.selectBy(projid=fr)
        for i, user in enumerate(users):
            user.projid = to
            return fr, to, i+1

    def delete(self):
        rm = rand(1, 5)
        users = Users.selectBy(projid=rm)
        i = -1
        for i, user in enumerate(users):
            user.destroySelf()
            return rm, i+1

    def dbDump(self):
        printf('\n%s' % ''.join(map(cformat, FIELDS)))
        for user in Users.select():
            printf(user)

    def finish(self):
        self.cxn.close()


def main():
    printf('*** Connect to %r databasee' % DBNAME)
    db = setup()
    if db not in DSNs:
        printf('\nERROR: %r not supported, exit' % db)
        return

    try:
        orm = SQLObjectTest(DSNs[db])
    except RuntimeError:
        printf('\nERROR: %r not supported, exit' % db)
        return

    printf('\n*** Create users table (drop old one if appl.)')
    Users.dropTable(True)
    Users.createTable()

    printf('\n*** Insert names into table')
    orm.insert()
    orm.dbDump()

    printf('\n*** Move users to a random group')
    fr, to, num = orm.update()
    printf('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    orm.dbDump()

    printf('\n*** Randomly delete froup')
    rm, num = orm.delete()
    printf('\t(group #%d; %d users removed' % (rm, num))
    orm.dbDump()

    printf('\n*** Drop users table')
    Users.dropTable()
    printf('\n*** Close cxns')
    orm.finish()


if __name__ == '__main__':
    main()
```


2018/11/4  
