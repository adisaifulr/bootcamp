# import datetime
# import math
import json
# import os

# x = datetime.datetime.now()
# print(x)

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2020, 5, 17)
# print(x)

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%D/%M/%Y"))

# ar_1 = [5, 78, 2, 0]

# assert(min(ar_1)) == 0
# assert(max(ar_1)) == 78

# assert(pow(5, 5)) == 3125

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("lorem ipsum")
#     except:
#         print("something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("something went wrong wen opening the file")

# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the 'try except' is finished")

# some JSON:
# x = { 
#          "name": "jhon", 
#          "age": 30, 
#          "city": "new york"
#      }

# # parse x:
# y = json.loads(x)

# # the resulg is a python dictionary:
# print(y["age"])

# x = { 
#         "name": "jhon", 
#          "age": 30, 
#         "city": "new york"
#      }

# # y = json.dumps(x)

# print(y)

# f = open ("demofile.txt", "x")

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("demofile2.txt", "a")
# f.write("now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# import os
# os.remove("demofile.txt")

# os.rmdir("demofile.txt")

f = open ('./json.txt')

