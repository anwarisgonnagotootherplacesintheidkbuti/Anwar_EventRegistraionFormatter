
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = first_name.strip().title() + " " + last_name.strip().title()

print("Student Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.strip().upper())
print("Event:", event_name.strip().title())
print("Year:", year)
print("Month:", month)
print("Day:", day)
