#======================================================================
# Called by:
#   [1] dynamic_campfires:_load
#   [2] dynamic_campfires:_tick
#======================================================================

# Update campfires
execute as @e[type=marker,tag=light_marker] positioned as @s if loaded ~ ~ ~ run function dynamic_campfires:update

# Schedule tick
schedule function dynamic_campfires:_tick 50t