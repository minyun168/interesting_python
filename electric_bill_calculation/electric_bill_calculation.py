#! python2.7
# The program will caculate the electrict bill of everyone who live in the sharehouse whenever he started live in.


import datetime
dt_now = datetime.datetime.now()
print('現在の時刻は%s' %dt_now)
dt_before1 = datetime.datetime(year = 2021, month = 5, day = 29)
dt_before2 = datetime.datetime(year = 2021, month = 5, day = 20)
print('前の時刻は%s%s'   %(dt_before1,dt_before2))
delta1 = dt_now - dt_before1
delta2 = dt_now - dt_before2
print('時間差は%s' %delta1)

