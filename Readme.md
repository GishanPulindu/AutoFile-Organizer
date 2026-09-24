# 📌 AutoFile Organizer

This project is designed to organize files in a computer automatically without taking up hours of time, also demostrates the use of Pathlib & Shutil while handling common errors & complications in code.

---

## 🚀 Features

* Creation of folders
* Moving files to appopriate folders
* Handling filename duplicates
* Handling unknown extentsions
* Command Line interface

---

## 🛠️ Technologies Used

* Python 3
* Pathlib
* Shutil

---

## ⚙️ How It Works

1. Enter a folder path
    The program asks the user to provide the path of the folder they want to organize.
    Enter the path
     copy & paste as shown below:
        **C:\Users\name\Documents\folder_name**

2. Validate the folder
    It checks whether the provided path exists, is a directory, and contains files.

3. Identify file types
    Each file is checked using its file extension. The program uses predefined categories such as:
        Documents
        Images
        Media
        Archive
        Other
    *Might have changes in future*

4. Create category folders
    The required category folders are created inside the selected folder.

5. Move the files
    Each file is moved into the folder corresponding to its file type.

6. Handle duplicate filenames
    If a file with the same name already exists, the program creates a unique filename by adding a number to the filename instead of overwriting the existing file.

---

## 📦 Installation

1. **Clone the repository**

    ```
    git clone https://github.com/GishanPulindu/Smart-File-Organizer.git
    cd AutoFile-Organizer
    ```

2. **Run the application**

    ```
    python Main_CLI.py
    ```

---

## 📁 Project Structure

    ```
    Smart-File-Organizer/
    │── Organizer.py
    │── Main_CLI.py
    └── Readme.md
    ```
---

## 🔮 Future Improvements

* Dry Run mode
* Custom catergories
* Recursive Scanning
* GUI Interface

---

## 📌 Version

**v1.1** – Basic file organizer with core functionality & Dry Run functionality

---

## 📓 What I Learned

* How path works & how to use pathlib
* How to move & rename files using Shutil
* How to handle errors and debugging
* How to organize a project, which can be used for commercial purposes in the future

---

## 📜 License

This project is open-source and free to use.