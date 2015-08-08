import os, fnmatch

from datetime import datetime
from datetime import timedelta


def find_files(directory, pattern):
    """Return a generator containing all files matching pattern in
    a directory

    Arguments:
     * x: a number.
     * n: the exponent.

    Returns:
     * c: the number x to the power of n.

    """
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def count_files(directory,pattern):
    """Count files matching pattern in directory

    Arguments:
     * directory:
     * pattern: the exponent.

    Returns:
     * count: number of files matching pattern

    """
    files = find_files(directory,pattern)
    count = len( list(files) )
    return count


def check_dates(strings, date_format):
    """Make an array of dates based on directory listing of datestamped folders

    Arguments:
     * x: a number.
     * n: the exponent.

    Returns:
     * c: the number x to the power of n.

    """
    dates = []
    for i in strings:
        try:
            datetime.strptime(i, date_format)
            dates.append(i)
        except:
            print 'ho'
    return dates

def MODIS_dates(directory):
    date_format = "%Y.%m.%d"
    files = os.listdir(directory)
    dates = check_dates(files, date_format)
    return dates


def previous_day(date):
    """Make an array of dates based on directory listing of datestamped folders

    Arguments:
     * x: a number.
     * n: the exponent.

    Returns:
     * c: the number x to the power of n.

    """
    date_format = "%Y.%m.%d"
    today = datetime.strptime(date, date_format)
    yesterday = today - timedelta(days=1)
    return yesterday.strftime(date_format)


def date2index(dateArray,date):
    """Make an array of dates based on directory listing of datestamped folders

    Arguments:
     * x: a number.
     * n: the exponent.

    Returns:
     * c: the number x to the power of n.

    """

    dateList = dateArray.tolist()
    try:
        print date
        return dateList.index(date)
    except:
        date2index(dateArray, previous_day(date))


def date_clip(dataset, dateArray, start, stop):
    """Make an array of dates based on directory listing of datestamped folders

    Arguments:
     * x: a number.
     * n: the exponent.

    Returns:
     * c: the number x to the power of n.

    """
    s = date2index(dateArray, start)
    e = date2index(dateArray, stop)
    window = dataset[s:e]
    return window #might need to convert back to array with fill value

