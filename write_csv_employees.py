import csv

with open('new_employees_with_dict.csv', 'w', newline='') as csvfile:
   header_lists = ["id", "first_name", "last_name"]
   writer = csv.DictWriter(csvfile, fieldnames=header_lists)

   writer.writeheader()
   writer.writerow({'id': 1, "first_name": "Huy", "last_name": "Phan"})

