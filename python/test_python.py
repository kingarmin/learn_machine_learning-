import json
from urllib.request import urlopen
from urllib.parse import quote
import time

def decoder(resp):
    decoded=''
    for line in resp :
        decoded=decoded+(line)
    return decoded
token='7151896681:AAGV3q3iRTKXnUIq_CDTePiQ4ztlEqRaA1k'
url='https://api.telegram.org/bot{}/'.format(token)
cmd='getme'
resp=urlopen(url + cmd)
line=decoder(resp)
line=json.load(line)
print(line)