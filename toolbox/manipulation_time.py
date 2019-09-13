import datetime as dt

h, m = "12h50".split("h")
minute = 60*int(h) + int(m)


def string_to_datetime(a):
    return dt.datetime.strptime(a, '%Y-%m-%d %H:%M')


def datetime_to_string(d):
    return dt.datetime.strftime(d, "%d %m %Y %H:%M:%S")


if __name__ == '__main__':
    print(string_to_datetime('2019-12-18 00:34'))
    print(datetime_to_string(string_to_datetime('2019-12-18 00:34')))
