import datetime as dt
import re


class DateParser:
    PATTERNS = dict([
        [k, re.compile(f'(((-|\+|)\d+){k})')]
        for k in ['days', 'years', 'minutes']
    ])

    def __init__(self, datestr):
        self.tdkwargs = self.__find(datestr)
        self.td = dt.timedelta(**self.tdkwargs).total_seconds()
        self.ts = int(dt.datetime.now().timestamp() + self.td) * 1000

    def __find(self, datestr):
        tdkwargs = {}

        for kw, regex in self.PATTERNS.items():
            kwval = re.search(regex, datestr)

            if kwval:
                val = re.search(r'((-|\+|)\d+)', kwval.group())
                tdkwargs[kw] = int(val.group())

        return tdkwargs
