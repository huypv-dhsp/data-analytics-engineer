
import psycopg2
import psycopg2.extras

# postgres_connection_string = "postgresql://postgres:postgres@localhost:5432/data-analytics-engineer"

postgres_connection = psycopg2.connect(
    user="postgres",
    host="localhost",
    port="5432",
    password="postgres",
    database="data-analytics-engineer"
)

postgres_cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
with open("load_employees.sql") as file:
    sql_text = file.read()
# employees_rows = f"""
#     SELECT * FROM employees
# """

postgres_cursor.execute(sql_text)
#
# for row in postgres_cursor.fetchall():
#     print(dict(row))

# connect to PostgreSQL
# insert_data_sql = """
#    INSERT INTO employees
#    (emp_no, birth_date, first_name, last_name, gender, hire_date)
#    VALUES
#    (10023, "1953-09-29", "Bojan", "Montemayor", "F", "1989-12-17")
# """
#
# postgres_cursor.execute(insert_data_sql)
postgres_connection.commit()

postgres_cursor.close()
postgres_connection.close()
