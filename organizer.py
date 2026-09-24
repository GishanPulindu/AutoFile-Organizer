from pathlib import Path
import shutil


class FileOrganizer:

    dir_name = {
        "Documents": (".docx", ".xlsx", ".pptx", ".pdf", ".txt", ".csv", ".rtf", ".md", ".odt"),
        "Images": (".jpg", ".png", ".jpeg", ".gif"),
        "Audio": (".mp3", ".wav", ".m4a", ".flac", ".aac"),
        "Video": (".mp4", ".avi", ".mov", ".mkv", ".webm"),
        "Archive": (".zip", ".rar", ".7z"),
        "Applications": (".exe", ".msi")
    }


    def __init__(self, location, dry_run=False):
        self.location = Path(location)
        self.dry_run = dry_run

    # Method used for input validation
    def validate_location(self):
        if not self.location.exists():
            print("This folder does not exist.")
            return False
        if not self.location.is_dir():
            print("This is not a folder.")
            return False
        if not any(self.location.iterdir()):
            print("This folder is empty.")
            return False
        return True

    # Method used to get the category of folder
    def get_category(self, file):
        for name, extensions in self.dir_name.items():
            if file.suffix.lower() in extensions:
                return name
        return "Other"

    # Method used to create folders needed for organization
    def create_directory(self, file):
        folder = self.location / self.get_category(file)
        if self.dry_run:
            return
        folder.mkdir(parents=True, exist_ok=True)
        return

    # Method used to move files to respective folders
    def move_file(self, file):
        destination = self.unique_filename(self.get_category(file), file)
        if self.dry_run:
            print(f"[DRY RUN] WOULD MOVE: {file.name} -> {destination}")
            return
        shutil.move(file, destination)
        return

    # Method handles filename conflicts
    def unique_filename(self, folder, file):
        counter = 1
        path = self.location / folder / file.name
        while path.exists():
            path = self.location / folder / f"{file.stem}_{counter}{file.suffix}"
            counter += 1
        return path

    # Method that provides the main logic
    def organize_folder(self):

        print("Creating folders.....")

        for item in self.location.iterdir():
            if item.is_file():
                self.create_directory(item)

        print("Folders have been created!")

        print("Moving files.....")

        for item in self.location.iterdir():
            if item.is_file():
                self.move_file(item)

        print("Files moved to respective folders!")


