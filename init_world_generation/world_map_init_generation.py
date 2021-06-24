from numpy import random
def init_zone_sequence_generation(first_world_model_zones_total_amount = 100, zone_types = [1, 2, 3, 4]):  #how many zones will be generated on initial world generation #zone types in a list
 the_central_zone_id = 0 #the central zone - the middle of the world
 first_world_model_zone_sequence = random.choice(zone_types, size=(first_world_model_zones_total_amount)) #zones random generation
 first_world_model_zone_sequence[0] = the_central_zone_id #replace the first element in array with the central zone
 return first_world_model_zone_sequence #return the array with zones sequence
def init_zone_ranges_generation(first_world_model_zones_total_amount = 100, the_central_zone_range = 100, min_zone_range = 20, max_zone_range = 60):
 first_world_model_zone_ranges = random.randint(min_zone_range,max_zone_range,size=first_world_model_zones_total_amount)
 first_world_model_zone_ranges[0] = the_central_zone_range
 for counter in range(len(first_world_model_zone_ranges)):
  if counter == 0:
   continue
  first_world_model_zone_ranges[counter] = first_world_model_zone_ranges[counter - 1] + first_world_model_zone_ranges[counter]
 return first_world_model_zone_ranges
