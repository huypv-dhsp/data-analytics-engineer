# with open("<file_path>", encoding="<file_encoding>") as file:
#     file_content = file.read() # return entire text of file
#     # Do something with file_content
#
#
# f = open("<file_path>", encoding="<file_encoding>")
# file_content = f.read() # return entire text of file
# # Do something with file_content
# f.close()
#

import csv
with open("employees.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])