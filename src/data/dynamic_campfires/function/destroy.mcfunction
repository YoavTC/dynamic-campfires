#======================================================================
# Called by:
#   [1] dynamic_campfires:update
#======================================================================

# Remove entity & drop item
kill @s
summon item ~ ~ ~ {Item:{id:"minecraft:daylight_detector"},Motion:[0d, .2d, 0d]}