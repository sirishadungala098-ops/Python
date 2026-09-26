import sqlite3
try:
    connection = sqlite3.connect("student.db")
    print("Database connected")
except sqlite3.Error:
    print("Database connection failed")
finally:
    if 'connection' in locals():
        connection.close()
        print("Database connection closed")