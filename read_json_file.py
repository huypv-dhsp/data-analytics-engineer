import json
json_object = {"id": 1, "first_name": "Huy", "last_name": "Phan"}
with open("new_employee_object.json", "w") as jsonfile:
    jsonfile.write(json.dumps(json_object))
