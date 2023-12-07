
import requests
import json
from datetime import datetime

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

class Station:
    def __init__(self, name, ID, longitude, latitude):
        self.name = name # Name of the station
        self.ID = ID # Id of the station, it is used in other functions
        self.longitude = longitude # Latitude of the station
        self.latitude = latitude # Longitude of the station

class Line:
    def __init__(self, lineNumber, ID):
        self.lineNumber = lineNumber # Line number, be aware it is a string
        self.ID = ID # ID of the bus line

def GetBusLocation():
    buses = []
    r = requests.get("https://skeleton.dpb.sk/Infotainment/VehicleState/__VehicleStateMapData?_ticket=973e3385-98cc-47a2-bb26-993fa41f26d2")
    locations = json.loads(r.text)
    for data in locations:
        bus_ins = Bus(data["Key"], data["Label"], data["TransportTypeCode"], data["TransportTypeName"],
                      data["Location"]["Latitude"], data["Location"]["Longitude"], data["LineName"],
                      data["FinalStationName"], data["Delay"], data["Azimuth"], data["State"])
        buses.append(bus_ins)
    return buses

def GetStations():
    r = requests.get("https://www.mhdspoje.cz/jrw50/php/5_1/ListStaniceJSON.php?location=6&packet=443&callback=getStaniceData")
    data = r.text
    data = data.split("""selfobj.getStaniceData(6, 443, """)
    data = data[1].split(");")
    data = data[0].encode("windows-1250")
    data = json.loads(data)
    stations = []
    for i in data:
        name = i[0].split(",")
        station = Station(name[0], i[3], i[2], i[1])
        stations.append(station)
    return stations

def GetBusLines():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d_%m_%Y")
    r = requests.get("https://www.mhdspoje.cz/jrw50/php/ListLinkyJSON.php?location=6&packet=443&datum="+formatted_date+"&target=select_linka&ptl=1&callback=getLinkyData")
    data = r.text
    data = data.split("""selfobj.getLinkyData(6, 443, "select_linka",""" )
    data = data[1].split(");")
    data = data[0]
    data = data.replace(" ","")
    data = json.loads(data)
    lines = []
    for i in data:
        name = i[1]
        line = Line(name, i[0])
        lines.append(line)
    return lines

def GetBusRouteByID(ID, direction=0):
    r = requests.get("https://www.mhdspoje.cz/jrw50/php/5_1/loadRouteJSON.php?linka={linka}&smer={smer}&location=6&packet=442&callback=getRouteData".format(linka=ID, smer=direction))
    data = r.text
    data = data.split("selfobj.getRouteData(")
    data = data[1].split(");")
    data = data[0].encode("windows-1250")
    data = json.loads(data)
    route = []
    for i in data:
        name = i[3].split("|")
        name = name[0]
        stop = Station(name, GetStationByName(name), i[2], i[1])
        route.append(stop)
    return route

def GetBusRouteByName(name, direction=0):
    ID = GetBusLineByName(name)
    r = requests.get("https://www.mhdspoje.cz/jrw50/php/5_1/loadRouteJSON.php?linka={linka}&smer={smer}&location=6&packet=442&callback=getRouteData".format(linka=ID, smer=direction))
    data = r.text
    data = data.split("selfobj.getRouteData(")
    data = data[1].split(");")
    data = data[0].encode("windows-1250")
    data = json.loads(data)
    route = []
    for i in data:
        name = i[3].split("|")
        name = name[0]
        stop = Station(name, GetStationByName(name), i[2], i[1])
        route.append(stop)
    return route

def GetStationByName(name):
    for i in GetStations():
        if i.name == name:
            return i.ID
        else:
            continue

def GetBusLineByName(number):
    for i in GetBusLines():
        print(i.lineNumber)
        if i.lineNumber == number:
            return i.ID
        else:
            continue

