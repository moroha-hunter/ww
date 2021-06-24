from numpy import random
#0 - the central circle, 1 - the plane, green zone, 2 - the mountain zone, 3 - the forest zone, 4 - the wasteland zone
#0,2,1,3,4,4,3,2,1,2 etc...
def init_zones_generation():
 first_model_size = 100 #how many zones will be generated on initial world generation
 zones = [1, 2, 3, 4] #zone types in a list
 the_central_zone = 0 #the central zone - the central of the world
 first_world_model = random.choice(zones, size=(first_model_size)) #zones random generation
 first_world_model[0] = the_central_zone #replace the first element in array with the central zone
 return first_world_model #return the array with zones sequence
