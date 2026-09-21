from pathlib import Path
import shutil


dir_name = {"Documents": (".docx", ".xlsx", ".pptx", ".pdf", ".txt", ".csv", ".rtf"),
                "Images": (".jpg", ".png", ".jpeg", ".gif"),
                "Media": (".mp3", ".mp4", ".avi", ".wav"),
                "Archive": (".zip", ".rar", ".7z")}

# function for creation of directory
def create_directory(loc,i):
    for name, ext in dir_name.items():
        if i.suffix.lower() in ext:
            folder = loc/name
            folder.mkdir(parents=True, exist_ok=True)
            return
    # If the extension is unknown creates a folder as "Other"
    folder = loc/"Other"
    folder.mkdir(parents=True, exist_ok=True)


# Function used to move files to the created folders in organization
def move_file(l,i):
    for name, ext in dir_name.items():
        if i.suffix.lower() in ext:
            file = unique_filename(l, name, i)
            shutil.move(i, file)
            return
    shutil.move(i, l/"Other"/i.name)

# Function used to create unique filename if file already available using num incrementer
def unique_filename(sys, folder, file):
    counter = 1
    path = sys/folder/file.name
    while path.exists():
        path = sys/folder/f"{file.stem}_{counter}{file.suffix}"
        counter += 1
    return path


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