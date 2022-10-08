# import csv
# with open("new_employees.csv", "w", newline="") as csvfile:
#     file_writer = csv.writer(csvfile, delimiter=",")
#     # using file_write.write(<iterator_object>) to write a row
#     file_writer.writerow(["id", "first_name", "last_name"])
#     file_writer.writerow([1, "Huy", "Phan"])


import csv

with open("new_employees.csv", "w", newline="") as csvfile:
    header_lists = ["id", "first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=header_lists)

    writer.writeheader()
    writer.writerow({"id": 1, "first_name": "Huy", "last_name": "Phan"})
