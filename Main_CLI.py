from pathlib import Path
from sys import path

from organizer import FileOrganizer
import argparse


def main():
    # Creating a parser
    parser = argparse.ArgumentParser(description="AutoFile Organizer\nAutomatically Organize files based on their file type")

    # Adding Arguments (Positional(Required) & Optional)
    parser.add_argument("location", type=str, help="Input the file location for organizing.")
    parser.add_argument("--dry-run", action="store_true", help="Used to run a preview without making changes to the files")

    # Parse Arguments (Access values via dot.notations)
    args = parser.parse_args()
    organizer = FileOrganizer(args.location, args.dry_run)

    # Existing path validation logic in organizer.py
    if not organizer.validate_location():
        return

    # Running organize_folder() method in organizer.py
    organizer.organize_folder()

    # Check if running dry run or not to show below print
    if args.dry_run:
        print(f"Dry run complete. {organizer.count_files} files would be moved.\nNo files were changed")

if __name__ == "__main__":
    main()