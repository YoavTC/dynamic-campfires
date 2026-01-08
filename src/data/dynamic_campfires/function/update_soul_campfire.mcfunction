#======================================================================
# Called by:
#   [1] dynamic_campfires:update
#======================================================================

# Turn ON normal campfires during night
execute if block ~ ~ ~ soul_campfire[facing=north]{components:{"minecraft:custom_data":{"reversed":0b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=north]
execute if block ~ ~ ~ soul_campfire[facing=east]{components:{"minecraft:custom_data":{"reversed":0b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=east]
execute if block ~ ~ ~ soul_campfire[facing=south]{components:{"minecraft:custom_data":{"reversed":0b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=south]
execute if block ~ ~ ~ soul_campfire[facing=west]{components:{"minecraft:custom_data":{"reversed":0b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=west]

# Turn OFF normal campfires during day
execute if block ~ ~ ~ soul_campfire[facing=north]{components:{"minecraft:custom_data":{"reversed":0b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=north]
execute if block ~ ~ ~ soul_campfire[facing=east]{components:{"minecraft:custom_data":{"reversed":0b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=east]
execute if block ~ ~ ~ soul_campfire[facing=south]{components:{"minecraft:custom_data":{"reversed":0b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=south]
execute if block ~ ~ ~ soul_campfire[facing=west]{components:{"minecraft:custom_data":{"reversed":0b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=west]

# Turn ON reversed campfires during day
execute if block ~ ~ ~ soul_campfire[facing=north]{components:{"minecraft:custom_data":{"reversed":1b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=north]
execute if block ~ ~ ~ soul_campfire[facing=east]{components:{"minecraft:custom_data":{"reversed":1b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=east]
execute if block ~ ~ ~ soul_campfire[facing=south]{components:{"minecraft:custom_data":{"reversed":1b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=south]
execute if block ~ ~ ~ soul_campfire[facing=west]{components:{"minecraft:custom_data":{"reversed":1b}}} if predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=true,facing=west]

# Turn OFF reversed campfires during night
execute if block ~ ~ ~ soul_campfire[facing=north]{components:{"minecraft:custom_data":{"reversed":1b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=north]
execute if block ~ ~ ~ soul_campfire[facing=east]{components:{"minecraft:custom_data":{"reversed":1b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=east]
execute if block ~ ~ ~ soul_campfire[facing=south]{components:{"minecraft:custom_data":{"reversed":1b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=south]
execute if block ~ ~ ~ soul_campfire[facing=west]{components:{"minecraft:custom_data":{"reversed":1b}}} unless predicate dynamic_campfires:is_day run return run setblock ~ ~ ~ soul_campfire[lit=false,facing=west]