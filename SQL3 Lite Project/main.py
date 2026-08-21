import sqlite3

# Importing our custom modules
import database_setup
import queries

def main():
    print("Starting University Database Program...\n")
    
    #  Open a  connection to the database
    # This creates 'university.db' in our folder, if it doesn't exist yet
    conn = sqlite3.connect('university.db')
    
    try:
        # Setting up, Creates tables and insert data
        database_setup.create_tables(conn)
        database_setup.insert_sample_data(conn)
        
        # Querying the info
        queries.students_per_course(conn)
        queries.students_multiple_courses(conn)
        
    except sqlite3.Error as error:
        # If anything goes wrong with the database, printing this error message
        print(f"A database error occurred: {error}")
        
    finally:
        # Cleaning up, it always close the db connection when finished
        conn.close()
        print("\nDatabase connection closed. Program complete.")

# main() only runs when we execute this script
if __name__ == "__main__":
    main()