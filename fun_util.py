import os
import datetime

def check_system_info(cammand):
    print(os.system(cammand))

def check_date(cammand):            # defining a function
    print(os.system(cammand))

def date_time():
    return datetime.datetime.today()


# check_system_info("systeminfo")     # calling a function
# check_date("date")

today = date_time()
print(today)

