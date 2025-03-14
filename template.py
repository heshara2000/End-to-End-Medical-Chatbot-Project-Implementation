import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files =[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file : {filename}")

        if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
            with open(filepath, 'w') as f:
                logging.info(f"empty File created: {filename}")
        else:
            logging.info({filename} + "alreay exists")


