import csv
from collections import defaultdict, Counter

DATA_FILE = '/data/dumps/flp/CourtListener/pacer/free-documents-report/out.csv'


def make_data(path=DATA_FILE):
    data = []
    with open(DATA_FILE, 'r') as f:
        c = csv.reader(f)
        for row in c:
            data.append(row)

    return data


def make_counters(data, granularity='year'):
    """Make counters for every court. 
    
    :param data: A list of csv rows (each row is also a list)
    :param granularity: either year or month. If 'year', then it counts by year.
    If 'month', it counts by month.
    :return: A dict of Counter objects keyed by court ID.
    """
    counters = defaultdict(Counter)
    if granularity == 'month':
        trim_date = lambda d: d.rsplit('-')[0]
    elif granularity == 'year':
        trim_date = lambda d: d.split('-', 1)[0]
    for row in data:
        counters[row[1]].update([trim_date(row[5])])

    return counters


def sum_all_counts(counters):
    """Sum up all the counter objects into a single one ignoring the courts.
    
    :param counters: A dict of name-counter pairs.
    :return: A counter object with counts for every year across all courts.
    """
    c = Counter()
    for court in counters.values():
        c.update(court)
    return c


def sum_all_dates(counters):
    """Sum up all the counters for each court across all dates.
    
    :param counters: A dict of name-counter pairs.
    :return: A counter object with counts for every court across all dates.
    """
    by_court = Counter()
    for court, counter in counters.items():
        by_court.update({court: sum(v for v in counter.values())})
    return by_court
