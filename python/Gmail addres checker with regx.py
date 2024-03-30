import re
x=input()
if re.match(r'[a-zA-Z0-9\.\_]+@gmail.com',x):
    print("ok")