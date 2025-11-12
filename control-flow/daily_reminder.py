task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        level = "high"
    case "medium":
        level = "medium"
    case "low":
        level = "low"
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
        level = None

if level:
    if time_bound in ("yes", "y"):
        print(f"Reminder: '{task}' is a {level} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {level} priority task. Consider completing it when you have free time.")