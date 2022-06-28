# Credit for the original code provided by Bill Weinman 
# @ https://www.linkedin.com/learning/python-essential-training-2018
# Below I have slightly altered it


import sqlite3

__version__ = '1.2.0'

# The constructor
class bwDB:
    def __init__(self, **kwargs):
        """
            db = bwDB( [ table = ''] [, filename = ''] )
            constructor method
                table is for CRUD methods 
                filename is for connecting to the database file
        """
        # see filename @property decorators below
        self._filename = kwargs.get('filename')
        self._table = kwargs.get('table', '')

    # set_table for CRUD methods
    def set_table(self, tablename):
        self._table = tablename

    # SQL methods
    def sql_do(self, sql, params=()):
        """
            db.sql_do( sql[, params] )
            method for non-select queries (i.e. queries that do not return any values)
                sql is string containing SQL
                params is list containing parameters
            returns nothing
        """
        self._db.execute(sql, params)
        self._db.commit()

    def sql_do_nocommit(self, sql, params=()):
        """
            sql_do_nocommit( sql[, params] )
            method for non-select queries *without commit*
                sql is string containing SQL
                params is list containing parameters
            returns nothing
        """
        self._db.execute(sql, params)

    def sql_query(self, sql, params=()):
        """
            db.sql_query( sql[, params] )
            generator method for queries
                sql is string containing SQL
                params is list containing parameters
            returns a generator with one row per iteration
            each row is a Row factory
        """
        c = self._db.execute(sql, params)
        for r in c:
            yield r

    def sql_query_row(self, sql, params=()):
        """
            db.sql_query_row( sql[, params] )
            query for a single row
                sql is string containing SQL
                params is list containing parameters
            returns a single row as a Row factory
        """
        c = self._db.execute(sql, params)
        return c.fetchone()

    def sql_query_value(self, sql, params=()):
        """
            db.sql_query_row( sql[, params] )
            query for a single value
                sql is string containing SQL
                params is list containing parameters
            returns a single value
        """
        c = self._db.execute(sql, params)
        return c.fetchone()[0]

    def commit(self):
        self._db.commit()


    '''CRUD section'''
    def getrec(self, recid):
        """
            db.getrec(recid)
            get a single row, by id
        """
        query = f'SELECT * FROM {self._table} WHERE id = ?'
        c = self._db.execute(query, (recid,))
        return c.fetchone()

    def getrecs(self):
        """
            db.getrecs()
            get all rows, returns a generator of Row factories
        """
        query = f'SELECT * FROM {self._table}'
        c = self._db.execute(query)
        for r in c:
            yield r

    def insert_nocommit(self, rec):
        """
            db.insert(rec)
            insert a single record into the table
                rec is a dict with key/value pairs corresponding to table schema
            omit id column to let SQLite generate it
        """
        klist = sorted(rec.keys())
        values = [rec[v] for v in klist]  # a list of values ordered by key
        q = 'INSERT INTO {} ({}) VALUES ({})'.format(
            self._table,
            ', '.join(klist),
            ', '.join('?' * len(values))
        )
        c = self._db.execute(q, values)
        return c.lastrowid

    def insert(self, rec):
        lastrowid = self.insert_nocommit(rec)
        self._db.commit()
        return lastrowid

    def update_nocommit(self, recid, rec):
        """
            db.update(id, rec)
            update a row in the table
                id is the value of the id column for the row to be updated
                rec is a dict with key/value pairs corresponding to table schema
        """
        klist = sorted(rec.keys())
        values = [rec[v] for v in klist]  # a list of values ordered by key

        for i, k in enumerate(klist):  # don't udpate id
            if k == 'id':
                del klist[i]
                del values[i]

        q = 'UPDATE {} SET {} WHERE id = ?'.format(
            self._table,
            ',  '.join(map(lambda s: '{} = ?'.format(s), klist))
        )
        self._db.execute(q, values + [recid])

    def update(self, recid, rec):
        self.update_nocommit(recid, rec)
        self._db.commit()

    def delete_nocommit(self, recid):
        """
            db.delete(recid)
            delete a row from the table, by recid
        """
        query = f'DELETE FROM {self._table} WHERE id = ?'
        self._db.execute(query, [recid])

    def delete(self, recid):
        self.delete_nocommit(recid)
        self._db.commit()

    def countrecs(self):
        """
            db.countrecs()
            count the records in the table
            returns a single integer value
        """
        query = f'SELECT COUNT(*) FROM {self._table}'
        c = self._db.execute(query)
        return c.fetchone()[0]

    '''
    Decorators:

    - @property: 
    * filename property --> the getter 
    * it reads the filename and returns it

    - @_filename.setter: 
    * it assigns a value to the filename
    * this assignment creates a fresh connection to db 
    * and it allows the row factory set up

    @_filename.deleter: 
    * it closes the db
    '''
    @property
    def _filename(self):
        return self._dbfilename

    @_filename.setter
    def _filename(self, fn):
        self._dbfilename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @_filename.deleter
    def _filename(self):
        self.close()

    def close(self):
        self._db.close()
        del self._dbfilename

# Testing
def test():
    fn = ':memory:'  # in-memory database | the filename
    t = 'foo'

    recs = [
        dict(string='Mercedes', number=25000),
        dict(string='BMW', number=20000),
        dict(string='Audi', number=15000)
    ]

    # -- for file-based database
    # try: os.stat(fn)
    # except: pass
    # else: 
    #     print('Delete', fn)
    #     os.unlink(fn)

    print('The bwDB version is: {}'.format(__version__))

    print(f'Create database file {fn} ...', end='')
    db = bwDB(filename=fn, table=t)
    print('Done.')

    print('Create table ... ', end='')
    db.sql_do(f' DROP TABLE IF EXISTS {t} ')
    db.sql_do(f' CREATE TABLE {t} ( id INTEGER PRIMARY KEY, string TEXT, number INTEGER ) ')
    print('Done.')

    print('Insert into table ... ', end='')
    for r in recs:
        db.insert(r)
    print('Done.')

    print(f'There are {db.countrecs()} rows')

    print('Read from table')
    for r in db.getrecs():
        print(dict(r))

    print('Update table')
    db.update(2, dict(string='Ford'))
    print(dict(db.getrec(2)))

    print('Insert an extra row ... ', end='')
    newid = db.insert({'string': 'Renault', 'number': 10000})
    print(f'(id is {newid})')
    print(dict(db.getrec(newid)))
    print(f'There are {db.countrecs()} rows')
    print('Now delete it')
    db.delete(newid)
    print(f'There are {db.countrecs()} rows')
    for r in db.getrecs():
        print(dict(r))
    for r in db.sql_query(f"select * from {t}"):
        print(r)
    db.close()


if __name__ == "__main__": test()