# Loggine means-> To capture details,which are useful while debugging
# and show user details about execution of program

# Warning to users
# Information to the users
# Errors, critical errors to users

import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    # International logging to User
    LOGGER.info("This is Information Logs")
    LOGGER.warning("This is Warning Logs")
    LOGGER.error("This is Error Logs")
    LOGGER.critical("This is Critical Logs")