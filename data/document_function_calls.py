import os
import re
from pathlib import Path
from collections import defaultdict

# Get the script's directory and build relative paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Namespace configuration
NAMESPACE = "dynamic_campfires"

# Base directory for mcfunction files
FUNCTION_DIR = PROJECT_ROOT / "src" / "data" / NAMESPACE / "function"
ADVANCEMENT_DIR = PROJECT_ROOT / "src" / "data" / NAMESPACE / "advancement"
TAGS_DIR = PROJECT_ROOT / "src" / "data" / "minecraft" / "tags"

def find_function_calls(line):
    """
    Extract function calls from a line.
    Returns a list of function namespace paths.
    """
    calls = []
    
    # Pattern to match function calls: function namespace:path
    # Includes letters, numbers, underscores, and forward slashes
    function_pattern = r'function\s+([a-z_]+:[a-z0-9_/]+)'
    
    matches = re.finditer(function_pattern, line)
    for match in matches:
        func_path = match.group(1)
        calls.append(func_path)
    
    return calls

def namespace_path_to_file(namespace_path):
    if ':' in namespace_path:
        namespace, path = namespace_path.split(':', 1)
        if namespace == NAMESPACE:
            return FUNCTION_DIR / f"{path}.mcfunction"
    return None

def file_to_namespace_path(file_path):
    try:
        rel_path = file_path.relative_to(FUNCTION_DIR)
        namespace_path = str(rel_path).replace('\\', '/').replace('.mcfunction', '')
        return f"{NAMESPACE}:{namespace_path}"
    except ValueError:
        return None

def scan_advancement_triggers():
    advancement_triggers = {}
    
    if not ADVANCEMENT_DIR.exists():
        return advancement_triggers
    
    import json
    
    for advancement_file in ADVANCEMENT_DIR.rglob("*.json"):
        try:
            with open(advancement_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Check for function rewards
            if 'rewards' in data and 'function' in data['rewards']:
                func_path = data['rewards']['function']
                advancement_name = str(advancement_file.relative_to(ADVANCEMENT_DIR.parent)).replace('\\', '/').replace('.json', '')
                advancement_triggers[func_path] = advancement_name
        
        except Exception as e:
            print(f"Error reading advancement {advancement_file}: {e}")
    
    return advancement_triggers

def scan_function_tags():
    import json
    
    function_tags = {}
    
    if not TAGS_DIR.exists():
        return function_tags
    
    # Look for function tags
    function_tags_dir = TAGS_DIR / "function"
    if not function_tags_dir.exists():
        return function_tags
    
    for tag_file in function_tags_dir.rglob("*.json"):
        try:
            with open(tag_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Get the tag name (e.g., load, tick)
            tag_name = tag_file.stem
            tag_namespace = f"minecraft:{tag_name}"
            
            # Check for function values
            if 'values' in data:
                for func_path in data['values']:
                    if isinstance(func_path, str):
                        function_tags[func_path] = tag_namespace
                    elif isinstance(func_path, dict) and 'id' in func_path:
                        function_tags[func_path['id']] = tag_namespace
        
        except Exception as e:
            print(f"Error reading function tag {tag_file}: {e}")
    
    return function_tags

def build_function_call_map():
    call_map = defaultdict(set)
    
    for mcfunction_file in FUNCTION_DIR.rglob("*.mcfunction"):
        try:
            with open(mcfunction_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            caller_namespace = file_to_namespace_path(mcfunction_file)
            
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                calls = find_function_calls(line)
                for func_path in calls:
                    call_map[func_path].add(caller_namespace)
        
        except Exception as e:
            print(f"Error reading {mcfunction_file}: {e}")
    
    return call_map

def collect_function_calls():
    # Get advancement triggers
    advancement_triggers = scan_advancement_triggers()
    
    # Get function tags (load, tick, etc.)
    function_tags = scan_function_tags()
    
    # Get function calls from mcfunction files
    call_map = build_function_call_map()
    
    # Add advancement triggers
    for func_path, advancement_name in advancement_triggers.items():
        if func_path not in call_map:
            call_map[func_path] = set()
        call_map[func_path].add(f"advancement: {advancement_name}")
    
    # Add function tags
    for func_path, tag_name in function_tags.items():
        if func_path not in call_map:
            call_map[func_path] = set()
        call_map[func_path].add(f"tag: {tag_name}")
    
    # Convert sets to sorted lists for consistent output
    return {func: sorted(list(callers)) for func, callers in call_map.items()}

def add_documentation_to_function(func_namespace_path, callers):
    file_path = namespace_path_to_file(func_namespace_path)
    if not file_path or not file_path.exists():
        print(f"Warning: Could not find file for {func_namespace_path}")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if documentation already exists
        lines = content.split('\n')
        
        # Remove old documentation comments
        new_lines = []
        skip_block = False
        for line in lines:
            stripped = line.strip()
            # Start skipping when we hit the documentation header
            if stripped.startswith('#') and '=' * 10 in stripped and not skip_block:
                skip_block = True
                continue
            if skip_block:
                # Keep skipping while we're in the documentation block
                if stripped.startswith('# Called by:'):
                    continue
                elif stripped.startswith('#   ['):
                    continue
                elif stripped.startswith('#') and '=' * 10 in stripped:
                    continue
                elif stripped == '' or stripped == '#':
                    # Skip empty lines that are part of the doc block
                    # Check if next non-empty line is part of doc or actual code
                    continue
                else:
                    # Hit actual code, stop skipping
                    skip_block = False
            new_lines.append(line)
        
        # Remove leading empty lines
        while new_lines and new_lines[0].strip() == '':
            new_lines.pop(0)
        
        # Build new documentation
        doc_lines = []
        doc_lines.append("#" + "="*70)
        doc_lines.append("# Called by:")
        
        for i, caller in enumerate(callers, 1):
            doc_lines.append(f"#   [{i}] {caller}")
        
        doc_lines.append("#" + "="*70)
        doc_lines.append("\n")  # Add blank line after documentation
        
        # Insert documentation at the top
        new_content = '\n'.join(doc_lines) + '\n'.join(new_lines)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated: {func_namespace_path}")
    
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def main():
    print("Scanning function files...")
    call_map = collect_function_calls()
    
    print(f"\nFound {len(call_map)} unique functions being called.")
    print("\nAdding documentation...\n")
    
    for func_path, callers in call_map.items():
        if func_path.startswith(f'{NAMESPACE}:'):
            add_documentation_to_function(func_path, callers)
    
    print("\nDocumentation complete!")

if __name__ == "__main__":
    main()