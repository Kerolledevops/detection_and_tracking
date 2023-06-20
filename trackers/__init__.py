__version__ = '10.0.12'

from pathlib import Path

from trackers.strongsort.strong_sort import StrongSORT
from trackers.ocsort.ocsort import OCSort as OCSORT
from trackers.bytetrack.byte_tracker import BYTETracker
from trackers.botsort.bot_sort import BoTSORT
from trackers.deepocsort.ocsort import OCSort as DeepOCSORT
from trackers.deep.reid_multibackend import ReIDDetectMultiBackend

from trackers.multi_trackers import create_tracker, get_tracker_config


__all__ = '__version__',\
          'StrongSORT', 'OCSORT', 'BYTETracker', 'BoTSORT', 'DeepOCSORT'
