from pathlib import Path
from shutil import copy
import sys

def files_sorter(src_dir: Path, dst_dir: Path):
    """
    Recursively collects all files from src_dir 
    and copies them to dst_dir according to extensions.
    Files without extension are copied to dst_dir/no_extension
    """
    try:
        if src_dir.is_dir():
            for item in src_dir.iterdir():
                # catching exceptions for each item separately
                try:
                    if item.is_dir():
                        # recursive call
                        files_sorter(item, dst_dir)
                    elif item.is_file():
                        subdir = item.suffix[1:]
                        if not subdir:
                            subdir = "no_extension"
                        dst_subdir = dst_dir / subdir.casefold()
                        dst_subdir.mkdir(parents = True, exist_ok = True)
                        dst_name = dst_subdir / item.name
                        if dst_name.exists():
                             print(f"ERROR: Can't copy file {str(item)}, destination file already exists: {dst_name}")
                        copy(item, dst_name)
                except IOError as e:
                    print(f"ERROR: {e}")
        else:
            print(f"ERROR: source directory \"{src_dir}\" should be existing folder!")
    except IOError as e:
        print(f"ERROR: {e}")

def main():
    """
    Entry point
    """
    # parsing command line arguments
    if len(sys.argv)<2 or len(sys.argv)>3:
        print(f"Usage HINT: {sys.argv[0]} <source_directory> [<destination_directory>]")  
        sys.exit()
    src_dir = Path(sys.argv[1])
    dst_dir = Path("dist")
    if len(sys.argv) == 3:
        dst_dir = Path(sys.argv[2])
    files_sorter(src_dir, dst_dir)

if __name__ == "__main__":
    main()
