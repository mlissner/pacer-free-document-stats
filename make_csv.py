"""Code to be run on the server. Kept here for easy reference.

Use the %ed command to get a vi interface into iPython, and paste this in.
"""

import csv
from cl.scrapers.models import PACERFreeDocumentRow


def make_csv():
    with open('/tmp/out.csv', 'w') as f:
        w = csv.writer(f)
        items = PACERFreeDocumentRow.objects.values_list()
        for row in items:
            try:
                w.writerow(row)
            except UnicodeEncodeError:
                pass
    del items  # reclaim memory
