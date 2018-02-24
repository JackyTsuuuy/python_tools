import requests
import sys

url = sys.argv[1]
print('Your url is :\n',url)
r = requests.options(url)
print('Return headers:\n%s'%r.headers)