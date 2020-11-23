import os
from datetime import date, timedelta
from glob import glob
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# for other options see https://github.com/theskumar/python-dotenv

LOG_DIR = Path(os.getenv("LOG_DIR")).absolute()
AREA_DIR = Path(os.getenv("AREA_DIR")).absolute()


if __name__ == "__main__":
    region = 'region_1016'
    LOG_FILE = LOG_DIR / "{0}.log".format(region)
    REGION_DIR = AREA_DIR / region
    RADARMASK_DIR = REGION_DIR / 'preprocessed' / 'radar_masks'

    _now = date.today()
    _offset = timedelta(days=13)
    START_TIME = (_now - _offset).strftime('%Y-%m-%d')
    STOP_TIME = _now.strftime('%Y-%m-%d')

    os.chdir(RADARMASK_DIR)
    track_list = glob('*.tif')
    TRACKS = []
    for track in track_list:
        TRACKS.append(int(track.split('.')[0].split('_')[2]))

    TRACKS = str(TRACKS).replace(',', '').replace('[', '').replace(']', '')

    CMD = "satskred run {REGION_DIR} --starttime {START_TIME} --stoptime {STOP_TIME} --logfile {LOG_FILE} --tracks {TRACKS}".format(REGION_DIR=REGION_DIR, START_TIME=START_TIME, STOP_TIME=STOP_TIME, LOG_FILE=LOG_FILE, TRACKS=TRACKS)
    print(LOG_DIR)
    print(REGION_DIR)
    print(RADARMASK_DIR)
    print(TRACKS)
    print(CMD)

