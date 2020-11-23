import os
from glob import glob
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# for other options see https://github.com/theskumar/python-dotenv

LOG_DIR = Path(os.getenv("LOG_DIR"))
AREA_DIR = Path(os.getenv("AREA_DIR"))


if __name__ == "__main__":
    region = 'region_1016'
    print(LOG_DIR.absolute())
    print(AREA_DIR.absolute())
    REGION_DIR = AREA_DIR / region
    RADARMASK_DIR = REGION_DIR / 'preprocessed' / 'radar_masks'
    print(RADARMASK_DIR.absolute())
    os.chdir(RADARMASK_DIR.absolute())
    track_list = glob('*.tif')
    tracks = []
    for track in track_list:
        tracks.append(int(track.split('.')[0].split('_')[2]))

    print(tracks)

