from cmath import sqrt
import random
from random import randrange
import math
import csv
from unicodedata import category

with open (
    'C:/Users/A515-43/Documents/GIT-HUB/reccomendation_system/reccomentation_system/destination_data.csv'
    ) as csv_file:
    csv_read = csv.reader(csv_file, delimiter = ',')
    destination_list = list(csv_read)

destination_collection, data_list = [
    destination[0] for destination in destination_list
    ], [data_set[1:] for data_set in destination_list]

destination_index = {
    destination:data for (destination, data) 
    in zip (destination_collection, data_list)
    }


bike = ("road", "mountain", "urban")

#the get_dist. function converts to km the longitude and latitude of tow points
def get_dist(point1, point2):
    lon1, lon2, lat1, lat2 = (
        destination_index[point1][0],
        destination_index[point2][0], 
        destination_index[point1][1], 
        destination_index[point2][1]
    )
    #return lon1, lon2, lat1, lat2
    lon1, lon2, lat1, lat2 = float(lon1), float(lon2), float(lat1), float(lat2)
    dx = (lon1-lon2)*40000*math.cos((lat1+lat2)*math.pi/360)/360
    dy = (lat1-lat2)*40000/360

    return dx, dy

def dist(x, y):
    distance = (sqrt(int(x)**2 + (y)**2))
    result = abs(distance)
    return int(result)



#print(get_dist('Akron Stadium', 'Minerva Roundabout'))

