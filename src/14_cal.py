"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import datetime


def printCalendar(*args):
    isValidArgs = validate(*args)
    argsList = list(args[1:])
    now = datetime.datetime.now()
    if (isValidArgs):
        if len(argsList) == 0:
            print(calendar.month(now.year, now.month))
        elif len(argsList) == 1:
            print(calendar.month(now.year, int(argsList[0])))
        elif len(argsList) == 2:
            print(calendar.month(int(argsList[1]), int(argsList[0])))
    else:
        print("Invalid input. Please enter the correct input.")


def validate(*args):
    argsList = list(args[1:])
    try:
        if len(argsList) == 2:
            if (int(argsList[0]) > 0) and (int(argsList[0]) < int(13))
            and isinstance(int(argsList[0]), int):
                if int(argsList[1]) > 0 and isinstance(int(argsList[1]), int):
                    return True
                else:
                    return False
            else:
                return False
        elif len(argsList) == 1:
            if int(argsList[0]) > 0 and int(argsList[0]) < int(13)
            and isinstance(int(argsList[0]), int):
                return True
            else:
                return False
        elif len(argsList) == 0:
            return True
    except TypeError:
        return False


printCalendar(*sys.argv)
