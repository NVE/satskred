import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# for other options see https://github.com/theskumar/python-dotenv

TARGET_DIR = Path(os.getenv("TARGET_DIR"))


if __name__ == "__main__":
    print(TARGET_DIR.absolute())
