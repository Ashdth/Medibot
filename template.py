import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",   # this is the constructor file (oop) --- this is modular approach 
    "src/helper.py",     # this will contain all the functionality
    "src/prompt.py",     # this will contain chatbot prompt , " what will the assistant say"
    ".env",
    "setup.py",          # to install all the above packages
    "app.py",
    "research/trials.ipynb",   # all the coding in jupyter file
   " test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)               # so that it resolves the path issues in mac / linux / windows
    filedir, filename = os.path.split(filepath)    # in file directory will save "folder name"  & "file name " under filename


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")