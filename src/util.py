import threading
import socket
import gettext

from gi.repository import GLib, Gtk

TRANSFER_SEND_DATA = "data"
TRANSFER_SEND_ABORT = "aborted"

TRANSFER_RECEIVE_STATUS_OK = "ok"
TRANSFER_RECEIVE_STATUS_ERROR = "error"

TRANSFER_REQUEST_PENDING = "pending"
TRANSFER_REQUEST_GRANTED = "granted"
TRANSFER_REQUEST_REFUSED = "refused"
TRANSFER_REQUEST_EXISTING = "existing"
TRANSFER_REQUEST_CANCELLED = "cancelled"

_ = gettext.gettext

class ProgressCallbackInfo():
    def __init__(self, progress=0, speed="", time_left="", finished=False,
                 sender_awaiting_approval=False, count=0,
                 transfer_request_refused=False, transfer_starting=False, transfer_cancelled=False):
        self.progress = progress
        self.speed = speed
        self.time_left = time_left
        self.finished = finished
        self.sender_awaiting_approval = sender_awaiting_approval
        self.count = count
        self.transfer_starting = transfer_starting
        self.transfer_cancelled = transfer_cancelled
        self.transfer_request_refused = transfer_request_refused

# A normal GtkFileChooserDialog only lets you pick folders OR files, not
# both in the same dialog.  This does.
def create_file_and_folder_picker(parent=None):
    window = Gtk.Dialog(title=_("Select file(s) to send"),
                        parent=None)
    window.add_buttons(_("Cancel"), Gtk.ResponseType.CANCEL,
                       _("Send"), Gtk.ResponseType.ACCEPT)

    chooser = Gtk.FileChooserWidget(action=Gtk.FileChooserAction.OPEN,
                                    select_multiple=True)
    chooser.connect("file-activated", lambda chooser: window.response(Gtk.ResponseType.ACCEPT))

    chooser.show_all()
    window.get_content_area().add(chooser)

    window.get_uris = chooser.get_uris
    return window

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

def relpath_from_uris(child_uri, base_uri):
    child_uri = GLib.uri_unescape_string(child_uri)
    base_uri = GLib.uri_unescape_string(base_uri)

    if child_uri.startswith(base_uri):
        return child_uri.replace(base_uri + "/", "")
    else:
        return None

# adapted from nemo-file-operations.c: format_time()
def format_time_span(seconds):
    if seconds < 0:
        seconds = 0

    if (seconds < 10):
        return _("A few seconds remaining")

    if (seconds < 60):
        return _("%d seconds remaining") % seconds

    if (seconds < 60 * 60):
        minutes = int(seconds / 60)
        return gettext.ngettext("%d minute", "%d minutes", minutes) % minutes

    hours = seconds / (60 * 60)

    if seconds < (60 * 60 * 4):
        minutes = int((seconds - hours * 60 * 60) / 60)

        h = gettext.ngettext ("%d hour", "%d hours", hours) % hours
        m = gettext.ngettext ("%d minute", "%d minutes", minutes) % minutes
        res = "%s, %s" % (h, m)
        return res;

    return gettext.ngettext("approximately %d hour", "approximately %d hours", hours) % hours
