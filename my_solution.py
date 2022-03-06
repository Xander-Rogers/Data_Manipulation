#!/usr/bin/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers & Tristan Bryant
# Contact: arogers23@email.davenport.edu & tbryant17@email.davenport.edu
# Program name: data_sort.py

"""
This program is an example of how data sorting techniques in python can be used to take a txt file with data
and filter, sort and then sum the information contained in the file.
"""

# The json module is used to save the final files in a son format.
# The os module is used to make a sub directory to store the json files in.
import json
import os


# Moved the import statements up here for a more pythonic format

##########
# The following area should only contain Functions and Classes
##########

# Examples only. your program may not contain any Functions or Classes.
def read_data():
    """
        read_data function reads the text file into wsd, which is a list of dictionaries that has
        key values of: station, month, snow

        Returns:
            wsd as a list
    """
    wsd = []

    # This line will read the header information of the file and do nothing with it.
    with open('data.txt', 'r', encoding='utf-8-sig') as data:
        data.readline()
        for line in data:

            # This line strips the lines in the file and splits them up by the tab delimiter.
            x = line.strip().split('\t')

            # Some of the lines do not contain data, this if statement will ignore any line, that does not have three
            # entries which eliminates any empty values in the file.
            if len(x) != 3:
                pass
            else:
                raw_data = {}
                raw_data['station'] = x[0]
                raw_data['month'] = x[1]
                raw_data['snow'] = x[2]
                wsd.append(raw_data)

    # Return statement to pass along an argument for the next function to use
    return wsd


def get_station_list():
    """
        get_station function gets input from the read_data function, set as wsd, appends it to a list called station,
        and then appends single station names to remove duplicates.

        Returns:
            station_list as a list.
    """
    wsd = read_data()
    station = []

    for entry in wsd:
        station.append(entry['station'])
    station_list = []
    [station_list.append(x) for x in station if x not in station_list]

    return station_list
    # The return statement passes along an argument for the next function to use


def subdir():
    """
        subdir function will create a directory for the .json files to be saved into using os.mkdir(). If the directory
        already exists then the program will terminate so as to avoid overwriting files.
    """
    try:
        directory = 'station_data/'
        os.mkdir(directory)
    except FileExistsError:
        print("This directory already exists")


def getsnowfall():
    """
        This function will sort through the list of stations, then for each month in the list of months it will sum the
        snowfall as listed in wsd. Then that information is passed to list for the station then once all 12 months of
        snow have been calculated, this information is written to a json file named as the station id.

        After all months have been iterated for the station ID, all the monthly snowfall totals are
        placed in a json object with an indent that will ensure they are listed vertically instead of
        horizontally.

    """
    wsd = read_data()
    station_list = get_station_list()

    # Using the above functions which have declared return values of the lists wanted from each function
    months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December',
              ]

    # Iterates through each station ID that was previously calculated.
    for st in station_list:
        combined = []

        # Iterates through each month in the list of months for each station ID.
        for month in months:
            snow_total = 0.0
            for ws in wsd:
                if st == ws['station']:

                    # Checks if the month iteration matches the wsd entry.
                    if month == ws['month']:
                        # sets the snow value in the wsd entry to sn.
                        sn = ws['snow']

                        # Adds to snow_total the value of sn as a float.
                        snow_total += float(sn)

                        # Rounds snow_total to 2 decimal places.
                        snow_total = round(snow_total, 2)

            # Appends the station ID, month and total snow to a list
            combined.append([st, month, snow_total])

        json_object = json.dumps(combined, indent=4)

        # Takes the station ID and assigns it as a variable.
        name = st

        # Takes the station ID and adds the .json extension.
        filename = name + ".json"
        full_filename = 'station_data/' + filename  # Takes the filepath and adds the filname into one variable.
        with open(full_filename, 'w') as outfile:  # Creates and writes the file with the information needed.
            outfile.write(json_object)


# All supporting functions and classes
# exist above this line
# ====================================
# Program Starts Here

def main():
    """
    the main function will take the data.txt file and sort it by station and sum all values for that station in each
    month, and write them to a .json file in the directory.
    """

    # Function that reads file.
    read_data()

    # Function that creates the directory to save the json files into.
    subdir()

    # Sums all values and writes to the json files.
    getsnowfall()


# ===============================
# No extra Code beyond this point
# This code is required for the main() function to work
if __name__ == "__main__":
    main()
# EOF #
