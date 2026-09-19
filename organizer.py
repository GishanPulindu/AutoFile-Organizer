from pathlib import Path
import shutil

# To track the created folders inside the directory
created = []
dir_name = {"Documents": (".docx", ".xlsx", ".pptx", ".pdf", ".txt"), "Images": (".jpg", ".png", ".jpeg"),
                "Media": (".mp3", ".mp4", ".avi", ".wav"),
                "Archive": (".zip", ".rar", ".7z"), "Other": (".html", ".exe")}

# function for creation of directory
def create_directory(loc,i):
    for name, ext in dir_name.items():
        if i.suffix in ext:
            if name not in created:
                created.append(name)
                folder = loc/name
                folder.mkdir(parents=True, exist_ok=True)
            return

# Function used to move files to the created folders in organization
def move_file(l,i):
    for name, ext in dir_name.items():
        if i.suffix in ext:
            shutil.move(i, l/name/i.name)

def main():
    # Get the location of the folder to be organized
    loc = input("Input the location of the folder: ")
    if not loc:
        print("No folder has been selected")
        return
    location = Path(loc)

    if not location.exists():
        print("This folder does not exist.")
        return
    if not location.is_dir():
        print("This is not a folder.")
        return
    if not any(location.iterdir()):
        print("This folder is empty.")
        return

    print("Creating folders.....")

    for item in location.iterdir():
        if item.is_file():
            create_directory(location,item)

    print("Folders have been created!")

    print("Moving files.....")

    for item in location.iterdir():
        if item.is_file():
            move_file(location, item)

    print("Files moved to respective folders!")


if __name__ == "__main__":
    main()