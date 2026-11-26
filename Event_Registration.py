from datetime import date

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = first_name.strip().title() + " " + last_name.strip().title()
section = section.strip().upper()
event_name = event_name.strip().title()

event_date = date(year, month, day)

print("Student Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date.strftime("%B %-d, %Y"))
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")

print("Registration record created successfully.")
