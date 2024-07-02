name = input("Employee's name: ").strip().title()
hourly_wage = input("Hourly wage: ")
hours_worked = input("Hours worked: ")

earnings = float(hourly_wage) * float(hours_worked)

print(f"{name} earned: {earnings}€")
