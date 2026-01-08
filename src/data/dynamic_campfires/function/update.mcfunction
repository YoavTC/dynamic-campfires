#======================================================================
# Called by:
#   [1] dynamic_campfires:_tick
#======================================================================

# Remove marker if block not found
execute unless predicate dynamic_campfires:is_campfire run return run function dynamic_campfires:destroy

execute if block ~ ~ ~ campfire run return run function dynamic_campfires:update_campfire
execute if block ~ ~ ~ soul_campfire run return run function dynamic_campfires:update_soul_campfire