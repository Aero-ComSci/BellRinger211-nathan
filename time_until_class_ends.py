from datetime import datetime, time, timedelta

current_time = datetime.now()
class_end_time = datetime.combine(datetime.now(), time(14, 19, 0))

time_until_class_ends = class_end_time - current_time
print(f'There is {time_until_class_ends.seconds//60} minutes until class ends.')
