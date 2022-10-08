import datetime

current_datetime = datetime.datetime.utcnow()
print(f"Current datetime: {current_datetime}")

datetime_string = "2022-09-25 10:15:20"
datetime_obj = datetime.datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
print(f"Datetime object is: {datetime_obj}")

datetime_to_vn_format = datetime.datetime.strftime(datetime_obj, "%H:%M:%S %d/%m/%Y")
print(f"Datetime vn format: {datetime_to_vn_format}")

time_delta_1_days = datetime.timedelta(days=1)
new_datetime_obj = datetime_obj + time_delta_1_days
print(f"New datetime object is: {new_datetime_obj}")
