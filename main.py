import requests
import pyspark
import pandas as pd
import csv
import json
import geopandas
import datetime
import geocoder
import math


def calculate_distance(user_location, previous_fire_location):
    # convert the latitude and longitude to radians for both locations
    # calculate delta phi
    # calculate delta lambda
    # calculate delta sigma

    earth_radius = 6378  # earths radius in kilometers

    # return the calculated distance


def load_historic_fire_data(MAP_KEY):
    print("load_historic_fire_data() - Loading historic fire data...")
    pls_work = 'https://firms.modaps.eosdis.nasa.gov//api/country/csv/[MAP_KEY]/[SOURCE]/[COUNTRY_CODE]/[DAY_RANGE]'
    nasa_usa_data = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/VIIRS_SNPP_NRT/USA/10'
    
    try:
        df = pd.read_csv(nasa_usa_data, sep=';')
        json_df = pd.DataFrame(df.to_dict(orient="records"))
        print(json_df + "\n")
        first_row = json_df.iloc[2]
        print(first_row)  # How to print the first row of the dataframe
        
    except:
        print("load_historic_fire_data() - There was an issue with a query to the NASA Firms API")
        exit()

    print("load_historic_fire_data() - Successfully loaded historic fire data")

    
def load_weather_and_enviornmental_data(fire_location, date):
    # NOAA Weather API
    pass


def gather_vegegation_and_moisture_levels(fire_location, date):
    pass


def gather_elevation_and_terrain_data(fire_location, date):
    pass


def get_user_location():
    g = geocoder.ip('me')  # 'me' automatically detects the user's IP
    if g.ok:
        return g.latlng  # Returns a tuple of (latitude, longitude)
    else:
        return None\
        

def main():
    NASA_FIRMS_MAP_KEY = 'f80b6fc478f8a899e4947ac6b36cb418'  # Expires after 10 minutes https://firms.modaps.eosdis.nasa.gov/api/map_key
    GOOGLE_MAPS_API_KEY = None

    location = get_user_location()
    desired_radius = int(input("What is your desired radius?"))

    if location:
        print(f"Latitude: {location[0]}, Longitude: {location[1]}")
    else:
        print("Could not retrieve user location")

    # From the users location, search in a specified radius. Gathering information from previously recorded fires in that radius, return a prediction
    # stuff = requests.get('https://data-nifc.opendata.arcgis.com/datasets/4181a117dc9e43db8598533e29972015_0/explore?showTable=true/WFIGS_Incident_Locations_Current_1704360007229377145.csv')
    # print(stuff)
    big_ahh_dataframe = load_historic_fire_data(NASA_FIRMS_MAP_KEY)

    for df in big_ahh_dataframe:
        if (calculate_distance(location, df) <= desired_radius): # and find out how to access the latitude and longitude of that fire
            print("Adding something to our predictions list")
            # Run through the rest of the steps???
        else:
            print("Not adding something to our predictions list")
        

if __name__ == '__main__':
    # https://data-nifc.opendata.arcgis.com/

    # https://data-nifc.opendata.arcgis.com/datasets/4181a117dc9e43db8598533e29972015_0/explore?showTable=true/WFIGS_Incident_Locations_Current_1704360007229377145.csv

    main()