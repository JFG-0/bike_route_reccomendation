#! This is a variation of Traveling Salesperson to 
# implement the get_coordinate function

import random
from random import randrange
from Graph import Graph
from Vertex import Vertex
#import math
import distance_charter
from  distance_charter import get_dist, dist, destination_index
#from destination_dataset import destination_index #for testing

def print_graph(graph):
  for vertex in graph.graph_dict:
    print("")
    print(vertex + " connected to")
    vertex_neighbors = graph.graph_dict[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)



def build_tsp_graph(directed):
  g = Graph(directed)
  vertices = []
  for val in ['a', 'b', 'c', 'd']:
    vertex = Vertex(val)
    vertices.append(vertex)
    g.add_vertex(vertex)
  g.add_edge(vertices[0], vertices[1], 3)
  g.add_edge(vertices[0], vertices[2], 4)
  g.add_edge(vertices[0], vertices[3], 5)
  g.add_edge(vertices[1], vertices[0], 3)
  g.add_edge(vertices[1], vertices[2], 2)
  g.add_edge(vertices[1], vertices[3], 6)
  g.add_edge(vertices[2], vertices[0], 4)
  g.add_edge(vertices[2], vertices[1], 2)
  g.add_edge(vertices[2], vertices[3], 1)
  g.add_edge(vertices[3], vertices[0], 5)
  g.add_edge(vertices[3], vertices[1], 6)
  g.add_edge(vertices[3], vertices[2], 1)
  return g

def build_destination_graph(directed, lst): 
 
  g = Graph(directed)
  vertices = []
  
  for val in lst: 
    vertex = Vertex(val)
    vertices.append(vertex.value)
    g.add_vertex(vertex)
  
  for vertex in range(0, len(vertices)):
    temp_list = vertices.copy()
    temp_list.remove(vertices[vertex])

    for remaining_v in range(0,len(temp_list)):
      #get_dist uses as default a set#dictionary, these strings should 
      # return values
      x, y = get_dist(vertices[vertex], temp_list[remaining_v]) 
      distance = dist(x,y)
          
      g.add_edge(
        g.graph_dict[vertices[vertex]], g.graph_dict[temp_list[remaining_v]], 
        distance
        )
  return g


def all_visited(visited_vertices):
  for vertex in visited_vertices:
    if visited_vertices[vertex] == "unvisited":
      return False
    return True 

# Define your functions below:
def traveling_salesman(graph):
  ts_path = ""
  visited_vertices = {x: "unvisited" for x in graph.graph_dict}
  current_vertex = random.choice(list(graph.graph_dict))
  visited_vertices[current_vertex] = "visited"
  ts_path += current_vertex
  visited_all_vertices = all_visited(visited_vertices)
  while not visited_all_vertices:
    current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
    current_vertex_edge_weights = {}
    for edge in current_vertex_edges:
      current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(edge)
    found_next_vertex = False
    next_vertex = ""
    while not found_next_vertex:
      if current_vertex_edge_weights is None:
        break
      next_vertex = min(current_vertex_edge_weights, key=current_vertex_edge_weights.get)
      if visited_vertices[next_vertex] == "visited" :
        current_vertex_edge_weights.pop(next_vertex)
      else:
        found_next_vertex = True
      
      if current_vertex_edge_weights is None:
        visited_all_vertices = True
      else:
        current_vertex = next_vertex
        visited_vertices[current_vertex] = "visited"
        ts_path += current_vertex
      visited_all_vertices = all_visited(visited_vertices)
    print(ts_path)



#test

#destinations = [dest_name for dest_name in destination_index.keys()]

#our_dest_graph = build_destination_graph(True, destinations) 
#Should return a graph


#print(our_dest_graph.graph_dict.values())

#x, y  = get_dist('Akron Stadium', 'Minerva Roundabout') # gets x, y
#print(dist(x, y)) # returns distance