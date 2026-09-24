from pathlib import Path
from organizer import FileOrganizer


def main():
    # Get the location of the folder to be organized
    loc = input("Input the location of the folder: ")
    preview = False
    if not loc:
        print("No folder has been selected.")
        return
    confirm = input("Do you want to start a dry run? (Y/N) ")
    if confirm.upper() == "Y":
        preview = True
    organizer = FileOrganizer(loc, dry_run=preview)

    if not organizer.validate_location():
        return

    organizer.organize_folder()

if __name__ == "__main__":
    main()