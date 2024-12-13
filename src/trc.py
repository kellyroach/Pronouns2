################################################################
#
#    trc.py
#
################################################################

"""Homebrew trace package produces output like output in 1980 M.S. thesis"""

from globals import *

_trc_writing: int
"""trc_write called since last trc_end()."""
# -1 = outside \vbox{\obeylines{\texttt{...}}}
# nonnegative = inside

_trc_level: int
"""Tracks the current indentation level."""

def trc(enable: bool) -> None:
    """Enables or disables function call tracing globally.

    Args:
        enable (bool): If True, enables tracing; if False, disables it
    """
    Manager.set_state(trace=enable)

def trc_reset() -> None:
    """Reset the trc package."""
    global _trc_writing, _trc_level
    _trc_writing = -1
    _trc_level = 0

def trc_begin() -> None:
    """Begins trace output for LaTeX streams by opening formatting blocks."""
    global _trc_writing
    if (_trc_writing >= 37) and (Manager.file_type == FileType.TEX):
        # Limit 37 empirically derived by examining successive test_trace.pdf's
        # until the most problematic page containing sentence (11.29) is
        # optimally produced.  The improvement which allows LaTeX to page
        # break instead of running a long trace off the bottom of the page
        # has a few noticeable occasional small white space hiccups when doing
        # pure tracing, as in test_trace.pdf .  However, these are liveable.
        # Besides, we rarely do pure tracing.
        trc_end()
    if _trc_writing < 0:
        Manager.write("\n")
        if Manager.file_type == FileType.TEX:
            Manager.write("\\bigbreak\n")
            Manager.write("\\vbox{\\obeylines{\\texttt{\n")
        _trc_writing = 0

def trc_end() -> None:
    """Ends trace output for LaTeX streams by closing formatting blocks."""
    global _trc_writing
    if _trc_writing >= 0:
        if Manager.file_type == FileType.TEX:
            Manager.write("}}}\n")
            Manager.write("\\bigbreak\n")
        _trc_writing = -1

def trc_enter(message: str) -> None:
    """Prints a message with increased indentation when entering a function, if tracing is enabled.

    Args:
        message (str): Function entry message to print.
    """
    global _trc_level
    trc_write(message)
    _trc_level += 1

def trc_exit(message: str) -> None:
    """Prints a message with decreased indentation when exiting a function, if tracing is enabled.

    Args:
        message (str): Function exit message to print.
    """
    global _trc_level
    _trc_level -= 1
    trc_write(message)

def trc_write(message: str) -> None:
    """Prints a message at current indentation level, if tracing is enabled.

    Args:
        message (str): Message to print at current indentation.
    """
    global _trc_level, _trc_writing
    if Manager.trace and message:
        trc_begin()
        if Manager.file_type == FileType.TEX:
            space = "~"
            message = message.replace("@", "\\symbol{95}")
        else:
            space = " "
            message = message.replace("@", "_").replace("~", " ")
        Manager.write(space * (4 * _trc_level) + message + "\n")
        _trc_writing += 1

trc_reset()
