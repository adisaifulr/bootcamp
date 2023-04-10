# import datetime

# class person:
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def say_my_name(self):
#         print("hello my name is " + self.name)

# person_1 = person("john", 36)

# class Mathematic:

#     def add(self, a, b):
#         return a + b
    
#     def substraction(self, a, b):
#         return a - b
    
#     def multyplay(self, a, b):
#         return a * b


# math = Mathematic()

# print(math.add(1, 2))
# print(datetime.datetime.now())

#STUDY KASUS

class car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.mobil = 'mati'
        self.pintu = 'tertutup'


    def membuka_pintu(self):
        if self.pintu =='tertutup':
            print("berhasil membuka pintu")
            self.pintu = 'terbuka'
        else :
            print('pintu tidak bisa di tutup')
    def menutup_pintu(self):
        if self.pintu == 'terbuka':
            print("berhasil menutup pintu")
            self.pintu = 'tertutup'
        else:
            print('pintu sulit di tutup')
    
    def menyalakan_mobil(self):
        if self.mobil == 'menyala':
            print("berhasil menyalakan mobil")
            self.mobil = 'mati'
        else:
            print('mobil susah hidup')
    def mematikan_mobil(self):
        if self.mobil == 'mati':
            print("berhasil mematikan mobil")
            self.mobil = 'menyala'
        else:
            print('mobil susah mati')

car_1 = car('honda', 1992)
car_1.membuka_pintu()
car_1.membuka_pintu()
car_1.menutup_pintu()
car_1.menutup_pintu()
car_1.menyalakan_mobil()
car_1.menyalakan_mobil()
car_1.mematikan_mobil()
car_1.mematikan_mobil()