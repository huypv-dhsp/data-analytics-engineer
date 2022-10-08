import csv
import datetime

with open("employees.csv", newline="") as file:
    dict_reader = csv.DictReader(file)

    count = 0

    for row in dict_reader:
        if count <= 10:
            birth_date = datetime.datetime.strptime(row['birth_date'], "%Y-%m-%d")
            age = datetime.datetime.now().year - birth_date.year
            print(f"{row['first_name']} - {row['last_name']} - {age}")
            count += 1
        else:
            break
