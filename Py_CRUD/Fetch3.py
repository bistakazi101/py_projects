from mysql.connector import MySQLConnection, Error
from config import read_config

def query_with_fetchone(config):
    # Initialize variables for cursor and connection
    cursor = None
    conn = None

    try:
        # Establish a connection to the MySQL database using the provided configuration
        conn = MySQLConnection(**config)
        
        # Create a cursor to interact with the database
        cursor = conn.cursor()
        
        # Execute a SELECT query to retrieve all rows from the 'books' table
        cursor.execute("SELECT * FROM books")

        # Fetch the first row
        row = cursor.fetchone()
       

        # Loop through all rows and print them
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        # Print an error message if an error occurs during the execution of the query
        print(e)

    finally:
        # Close the cursor and connection in the 'finally' block to ensure it happens
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    # Read the database configuration from the 'config' module
    config = read_config()
    
    # Call the function with the obtained configuration to execute the query
    query_with_fetchone(config)
