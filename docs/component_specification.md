# This is the component specification for all functions in `utils`

### 1. get_temperature
* What it does: get the temperature values in the given netCDF file
* Inputs(data type): file path(string), variable name(string), filling value(int or float)
* Outputs(data type): the temperature data in the file(numpy array)
* How it interacts with other components: get the temperature data that will be used by `get_zone`

### 2. get_lat_lon_mask
* What it does: get the land-ocean mask in the given netCDF file
* Inputs(data type): file path(string), variable name(string)
* Outputs(data type): the land-ocean mask in the file(numpy array)
* How it interacts with other components: the land-ocean mask will be used to mask the (calculated) temperature data from `get_temperature`

### 3. get_zone
* What it does: given the score, or any value, return the zone that the score belongs to
* Inputs(data type): score(int or float), bin size(int or float)
* Outputs(data type): the zone that the given score belongs to 
* How it interacts with other components: score is calculated based off temperature data from `get_temperature`