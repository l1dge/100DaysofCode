from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    x = 20
    birthday = PYBITES_BORN + timedelta(days=100)
    for i in range(x):
        yield birthday
        birthday = birthday + timedelta(days=100)
