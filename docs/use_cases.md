# Use Cases of EV Temperature Map
This document describes some of the potential use cases for the EV Temperature Map created in this project.

## Use Case 1

**USER CASE**: Wants to know the temperature effect on the range of their EV at a certain time of your based off of their location.

**MAP Provides**: 
- Average temperature of the location for a certain day
- Minimum and maximum temperature of a location for a certain day
- How many days in a year they will experience different brackets of ranges:
    - E.g. How many days the temperature will be in certain temperature ranges (for example, between -20$^{\circ}$C and 0$^{\circ}$C which results in X% decrease in range)
    

## Use Case 2

**USER CASE**: Potential EV purchaser living in an extremely cold area wants to know longevity and temperature effects on their battery if they buy an EV in their location.

People living in Fairbanks, for example, wants to know
- If it's worth buying an EV
- How much battery should be charged enough to, or if they can really, reach a certain destination
- How many days can their car stand parked in a garage without degradation of the battery
- How serious will the degradation be
- If the battery is enough to heat inside of the vehicle during a trip

**MAP Provides**: 
- How many days in a year they will experience different brackets of ranges
    - This will give a yearly degredation of battery capacity/range
    - Output: %Capacity/range loss/year for location on map
- When it is recommended to plug in EV to combat battery damage
- Help guide decision on potential need for insulated garage to store EV


## Use Case 3

**USER CASE**: Researchers need more information to be assured with the practicability of domesticating electric transportations into cold areas such as Alaska.

**Map Provides**:
- HDD for a given location and expected battery degradation
- Ocean temperature information for electric boats *(this can be removed)*


## Use Case 4

**USER CASE**: Potential EV manufactureres/salesperson helping clients choose between models or EV vs. hybrid based on their location.

**Map Provides**:
- They might use this map to possibly recommend drivers to choose rather hybrid(electric+combustible) model and which area they better go combustion mode

Example from use case 1:
![](https://github.com/ACE-P/ev_temp_map/blob/master/docs/use_case_1.png)