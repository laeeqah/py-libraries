#Task 2

student_name= input("Student name: ")
student_surname= input("Surname: ")

mark_1= int(input("Test mark 1: "))
mark_2= int(input("Test mark 2: "))
mark_3=int(input("Test mark 3: "))

average = (mark_1 + mark_2 + mark_3) / 3

if average >= 50:
    print("Pass!")

elif average < 50:
    print("Failed")

print(round(average),"%")

from datetime import datetime, timedelta
now = datetime.now()

for d in range(10):
    ten_date = now + timedelta(days=14)
    now = ten_date
    print(ten_date.strftime("%Y-%m-%d"))

