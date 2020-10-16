#Exercise 1

from datetime import datetime,timedelta

now = datetime.now()

for d in range(10):
    add_date = now + timedelta(days=14)
    now = add_date
    print(add_date.strftime("%Y-%m-%d"))









