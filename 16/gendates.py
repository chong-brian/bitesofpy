from datetime import datetime

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    dates = []
    working_date = PYBITES_BORN
    while working_date.year < 2019:
        for x in range(1, 101):
            try:
                working_date = datetime(year=working_date.year, month=working_date.month, day=working_date.day + 1)
                if working_date.month == PYBITES_BORN.month and working_date.day == PYBITES_BORN.day:
                    dates.append(working_date)
                    continue
                # print(working_date)
            except ValueError:
                try:
                    working_date = datetime(year=working_date.year, month=working_date.month + 1, day=1)
                    # print(working_date)
                except ValueError:
                    working_date = datetime(year=working_date.year + 1, month=1, day=1)
                    # print(working_date)
        dates.append(working_date)
    return dates

# print(gen_special_pybites_dates())

""" OFFICIAL SOLUTION

def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)
"""