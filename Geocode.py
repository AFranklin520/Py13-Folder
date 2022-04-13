# FranklinP9
# Programmer: Anthony Franklin
# EMail: afranklin18@cnm.edu
# Purpose: demonstrate how to define a class


from math import sin, cos, sqrt, atan2, radians


class GeoPoint:

    def __init__(self,lat=0,lon=0,description='TBD'):
        self.__lon=lon
        self.__lat=lat
        self.__description=description

    def SetPoint(self,coords):
        self.__lat=coords[0]
        self.__lon=coords[1]

    def GetPoint(self):
        return float(self.__lat),float(self.__lon)

    def SetDescription(self,description):
        self.__description=description

    def GetDescription(self):
        return self.__description

    def Distance(self,Location):
        R=6371
        lat1 = radians(float(Location.GetPoint()[0]))
        lon1 = radians(float(Location.GetPoint()[1]))
        lat2 = radians(self.__lat)
        lon2 = radians(self.__lon)
        dlon= lon2-lon1
        dlat=lat2-lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        Distance= round((R*c)*0.6214,2)

        return Distance

