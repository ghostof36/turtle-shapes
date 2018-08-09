#define our variables
current_time = int(input("Please enter the current time. "))
total_hours = int(input("How long would you like to sleep? "))
days = total_hours // 24
remaining_hours = total_hours % 24
hours = current_time + remaining_hours

if hours > 24:
    hours = hours - 24

print("Your alarm will ring in",days,"days and",remaining_hours,"hours, at",hours,"o clock.")