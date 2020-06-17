"""
This module contains some useful functions for making the map
"""
import os

import netCDF4 as nc


def get_temperature(filepath, var_name="AvgSurfT_tavg", fill_val=273.15):
    """
    This function extracts temperature data from the given file path

    # Arguements:
        filepath: A string that specifies the file to be read
        var_name: The name of the temperature variable to be extracted.
                  Default is "AvgSurfT_tavg"
        fill_val: The fill value for masked values. Default is 273.15
    # Returns:
        The data temperature in the file. Masked values are filled as 273.15
        by default
    """
    assert isinstance(filepath, str), "Pass in file path as a string!"
    assert os.path.isfile(filepath), "{} does not exist!".format(filepath)

    file = nc.Dataset(filepath)
    temperature = file.variables[var_name][0]
    file.close()

    # masked values are filled as 273.15K (0°C)
    return temperature.filled(fill_val)


def get_lat_lon_mask(filepath, var_name="AvgSurfT_tavg"):
    """
    This function extracts latitudes, longitudes and a land-ocean mask from
    the given file path

    # Arguments:
        filepath: A string that specifies the file to be read
        var_name: The name of the temperature variable to be extracted.
                  Default is "AvgSurfT_tavg"
    # Returns:
        Available latitudes, longitudes, and a land_ocean mask from the file
    """
    assert isinstance(filepath, str), "Pass in file path as a string!"
    assert os.path.isfile(filepath), "{} does not exist!".format(filepath)

    file = nc.Dataset(filepath)
    lat = file.variables['lat'][:].filled()
    lon = file.variables['lon'][:].filled()
    mask = file.variables[var_name][0].mask
    file.close()

    return lat, lon, mask


def get_zone(score):
    """
    A simple function to return the corresponding zone of the given score.
    Zone format: "<lower_limit> - <upper_limit>"
    lower_limit is inclusive and upper_limit is exclusive.

    # Arguments:
        score: a number in the range of [0, 100].
    # Returns:
        A string representation of the corresponding zone.
    """
    assert isinstance(score, (int, float)), "Score needs to be a number!"
    assert 0 <= score <= 100,\
        "Score {} is out of valid range [0, 100]".format(score)

    if score == 100:
        return "90 - 100"
    else:
        return "{:.0f} - {:.0f}".format(score//10*10, (score+10)//10*10)
