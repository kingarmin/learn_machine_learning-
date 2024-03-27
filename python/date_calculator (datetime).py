from datetime import datetime
import math
def day_calculator(date_str):
    x=datetime.strptime(date_str,"%Y-%m-%d")
    y=datetime.now()
    return int(math.fabs((y-x).days))

print(day_calculator("2022-1-1"))