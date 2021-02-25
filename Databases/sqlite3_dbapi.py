import sqlite3

def main():
    
    # connect to sqlite3 db api
    print('connect')
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    print('create')

    ''' Create table '''
    # first check if table exists
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    
    # Insert rows
    print('Inserting a row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('Mercedes', 25000)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('BMW', 20000)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('Audi', 18000)
        """)
    
    # Commit
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()