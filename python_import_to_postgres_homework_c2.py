import csv

import psycopg2

postgres_connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="postgres",
    database="data-analytics-engineer"
)

postgres_cursor = postgres_connection.cursor()

# INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
# VALUES
# (1, '1920-09-10', 'Huy', 'Phan', 'F', '1920-01-01'),
# (1, '1920-09-10', 'Huy', 'Phan', 'F', '1920-01-01')
value_texts = []
with open("employees.csv", newline="") as file:
    file_reader = csv.reader(file)
    for row in file_reader:
        # row_text = f"({row['emp_no']}, '{row['birth_date']}', '{row['first_name']}', '{row['last_name']}', '{row['gender']}', '{row['hire_date']}')"
        new_row = []
        for item in row:
            new_item = f"'{item}'"
            new_row.append(new_item)
        text = "(" + ",".join(new_row) + ")"
        value_texts.append(text)

# print(value_texts[1])
value_full_text = ",".join(value_texts[1:])
full_sql = f"""
     INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
    VALUES
    {value_full_text}
"""

postgres_cursor.execute(full_sql)
#
postgres_connection.commit()

postgres_cursor.close()
postgres_connection.close()
