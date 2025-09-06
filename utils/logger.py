import os
import sys

from datetime import datetime as dt


class Logger(object):
    _instance = None
    _log = None

    def __new__(cls, filename=None, directory=None):
        """
        Logger builder, create a new instance.
        """
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(filename, directory)
        return cls._instance

    def _initialize(self, filename=None, directory=None):
        """
        Initialize the logging class with filename and direcory (if available).
        """
        self._log = None

        if not filename or not directory:
            # No file logging, fallback to console-only
            self.write("Logging", "Console-only mode (no file logging).")
            return

        # Validate types
        if not isinstance(filename, str) or not isinstance(directory, str):
            self.write("Logging", "Error: File name and directory must be strings.")
            return
        
        # Check for invalid characters in filename
        if any(c in r'\/:*?"<>|' for c in filename) or not filename.strip():
            self.write("Logging", "Error: File name contains invalid characters.")
            return

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Create a timestamped log file
        timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
        log_path = os.path.join(directory, f"{filename}_{timestamp}.log")
        try:
            self._log = open(log_path, "a", encoding="utf-8")
            self.write("Logging", f"Logging to {log_path}.")
        except Exception as e:
            self._log = None
            sys.stderr.write(f"[Logging - {dt.now().strftime('%H:%M:%S')}] "
                             f"Error opening log file: {e}\n")

    def write(self, tag, text):
        """
        Write a message to stdout and to the log file (if available).
        """
        curr_time = dt.now().strftime("%H:%M:%S")
        log_message = f"[{tag} - {curr_time}] {text}\n"

        # Always print to console
        sys.stdout.write(log_message)
        sys.stdout.flush()
        
        # Also write to log file if it is open
        if self._log is not None:
            self._log.write(log_message)
            self._log.flush()

    def flush(self):
        """
        Flush the log file buffer.
        """
        if self._log is not None:
            self._log.flush()

    def close(self):
        """
        Close the log file if it is open.
        """
        if self._log is not None:
            try:
                self._log.close()
            finally:
                self._log = None


# Helper function to get the singleton logger instance
def get_logging(filename: str = None, directory: str = None) -> Logger:
    if Logger._instance is None:
        Logger(filename, directory)
    return Logger._instance
