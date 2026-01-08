#======================================================================
# Called by:
#   [1] advancement: advancement/_events/place
#======================================================================

advancement revoke @s only dynamic_campfires:_events/place

scoreboard players set @s lights.raycast 0
execute positioned as @s rotated as @s anchored eyes positioned ^ ^ ^ run function dynamic_campfires:raycast