"""
This module provides functionality to generate and print an ASCII calendar for the current month.
"""

import calendar
from datetime import datetime


def generate_current_month_calendar():
    """
    Generate the ASCII calendar for the current month.

    Returns:
        str: ASCII representation of the current month's calendar.
    """
    current_month = datetime.now().month
    current_year = datetime.now().year
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    return cal.formatmonth(current_year, current_month)


def print_calendar(ascii_calendar):
    """
    Print the given ASCII calendar.

    Args:
        ascii_calendar (str): ASCII representation of a calendar.
    """
    print(ascii_calendar)


if __name__ == "__main__":
    calendar_string = generate_current_month_calendar()
    print_calendar(calendar_string)
