from mysql.connector import MySQLConnection, Error
from config import read_config

def iter_row(cursor, size=10):
    # Infinite loop to fetch rows in chunks of 'size' from the result set
    while True:
        rows = cursor.fetchmany(size)
        # Break the loop if there are no more rows to fetch
        if not rows:
            break

        # Yield each row in the fetched chunk
        for row in rows:
            yield row

def query_with_fetchmany(config):
    # Initialize variables for connection and cursor
    conn = None
    cursor = None

    try:
        # Establish a connection to the MySQL database using the provided configuration
        conn = MySQLConnection(**config)
        
        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Execute a SELECT query to retrieve all rows from the 'books' table
        cursor.execute("SELECT * FROM books")

        # Iterate over rows using the custom iterator function 'iter_row'
        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        # Print an error message if an error occurs during the execution of the query
        print(e)

    finally:
        # Close the cursor and connection in the 'finally' block to ensure it happens
        if cursor:
            cursor.close()
        
        if conn:
            conn.close()

if __name__ =='__main__' :
    # Read the database configuration from the 'config' module
    config = read_config()
    
    # Call the function with the obtained configuration to execute the query
    query_with_fetchmany(config)
