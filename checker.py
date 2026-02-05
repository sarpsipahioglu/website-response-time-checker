from urllib3 import encode_multipart_formdata
from itertools import starmap
import requests
import time

start= time.time()
responses = requests.get("https://www.google.com")
end = time.time()
enlapsed = end - start
print("status:", responses.status_code)
print("time ms:", enlapsed*1000)
