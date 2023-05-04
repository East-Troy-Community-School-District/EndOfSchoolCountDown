'''
End of School Count Down
Pawelski
5/4/2023
Python II
'''

import tkinter
import datetime
import calendar

def count_weekdays(start, end):
    '''
    Counts the number of weekdays between the start and end dates.
    '''
    count = 0
    start_year = start.year
    end_year = end.year
    for year in range(start_year, end_year + 1):
        if year == start.year:
            start_month = start.month
        else:
            start_month = 1
            
        if year == end.year:
            end_month = end.month
        else:
            end_month = 12
        
        for month in range(start_month, end_month + 1):
            if month == start.month:
                start_day = start.day
            else:
                start_day = 1
                
            if month == end.month:
                last_day = end.day
            else:
                last_day = calendar.monthrange(year, month)[1]
            
            for day in range(start_day, last_day + 1):
                day_date = datetime.date(year, month, day)
                if 0 <= day_date.weekday() and day_date.weekday() <= 4:
                    count += 1
    return count

current_day = datetime.date.today()
senior_last_day = datetime.date(2023, 5, 26)
last_day = datetime.date(2023, 6, 8)
print(count_weekdays(current_day, last_day))
print(count_weekdays(current_day, senior_last_day))