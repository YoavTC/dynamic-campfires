#======================================================================
# Called by:
#   [1] dynamic_campfires:raycast
#======================================================================

# Summon tracking entity & setup block (data is on block, entity is just for locating)
summon marker ~ ~ ~ {Tags:[light_marker]}
data modify block ~ ~ ~ components."minecraft:custom_data".setup set value 1

# Reverse check
execute if predicate dynamic_campfires:is_sneaking run data modify block ~ ~ ~ components."minecraft:custom_data".reversed set value true