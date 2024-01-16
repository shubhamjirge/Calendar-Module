"""
Title     : Calendar Module
Subdomain : Date and Time
Domain    : Python
Problem   : https://www.hackerrank.com/challenges/calendar-module/problem
"""
import calendar
import datetime

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())
