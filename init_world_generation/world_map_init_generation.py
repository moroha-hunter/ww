from numpy import random
#0 - the central circle, 1 - the plane, green zone, 2 - the mountain zone, 3 - the forest zone, 4 - the wasteland zone
#0,2,1,3,4,4,3,2,1,2 etc...
def init_zone_sequence_generation():
 first_world_model_zones_total_amount = 100 #how many zones will be generated on initial world generation
 zone_types = [1, 2, 3, 4] #zone types in a list
 the_central_zone_id = 0 #the central zone - the central of the world
 first_world_model_zone_sequence = random.choice(zone_types, size=(first_world_model_zones_total_amount)) #zones random generation
 first_world_model_zone_sequence[0] = the_central_zone_id #replace the first element in array with the central zone
 return first_world_model_zone_sequence #return the array with zones sequence
def init_zone_sizes_generation():
 the_central_zone_range = 100
 
 return first_world_model_zone_sizes
