import datetime
dt_now = datetime.datetime.now()
print('現在の時刻は%s' %dt_now)
dt_before = datetime.datetime(year = 2021, month = 5, day = 29)
print('前の時刻は%s' %dt_before)
delta = dt_now - dt_before
