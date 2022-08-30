##This program gets your input and tells you the ideal road for 
# your altitude and distance objectives!

from Graph import Graph
from Vertex import Vertex
from queues import Queue
from node import Node

import distance_charter
from distance_charter import get_dist, destination_index, bike
from traveling_cyclist import print_graph,  build_destination_graph as bdg

#start of validate_answer
def validate_answer():
    print("Please answer 'y' for yes or 'n' for no\n")
    answer = input()
    answers = ['y', 'n']
    while answer.lower() not in answers:
        return validate_answer()
    if answer.lower() == 'y':
        return True
    else:
        return False 

#start of greet
def greet():
    rider_name = input("Hello, we would like to know your name\n\n")
    print(
        f"Welcome {rider_name}, we'll help you find the right path for today's \
        ride\n"
        ) 
    return rider_name

#start of bike_type
def bike_type(dest_dict = destination_index):
    print("We'd like to know the kind of bike you use")
    bike_option = [b + ", " for b in bike]
    print(str(bike_option))
    bike_type_chosen = input()
    while bike_type_chosen.lower() not in bike:
        bike_type()
    print(f"Ok, your chosen bike type is {bike_type_chosen}\n")
    valdt = validate_answer()
    if valdt == True:
       
       return bike_type_chosen.title()
    else:
        print('Sorry, we need to know your bike type to continue\n')
        return bike_type()

def get_viable_dest(bike_type_chosen):
    viable_destinations = [
        str(destination) for destination in list(destination_index.keys()) 
        if bike_type_chosen in list(destination_index[destination])
        ]
    return viable_destinations

#start of destinations
def get_destination(viable_destinations):

    print("These are the possible destinations based on your riding style:\n")
    print(list(viable_destinations))

    print("\nPlease choose your origin:\n")
    origin = input()
    while origin.title() not in viable_destinations:
        print(
            "Sorry, we didn't get the appropriate origin, it should be one\
            of the listed below\n"
            )
        return get_destination()

    print("\nPlease choose your destiantion:\n")
    destination = input()
    while destination.title() not in viable_destinations:
        print(
            "Sorry, we didn't get the appropriate destination, it should be one\
            of the listed below\n"
            )
        return get_destination()
    return origin.title(), destination.title()

#start of no_int (control fnctn)
def not_int():
    print(
        "\nWhops! try entering an integer, i.e. a rounded up number, like 2,\
        133, or 9999\n"
        )

#Start of get_goals
def get_goals():
    print("We'd like to know the distance in km you're going after!\n\
        you may type a figure in integers")
    distance = input()
    while int(distance) <= 0:  
        not_int()
        return get_goals()
    print(f"Good, so you're after {distance} km, right?\n")
    answer = validate_answer()
    if answer == False:
        return get_goals()
 
    print(
        f"Great!\n \tWe're good to go, you're going for {distance}km in length"
        )

    return int(distance) # int(altitude)

#previously function had an argument "altitude" that matched dataset altimetry,
#it's removed due to inability to use it properly at current level of project.
def optimal_route(origin, destination, distance, graph = Graph()): 
    
    attained_distance = 0
    start = graph.graph_dict[origin]
    end = graph.graph_dict[destination]
    route = Graph(True)

    departure = start
    visited = Queue(4)
    not_available_dest = []

    while attained_distance < distance :
        if visited.get_size() == visited.max_size:
            visited.dequeue()
            not_available_dest.pop(0)
                
        destinations_from_current = departure.get_edges()
        if not_available_dest:
            #print(not_available_dest)
            for d in not_available_dest:
                destinations_from_current.remove(d)     
        print(destinations_from_current)

        distances = list(map(lambda x: departure.get_edge_weight(x),
         destinations_from_current))
        next_destination = graph.graph_dict[destinations_from_current
            [distances.index(max(distances))]
            ]

        visited.enqueue(departure.value)
        not_available_dest.append(departure.value)
        departure_vtx = Vertex(departure)
        route.add_vertex(departure_vtx)
        
        attained_distance += departure.get_edge_weight(next_destination.value)
        print(f"so far {attained_distance} km done")
        
        print(f"now to {next_destination.value}")
        next_dest_vtx = Vertex(next_destination)
        
        route.add_vertex(next_dest_vtx)
        route.add_edge(departure_vtx, next_dest_vtx)
        departure = next_destination

    result = route.graph_path()
    print(f"Great work, you've done {attained_distance} kms, going from:\n \
    {result}")    


dest_check = list(destination_index.keys())

#first
user_name = greet()

#get bike type
your_bike = bike_type()

#get testinations
destinations = get_viable_dest(your_bike)

#build the graph
user_destinations = bdg(True, destinations)

#get chosen destination
origin, destination  = get_destination(destinations)
 
#get goals
goal_distance = get_goals()

#run
optimal_route(origin, destination, goal_distance, user_destinations )
