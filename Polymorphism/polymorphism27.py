class MySQL:
    def connect(self):
        print("Connected to MySQL")
class Oracle:
    def connect(self):
        print("Connected to Oracle")
class PostgreSQL:
    def connect(self):
        print("Connected to PostgreSQL")
def connect_database(database):
    database.connect()
connect_database(MySQL())
connect_database(Oracle())
connect_database(PostgreSQL())