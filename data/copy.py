import sys
sys.dont_write_bytecode = True

import shutil
from pathlib import Path

from config import DESTINATION_PATH


def main():
    # Paths
    src = Path(__file__).parent.parent / "src"
    dest = Path(DESTINATION_PATH)

    # Ensure destination exists
    dest.mkdir(parents=True, exist_ok=True)

    # Clear destination
    for item in dest.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

    # Copy everything from src to dest
    for item in src.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


if __name__ == "__main__":
    main()