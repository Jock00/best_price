import sqlite3

# Step 2: Create a Database Connection
# The file `my_database.db` will be created in the current directory if it doesn't exist
connection = sqlite3.connect('phones_db.db')

# Step 3: Create a Cursor Object
# This cursor will be used to execute SQL commands
cursor = connection.cursor()

# Step 4: Create a Table (Optional)
# Define a SQL query to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS phones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    model TEXT,
    memory TEXT,
    ram TEXT,
    connectivity TEXT,
    color TEXT
)
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
connection.commit()

# Step 5: Close the Connection
connection.close()

print("Database created and connection closed successfully.")
