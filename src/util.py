import threading
import socket
from gi.repository import GLib

TRANSFER_START = "start"
TRANSFER_DATA = "data"
TRANSFER_COMPLETE = "end"
TRANSFER_FOLDER = "folder"
TRANSFER_ABORT = "aborted"
TRANSFER_REQUEST_PERM = "ask-permission"

RESPONSE_EXISTS = "exists"
RESPONSE_OK = "ok"
RESPONSE_DISKFULL = "diskfull"
RESPONSE_ERROR = "error"
RESPONSE_PERMISSION_GRANTED = "permission-granted"

# Used as a decorator to run things in the background
def _async(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread
    return wrapper

# Used as a decorator to run things in the main loop, from another thread
def _idle(func):
    def wrapper(*args, **kwargs):
        GLib.idle_add(func, *args, **kwargs)
    return wrapper

def getmyip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        ans = s.getsockname()[0]
        return ans
