import leather


def make_chart(counter, name):
    """Make SVG charts and save them in /tmp.
    
    :param counter: A counter object with counts for every year/month.
    :param name: The name of the dataset to be used for the filename and the 
    legend.
    :return: None, however, a file is created in /tmp named `name`.svg 
    """
    chart = leather.Chart(name)
    chart.add_bars(sorted(counter.items(), key=lambda t: t[0]), x=1, y=0)
    chart.to_svg('/tmp/%s.svg' % name.lower())


def make_all_charts(counters):
    """Make many charts using a dict of counters.
    
    The key to the dict is used as the name, and the value (a counter object) is
    used as the data.
    
    :param counters: A dict of name-counter pairs.
    :return: None, however numerous charts should be created in /tmp.
    """
    for name, counter in counters.items():
        make_chart(counter, name)
