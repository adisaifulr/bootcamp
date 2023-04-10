#LIST
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

#ACCES LIST ITEMS NEGATIVE
# thistlist = ("apple","banana","chery")
# if "apple" in thistlist
# print("yes, is apple delicious")

# thistlist = ("apple","banana","chery")
# print(thistlist[-1])

#RANGE OF INDEX
# thistlist = ["apple","banana","chery","orange","kiwi","mango"]
# print(thistlist[2:5])

#RANGE OF INDEX NEGATIVE
# thistlist = ["apple","banana","chery","orange","kiwi","mango"]
# print(thistlist[-4:-2])

#ALLOW DUPLICATES
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

#LIST LENGTH
# thislist =["apple", "banana", "cherry"]
# print(len(thislist))

#LIST ITEMS - DATA TYPES
# list1 = ["apple", "banana", "cherry"]
# list2 = [1 ,5, 7, 9, 3]
# list3 = [True, False, False]

#CHANGE ITEM VALUE
# thistlist = ["apple","banana","chery","orange","kiwi","mango"]
# thistlist[1:3] = ["blackcurant", "watermelon"]
# print(thistlist)

#insert items
# thislist = ["apple","banana","chery"]
# thislist.insert(1, "blackcurant")
# print(thislist)

#APPEND ITEMS
# thistlist = ['apple', 'banana']
# thistlist.append('mango')
# print(thistlist)

#EXTEND LIST
# thistlist = ["apple","banana","chery"]
# tropical = ["mango", "papaya"]
# thistlist.extend(tropical)
# print(thistlist)

# thistlist.extends(thistlist2)
# print(thistlist2)

#REMOVE SPECIFIED ITEM
# thistlist = ['apple', 'banana', 'cherry']
# thistlist.remove('banana')
# print(thistlist)

#REMOVE SPECIFIED INDEX
# thistlist = ['apple', 'banana', 'cherry']
# thistlist.pop(1)
# print(thistlist)

#LOOP THROUGH A LIST
# thistlist = ['apple', 'banana', 'cherry']
# for x in thistlist:
#     print(x)

#LOOP THROUGH THE INDEX NUMBERS
# thistlist = ['apple', 'banana', 'cherry']
# for x in range(len(thistlist)) :
#     print(thistlist)

#CLEAR THE LIST
# thistlist = ['apple', 'banana', 'cherry']
# thistlist.clear()
# print(thistlist)

#USING A WHILE LOOP 
# thistlist = ['apple', 'banana', 'cherry']
# i = 0 
# while i < len(thistlist):
#     print(thistlist[i])
#     i = i + 1

#LOOPING USING LIST COMPREHESION
# thistlist = ['apple', 'banana', 'cherry']
# [print(x) for x in thistlist]

#LIST COMPREHENSION 1
# fruits = ["apple","banana","chery","orange","kiwi","mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

#LIST COMPREHENSION 2
# fruits = ["apple","banana","chery","orange","kiwi","mango"]
# newlist = [x for x in fruits if "a" in x]

# print(newlist)

#SORT LIST ALPANUMERICALLY
# fruits = ["apple","banana","chery","orange","kiwi","mango"]
# fruits.sort()
# print(fruits)

# fruits = [23, 45, 12, 89, 20]
# fruits.sort()
# print(fruits)

#SORT DESCENDING 
# fruits = ["apple","banana","chery","orange","kiwi","mango"]
# fruits.sort(reverse = True)
# print(fruits)

# fruits = [23, 45, 12, 89, 20]
# fruits.sort(reverse= True)
# print(fruits)

#COSTUMIZE SORT FUNCTION
# def myfunc(n):
#     return abs(n - 50)

# thislist = [100, 50 , 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

#python loop list

#1
# thistlist = ["apple","banana","chery"]

# assert(thistlist.pop(1)) == ['apple', 'mango']

# assert(thistlist.append('kiwi')) == ['apple', 'mango', 'kiwi']
 
# new_list = ['apple', 'apple', 'apple', 'apple', 'mango', 'kiwi', 'apple', 'apple', 'apple', 'apple']

# assert(new_list[4:6]) == ['mango', 'kiwi']

# new_list = ['apple', 'apple', 'apple', 'apple', 'mango', 'kiwi', 'apple', 'apple', 'mango', 'kiwi', 'apple', 'apple']

# assert(x for x in new_list if x != 'apple') == ['mango', 'kiwi', 'mango', 'kiwi']

#2
# list1 = [1, 4, 5, 6, 2,4]
# assert(x for x in list1 if x != 4) == [1, 5, 6, 2]

# assert(x for x in list1 if x == 4) == [4, 4]

#3
# list1 = [1, 4, 5, 6, 2,4]
# list2 = list.copy()
# list2.pop()

# print(list1, list2)

# list3 = [1, 4, 5, 2]

# list3 

#unpacking using a
# fruits = ("apple", "banana", "chery", "stroberry", "rasberry")

# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

#2
# print(cars['brand'])

# print(cars.keys())
# for key in cars.keys():
#     print(cars[key])

# cars = {
#     'brand' : 'honda',
#     'product' :'civic'
# }    

# assert(list(cars.keys())[1]) == 'product'

# print(cars.values())

# print(cars.get('year'.none))
# print('tidak akan dijalankan')

#aargumen
# def my_function(fname):
#     print(fname +"Refsnes")
# my_function("emil")
# my_function("tobias")

#
# def my_function_2(child1, child2):
#     print(child2)

# my_function_2(child2="emil", child1="tobias")

#
# def multiply_by_two(a):
#     return 2 * a 

# assert(multiply_by_two(3)) == 6
    
# def multiplay_by_x(a, b=2):
#     "if x not passed, then define the default value to 2"
#     return a * b

# assert(multiplay_by_x(3)) == 6
# assert(multiplay_by_x(3, 1)) == 3

# user_input = input("input dikali dengan 2:")
# print(multiply_by_two(int(user_input)))

#study kasus
# how_many_input = input(' enter the number of student in your class : ')
# students = []

# def totalgrades(grades):
#     grade = 0 
#     grades = grades.split(",")
#     for i in grades:
#         grade += float(i)
#     grade = grade/len(grades)
#     return grade

# for i in range(int(how_many_input)):
#     name = input('enter the name of student : ')
#     grades = input('enter the grades of student (coma-separated) : ')
#     students.append(
#         {
#             'nama' : name,
#             'grade' : grades,
#             'averange_grade' : totalgrades(grades)
#         }
#     )

# print()
# print("averange grades:")
# for z in students:
#     print(z["nama"], ":", z["averange_grade"])
