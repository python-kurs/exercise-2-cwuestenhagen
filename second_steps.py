# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database["GOES"] = 2000
sat_database["worldview"] = 0.31
sat_database

# 2) print out all satellite names contained in the dictionary [2P]

print("I have the following satellites in my database:", sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
print("I have the following satellites in my database:", sat_database.keys())
answer = input("From which satellite would you like to know the resolution?")

   
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

answer = input("From which satellite would you like to know the resolution?")
if answer == "METEOSAT": 
    print("METEOSAT is in the database.")
elif answer =="LANDSAT":
    print("LANDSAT is in the database.")
elif answer =="MODIS": 
    print("MODIS is in the database.")
elif answer =="GOES":
    print("GOES is in the database.")
elif answer =="worldview": 
    print("worldview is in the database.")
else:
    print("Your satellite is not in the database.")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P]
    
answer = input("From which satellite would you like to know the resolution?")
if answer == "METEOSAT": 
    print("The satellite METEOSAT is in the database and has the resolution of", sat_database[answer],".")
    #print("The satellite METEOSAT has a resolution of", sat_database["METEOSAT"],".")
elif answer =="LANDSAT": 
     print("The satellite LANDSAT has a resolution of", sat_database[answer],".")
     #print("The satellite LANDSAT has a resolution of", sat_database["LANDSAT"],".")
elif answer =="MODIS": 
    print("The satellite MODIS has a resolution of", sat_database[answer],".")
    #print("The satellite MODIS has a resolution of", sat_database["MODIS"],".")
elif answer =="GOES":
    print("The satellite GOES has a resolution of", sat_database[answer],".")
    #print("The satellite GOES has a resolution of", sat_database["GOES"],".")
elif answer =="worldview": 
    print("The satellite worldview has a resolution of", sat_database[answer],".")
    #print("The satellite worldview has a resolution of", sat_database["worldview"],".")
