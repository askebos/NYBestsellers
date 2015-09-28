# source: http://stackoverflow.com/questions/10688006/generate-a-list-of-datetimes-between-an-interval-in-python
from datetime import date, datetime, timedelta

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

datesList = []

# Date is in format year, month, day. Change here for alternative dates. With 9 and 8 don't use a 0 in front for months
for result in perdelta(date(2008, 01, 01), date(2015, 12, 31), timedelta(days=7)):
    datesList.append(result)
