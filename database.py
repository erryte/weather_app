import sqlite3
from datetime import datetime, timedelta

class WeatherDatabase:
    """
    Database class to interact with the weather database.
    """

    def __init__(self, db_file):
        """
        Initialize the database connection.
        """
        # Connect to SQLite database (creates a new one if not exists)
        self.conn = sqlite3.connect(db_file)

        # Create a cursor object to interact with the database
        self.cursor = self.conn.cursor()

        # Create a table to store weather data
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                dew_point REAL,
                timestamp TEXT
            );
        ''')

    def reset_database(self):
        """
        Reset the database by deleting all data
        """
        # Delete all data from the table
        self.cursor.execute('''
            DELETE FROM weather                    
        ''')
        self.conn.commit()
        print("Database deleted!")
    
    def insert_data(self, city, dew_point):
        """
        Insert weather data into the database
        """
        # Get current timestamp
        timestamp = datetime.now()

        # Insert data into the database
        self.cursor.execute('''
            SELECT * FROM weather
            WHERE city = ?
            ORDER BY timestamp DESC
            LIMIT 1
        ''', (city,))
        data = self.cursor.fetchone()

        # Check if data exists and if it is older than 24 hours before inserting
        if data and datetime.strptime(data[4], "%Y-%m-%d %H:%M:%S") > timestamp - timedelta(hours=24):
            return data
        else:
            self.cursor.execute('''
                INSERT INTO weather (city, dew_point, timestamp)
                VALUES (?,?,?)
            '''), (city, dew_point, timestamp.strftime("%Y-%m-%d"))


    def get_weather_data(self, weather_service, city):
        """
        Retrieve weather data for city.
        """
        self.cursor.execute('''
            SELECT * FROM weather
            WHERE city = ?
        ''', (city,))
        """
        data = self.cursor.fetchall()
        """
        data = self.cursor.fetchone()
        

        if data:
            return data[2]
        else:
            weather_data = weather_service.get_weather_data(city)

            self.cursor.execute('''
                INSERT INTO weather (city, dew_point)
                VALUES (?, ?)
            ''', (city, str(weather_data)))
            self.conn.commit()

            return weather_data

    def __del__(self):
        """
        Close the databse connection when the object is deleted.
        """
        self.conn.close()