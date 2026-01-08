#======================================================================
# Called by:
#   [1] tag: minecraft:load
#======================================================================

# Setup raycast scoreboard
scoreboard objectives add lights.raycast dummy
scoreboard players set .limit lights.raycast 100

# Schedule tick
function dynamic_campfires:_tick