# MHD_API
Python package for accessing data about MHD in Bratislava
## Functions:
### GetBusLocation():
+ Used to get live location of every bus
+ Updated every 2-3 minutes
+ Returns list with Bus class instances
### Class Bus:
```python
class Bus:
    def __init__(self, key, label, transport_type_code, transport_type_name, latitude, longitude, lineName, finalStation, delay, azimuth, state):
        self.key = key # Number of the bus for example 2602(Solaris Urbino 12 hydrogen)
        self.label = label # Line number of the bus usually it mathces with lineName
        self.transport_type_code = transport_type_code # Letter that defines what type of vehicle is it(bus,tram, trolleybus)
        self.transport_type_name = transport_type_name # Type of vehicle said in a word, be aware it is in czech for some reason
        self.latitude = latitude # Latitude of the bus
        self.longitude = longitude # Longitude of the bus
        self.lineName = lineName # Line number of the bus
        self.finalStation = finalStation # Final destination of the bus
        self.delay = delay # Delay of the bus rounded up to minutes
        self.azimuth = azimuth # I have no idea what is this, It should be some angle. If you know what it is feel free to message me on Discord or create a Issue
        self.state = state # I am not really sure what is this, it is 1 or 0 or None
```

### GetStations():
+ Used to get data about all stations
+ Returns list with Station class instances
### Class Station:
```python
class Station:
    def __init__(self, name, ID, longitude, latitude):
        self.name = name # Name of the station
        self.ID = ID # Id of the station, it is used in other functions
        self.longitude = longitude # Latitude of the station
        self.latitude = latitude # Longitude of the station
```
### GetBusLines():
+ Used to get all bus lines and their IDs
+ returns a list with Line class instances
### Class Line:
```python
class Line:
    def __init__(self, lineNumber, ID):
        self.lineNumber = lineNumber # Line number, be aware it is a string
        self.ID = ID # ID of the bus line
```
### GetBusRouteByID(ID, *direction*):
+ Used to get route details about specific Bus line, you input the ID of the line
+ Variable direction is not reqiured, it can be 1 or 0
+ Returs a list with Station class instances in order of chosen direction
> [!IMPORTANT]
> ID must be a String
### GetBusRouteByName(name, *direction*): 
+ Used to get route details about specific Bus line, you input the line number(30, 63) of the line
+ Variable direction is not reqiured, it can be 1 or 0
+ Returs a list with Station class instances in order of chosen direction
> [!IMPORTANT]
> Name must be a String
### GetStationByName(name):
+ Used to get ID of a staion using its name
+ returns ID as a string
> [!IMPORTANT]
> Name must be a String
### GetBusLineByName(number):
+ Used to get ID of a bus line using its line number
+ returns ID as a string
> [!IMPORTANT]
> Name must be a String
## Other information
+ If you have any problems,question or a suggestion feel free to submit a Issue or message me on Discord: mrtineu
+ I do not take any responsibility for uses
+ If you want to get live departures and search routes try using [IMHD API](https://github.com/mrshu/python-imhdsk-api)
+ My source of data is from this old forgotten website from DPB https://www.mhdspoje.cz/dpb/
+ Import this package like this:
```python from
from mhd_api import *
```
> [!NOTE]
> Sometimes the load time is a few seconds, so do not be suprised
