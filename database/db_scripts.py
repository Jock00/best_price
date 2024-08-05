import sqlite3


class PhonesDB:
    def __init__(self, table, db_name="phones_db.db"):
        self.connection = sqlite3.connect(db_name)
        self.table = table
        # Step 3: Create a Cursor Object
        # This cursor will be used to execute SQL commands
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def create_table(self):
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {self.table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT,
            model TEXT,
            memory TEXT,
            ram TEXT,
            connectivity TEXT,
            color TEXT,
            url TEXT REQUIRED
        )
        '''

        # Execute the query to create the table
        self.cursor.execute(create_table_query)

        # Commit the changes to the database
        self.connection.commit()

    def insert_values(self, params):
        brand = params.get("BRAND", None)
        model = params.get("MODEL", None)
        memory = params.get("MEMORY", None)
        ram = params.get("RAM", None)
        connectivity = params.get("CONNECTIVITY", None)
        color = params.get("COLOR", None)
        url = params.get("url", None)

        if type(brand) == list:
            brand = ",".join(brand)

        if type(model) == list:
            model = ",".join(model)

        if type(memory) == list:
            memory = ",".join(memory)

        if type(ram) == list:
            ram = ",".join(ram)

        if type(connectivity) == list:
            connectivity = ",".join(connectivity)

        if type(color) == list:
            color = ",".join(color)

        insert_query = f'''
        INSERT INTO {self.table} (
        brand,
            model ,
            memory ,
            ram ,
            connectivity ,
            color,
             url) 
        VALUES (?, ?, ?,?,?,?,?)
        '''
        data_to_insert = (brand, model, memory, ram, connectivity, color, url)
        self.cursor.execute(insert_query, data_to_insert)

        # Step 4: Commit the transaction
        self.connection.commit()

        # Step 5: Close the connection

    def check_records(self, params):

        select_query = f'SELECT url FROM {self.table}'
        if not params:
            return []

        brand = params.get("brand", None)
        model = params.get("model", None)
        memory = params.get("memory", None)
        ram = params.get("ram", None)
        connectivity = params.get("connectivity", None)
        color = params.get("color", None)
        url = params.get("color", None)

        extra_query = []
        if brand:
            extra_query = [f"Lower(brand) like '%{brand.lower()}%'"]

        if model:
            extra_query.append(f"Lower(model) like '%{model.lower()}%'")

        if memory:
            extra_query.append(f"Lower(model) like '%{memory.lower()}%'")

        if ram:
            extra_query.append(f"Lower(ram) like '%{ram.lower()}%'")

        if connectivity:
            extra_query.append(f"Lower(connectivity) like '%{connectivity.lower()}%'")

        if color:
            extra_query.append(f"Lower(color) like '%{color.lower()}%'")

        if url:
            extra_query.append(f"Lower(connectivity) like '%{url.lower()}'")

        select_query += " WHERE " + " AND ".join(extra_query)

        self.cursor.execute(select_query)

        # Fetch all rows and convert them to a list of dictionaries
        results = [dict(row)['url'] for row in self.cursor.fetchall()]

        return results



    def close_connection(self):
        # Step 5: Close the Connection
        self.connection.close()
