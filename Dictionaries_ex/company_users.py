employees_records = {}

while True:
    user_input = input().split(" -> ")

    if user_input[0] == 'End':
        break

    company_name = user_input[0]
    employee_id = user_input[1]

    if company_name not in employees_records:
        employees_records[company_name] = []
    if employee_id not in employees_records[company_name]:
        employees_records[company_name].append(employee_id)

for company_name, list_of_employees in employees_records.items():
    print(company_name)
    for employee_id in list_of_employees:
        print(f"-- {employee_id}")
