import csv
from unicodedata import category

with open (
    'C:/Users/A515-43/Documents/GIT-HUB/reccomendation_system/reccomentation_\
        system/destination_data.csv'
    ) as csv_file:
    csv_read = csv.reader(csv_file, delimiter = ',')
    destination_list = list(csv_read)

destination_collection, data_list = [
    destination[0] for destination in destination_list
    ], [
        data_set[1:] for data_set in destination_list
        ]

destination_index = {
    destination:data for (destination, data) 
    in zip (destination_collection, data_list)
    }


bike = {"road", "mountain", "urban"}