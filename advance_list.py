my_list = ["emp_no", "first_name", "last_name", "hire_date"]
where = {"first_name": "Huy", "last_name": "Phan"}

list_column_string = ",".join(my_list)


string = f"SELECT {list_column_string} FROM employees WHERE 1 = 1"
print(f"sql string: {string}")