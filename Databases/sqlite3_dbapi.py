import sqlite3

def main():
    
    # connecting to sqlite3 
    ''' 
    connection returns a db handle that can be used to interface with db
    and this can be managed via the db.cursor() 
    '''
    print('Connecting...')
    print("**************************************************************\n")
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    
    ''' Create table '''
    print('Creating tables:\n')
    # first check if table exists
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    
    # Insert rows
    print('Inserting 3 rows')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('Mercedes', 25000)
        """)
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('BMW', 20000)
        """)
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('Audi', 18000)
        """)
    
    # Commit
    print('Inserts were committed')
    db.commit()

    # Query - count rows
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'There are {count} rows in the table')

    # Query - print rows
    print("\nPrinting the table's rows:")
    for row in cur.execute("SELECT * FROM test"):
        print(row)

    # drop table  
    print("**************************************************************\n")  
    print("Dropping the 'test' table")
    cur.execute("DROP TABLE test")

    # Closing db
    db.close()
    print('db closed')

if __name__ == '__main__': main()