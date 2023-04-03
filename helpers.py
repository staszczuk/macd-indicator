from datetime import datetime


def str_to_datetime(val):
    return datetime.strptime(val, "%m/%d/%Y").date()


def price_to_float(val):
    return float(val[1:])
