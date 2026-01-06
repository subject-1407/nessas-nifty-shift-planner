#!/usr/bin/env python3
import csv
import argparse

# Constants
days_of_week = ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
shifts = ['Morning', 'Afternoon']
required_shifts_per_employee = 3

# Minimum employees needed for each shift on each day
employees_per_shift = {
    'Friday': {'Morning': 2, 'Afternoon': 2},
    'Saturday': {'Morning': 3, 'Afternoon': 3},
    'Sunday': {'Morning': 4, 'Afternoon': 4},
    'Monday': {'Morning': 4, 'Afternoon': 4},
    'Tuesday': {'Morning': 5, 'Afternoon': 5},
    'Wednesday': {'Morning': 5, 'Afternoon': 5},
    'Thursday': {'Morning': 5, 'Afternoon': 5}
}

# Load employees from CSV
def load_employees(csv_file):
    employees = {}
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Name']
            days = row['Days'].split(';')
            friends = row['Friends'].split(';') if row['Friends'] else []
            employees[name] = {'days': days, 'friends': friends}
    return employees

# Scheduler logic
def create_schedule(employees):
    schedule = {day: {shift: [] for shift in shifts} for day in days_of_week}
    remaining_shifts = {emp: required_shifts_per_employee for emp in employees}

    sorted_employees = [employee[0] for employee in
                        sorted(employees.items(), key=lambda x: (len(x[1]['days']), -len(x[1]['friends'])))]

    for emp in sorted_employees:
        for day in employees[emp]['days']:
            for shift in shifts:
                if remaining_shifts[emp] == 0:
                    break
                required = employees_per_shift[day][shift]
                available_employees = [e for e in sorted_employees if day in employees[e]['days'] and remaining_shifts[e] > 0]
                assigned_employees = schedule[day][shift]
                group = [emp] + [pref for pref in employees[emp]['friends'] if pref in available_employees]
                if required - len(assigned_employees) >= len(group):
                    for e in group:
                        if e not in assigned_employees:
                            schedule[day][shift].append(e)
                            remaining_shifts[e] -= 1
    return schedule, remaining_shifts

# Print schedule
def print_schedule(schedule, remaining_shifts):
    print("Schedule:")
    for day, shifts_dict in schedule.items():
        print(f"{day}:")
        for shift, workers in shifts_dict.items():
            print(f"  {shift}: {', '.join(workers) if workers else 'No one assigned'}")

    print("\nRemaining Shifts per Employee:")
    for e, remaining in remaining_shifts.items():
        if remaining > 0:
            print(f"  {e}: {remaining} remaining shift{'s' if remaining > 1 else ''}")

# CLI entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Shift planner for volunteer schedules")
    parser.add_argument('employee_csv', help="Path to CSV file with employees, availability, and friends")
    args = parser.parse_args()

    employees = load_employees(args.employee_csv)
    schedule, remaining_shifts = create_schedule(employees)
    print_schedule(schedule, remaining_shifts)

