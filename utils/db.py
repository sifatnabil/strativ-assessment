import sqlite3

def create_db() -> None:
    """
    Create the weather database.
    """
    # Connect to the database
    con = sqlite3.connect("data/weather.db")

    # Create a cursor
    cur = con.cursor()

    # Create the weather table
    cur.execute("CREATE TABLE weather (name, temperature)")

    # Commit the changes
    con.commit()

    # Close the connection
    con.close()

if __name__ == "__main__":
    create_db()
