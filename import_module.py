import datetime
datetime_object = datetime.datetime.now()

datetime_str = datetime.datetime.strftime(datetime_object, "%m/%d/%Y %H::%M::%S")
print(datetime_str)