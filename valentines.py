import datetime
def is_valentine():
    today = datetime.date.today()
    return(today.month == 2 and today.day == 14)

if _name_==_"_main_":

 if is_valentine():
    print("Happy Valentine's Day!")
else:
    print("it's not valentine's Day yet.")