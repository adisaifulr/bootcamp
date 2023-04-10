import requests
from pprint import pprint
# import time
# import math


# def calculate_time(func):

#     def inner1(*args, **kwargs):

#         begin = time.time()

#         func(*args, **kwargs)

#         end = time.time()
#         print("total time taken in : ", func.__name__, end - begin)

#     return inner1
    
# @calculate_time
# def factorial(num):

#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

r = requests.get('https://jsonplaceholder.tyicode.com/todos/1')
data = r.json()
print(data)

post = {
    'body' : "lorem ipsum",
    'title': "title",
    'userId': 5
}

req = requests.post('https://jsonplaceholder.tyicode.com/posts', post)
print(req.status_code)