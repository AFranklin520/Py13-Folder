# FranklinP13
# Programmer: Anthony Franklin
# EMail: afranklin18@cnm.edu
# Purpose: demonstrate python database

#Manipulate Database with Python

import sys
import sqlite3
from Geocode import GeoPoint

def header():
    'Message to user describing function'
    print("\n\nProgram reads points from a database and compares them to user input. You may add locations to the database by modifying the 'locations.txt' file included.")
    print("\nLet's get started!\n")

#MainProgram
header()
def convert(value):
       return(value)

#creating/connecting to DB
conn = sqlite3.connect('GeoPoint.db')
curs=conn.cursor()

#creating table after ensuring it doesn't already exist
curs.execute('''
CREATE TABLE IF NOT EXISTS geopoint (
lat FLOAT,
lon FLOAT,
description TEXT
)
''')

#importing data from .txt file into DB
points=[]
query='INSERT INTO geopoint VALUES(?,?,?)'
for line in open('locations.txt'):
    fields = line.split(',')
    vals = [convert(f) for f in fields[:]]
    curs.execute(query,vals)
conn.commit()
curs.execute('SELECT * FROM geopoint')
data=curs.fetchall()

#setting the points for the program
for row in data:
            plat=row[0]
            plon=row[1]
            pdesc=row[2]
            place=GeoPoint(plat,plon,pdesc)
            points.append(place)  
conn.close() #Making sure to close the DB


again='y'
while again=='y':
        dist=[]



#setting point with user input    
        userDescription=input("What is your location's name?\n")
        print("Enter both coordinates as decimal degrees separated by a comma")
        print("Example: \nFor San Francisco, California, enter: 35.658487,-105.995741")            
        userLocation=(input("Enter your coordinates: \n").split(','))
        userGeo=GeoPoint(float(userLocation[0]),float(userLocation[1]),userDescription)
        
#comparing distance between external data and user input and putting those distances in a list
        dist=["Max Value",float("inf")]
        for p in points:
            d=userGeo.Distance(p)
            if d<dist[1]:
                dist[0]=p.GetDescription()
                dist[1]=d
        
#output to user
        print(f"\nLooks like {userDescription} is closest to {dist[0]}\nLocated at \n{userLocation[0], userLocation[1]}.\n\nYou are {dist[1]} miles away from there.")

#continuing or ending loop        
        again=input("\nDo you want to go again? Y/N: ").lower().strip()
        if again=='y':
            print("\n\nAwesome, let's go!\n\n")
        else:
            print("\nHope you enjoyed the app. See ya later!")
            break
