import logging
import sys
import threading
import traceback

import bpy

# Set up a logging handler to write to a file
log_file = "W:/blender_output.log"
handler = logging.FileHandler(log_file, mode="a")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)

# Redirect stdout and stderr to the logging module
import sys

sys.stdout = handler
sys.stderr = handler

# Lock to prevent duplicate log messages
log_lock = threading.Lock()


# Exception hook function to log uncaught exceptions
def log_uncaught_exception(exctype, value, tb):
    # Acquire the lock to prevent duplicate log messages
    log_lock.acquire()
    logging.error("Uncaught exception occurred:")
    logging.error("".join(traceback.format_exception(exctype, value, tb)))
    log_lock.release()


# Install the exception hook
sys.excepthook = log_uncaught_exception

# Example script code that generates an error
raise Exception("This is an error message")
