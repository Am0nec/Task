from datetime import datetime, timedelta
def date_in_future(day):
    now = datetime.now()
    date_now = now.strftime("%d-%m-%Y %H:%M:%S")

    if not isinstance(day, int):
        return date_now
    else:
        new_date = now + timedelta(days = day)
    return new_date.strftime("%d-%m-%Y %H:%M:%S")


day_future = 9
x = date_in_future(day_future)
print(x)
