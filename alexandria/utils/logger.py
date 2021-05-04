"""Mock version of the logger for development purposes.

TODO: Design this to be production ready logger
"""
import datetime


class Logger:
    """Class logger for mock purposes.

    Latter should be replaced by production ready logger.
    """

    def __init__(self, modulename):
        """Initialise mock version of the logger for testing purposes."""
        self.modulename = modulename
        self.off = False

    def _log(self, level, msg, *args):
        if self.off:
            return
        if len(args) > 0:
            msg = msg % (args)
        print(f"{self.modulename} | {datetime.datetime.now()} | {level} |\t{msg}")

    def info(self, msg, *args):
        """Log info level messages into output stream."""
        self._log("INFO", msg, *args)

    def warning(self, msg, *args):
        """Log warning level messages into output stream."""
        self._log("WARNING", msg, *args)

    def error(self, msg, *args):
        """Log error level messages into output stream."""
        self._log("ERROR", msg, *args)

    def debug(self, msg, *args):
        """Log debug level messages into output stream."""
        self._log("DEBUG", msg, *args)


logger = Logger("alexandria")
