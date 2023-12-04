# Heemonshu's code
import argparse
from database import WeatherDatabase
from service import WeatherService


# Global constants
DB_FILE = "data/weather_database.db"
API_KEY = "AhheRKHvgwik_KATjphklR0VDuKjiXIWdXcebixEDojj8q2lRbKiq0evSCSqKo5K"



def main():
    """
    Main function to run the program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="City to get the weather data for")
    parser.add_argument("--reset", action="store_true", help="Reset the database")
    args = parser.parse_args()

    # Create a database object
    db = WeatherDatabase(DB_FILE)
    service = WeatherService(API_KEY)

    # Reset the database if --reset is provided
    if args.reset:
        db.reset_database()
    
    # Retrieve and print weather data for the provided city
    city_weather_data = db.get_weather_data(service, args.city)
    print(f"Dew point for {args.city}: ", city_weather_data,'\u00b0C', sep='') 
    
if __name__ == "__main__":
    main()