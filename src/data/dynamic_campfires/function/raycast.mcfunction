#======================================================================
# Called by:
#   [1] dynamic_campfires:_events/on_place
#   [2] dynamic_campfires:raycast
#======================================================================

# Block check (offset section for better precision)
execute align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~ ~0.075 ~ align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~ ~-0.075 ~ align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~-0.075 ~ ~ align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~0.075 ~ ~ align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~ ~ ~-0.075 align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create
execute positioned ~ ~ ~0.075 align xyz if predicate dynamic_campfires:being_setup run return run function dynamic_campfires:create

# Raycast logic
scoreboard players add @s lights.raycast 1
execute if score @s lights.raycast = .limit lights.raycast run return fail
execute positioned ^ ^ ^0.1 run function dynamic_campfires:raycast