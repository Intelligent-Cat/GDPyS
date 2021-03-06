import logging
from datetime import datetime

def FormattedTime(DateTimeObject = None):
    """Returns a formatted time string."""
    if DateTimeObject == None:
        DateTimeObject = datetime.now()
    return DateTimeObject.strftime("%H:%M:%S")

logging.basicConfig(format=f"[%(levelname)s] %(message)s ({FormattedTime()})")
logger = logging.getLogger("GDPyS") # init loggers