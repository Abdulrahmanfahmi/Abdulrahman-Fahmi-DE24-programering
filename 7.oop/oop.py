# oopar


# class Bil:
#     def __init__(self, name):
#         print("i am created!")
#     def Calculate_total_price(self, x, y):
#         return x * y 

# item1 = item()  
# item1.name = "bil"
# item1.price = 100
# item1.quantity = 6
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = item()
# item2.name = "laptop"
# item2.price = 1000
# item2.quantity = 2
# print(item2.calculate_total_price(item2.price, item2.quantity))

#.....................................................................................

# class sample():
#     pass
# s = sample()

# print(type(s))

#................................................................................................

# class dog():
#     #class objects atributes:
#     species = "däggdjur"
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
# frank = dog("Huskie", "frank")


# print(frank.breed)
# print(frank.name)
# print(frank.species)

#.......................................................................................................

# class Circle:
#     pi =3.14

#     # cirkeln initieras med en radie (standard 1)
#     def __init__(self, radius=1):
#         self.radius = radius

#     # metod för att beräkna arean (tänk på self)
#     def area(self):
#         return self.pi * self.radius**2
    
#     # metod för att sätta radien
#     def set_radius(self, radius):
#         return self.radius

#     # metod för arr hämta radien
#     def get_radius(self):
#         return self.radius
    
# c = Circle()
# c.set_radius(5)
# print("radien är", c.get_radius())
# print("area är", c.area())

#................................................................................

# class person:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.age = age
#         self.email = email
#     def __str__(self):
#         return f'{self.name} är {self.age} år gammal och har e-post {self.email}'
    
# p1 = person('abdulrahman', 'abdulrahman@gmail.com', 25)
# p2 = person('ali', 'ali@gmail.com', 28)
# print(p1)
# print(p2)

# p1.phone = '07012398'
# print(p1.phone)

# p2.phone = '07984824'
# print(p2.phone)

#..........................................................................................................


# class somthing:
#     def __init__(self, data:dict):
#         self.__dict__ = data
#     def __str__(self):
#         for key, value in self.__dict__.items():
#             str_rep += f'{key} = {value}'
#             return str_rep



# data_dict1 = {
#     'a' : 10,
#     'age' : 20,
#     'name' : 'one'

# }

# data_dict2 = {
#     'c' : 14,
#     'd' : 26,
#     'name' : 'two'
# }

# s1 = somthing(data_dict1)
# s2 = somthing(data_dict2)
# print(s1)
# print(s2)

#...............................................................................

# class person:
#     def __init__(self, fodelsedatum):
#         self.fodelsedatum = fodelsedatum
#         self.name = None
#         self.adress = None
#         self.telefonnumer = None
#     def set_name(self,name):
#         self.name = name
    

# p1 = person('2000-01-10 00.00.00, abdulrahman, södertälje gatan 32')

# print(p1.name)

#.................................................................................................

# oopar

# # uppgift 1
# class maträtt: 
#     def __init__(self, name, pris, typ, kalorier):
#         self.name = name
#         self.pris = pris
#         self.typ = typ
#         self.kalorier = kalorier 
#     def __str__(self):
#         return f'{self.name} {self.type} - {self.kalorier} kcal: {self.pris} kr'

# ratt1 = maträtt('vegansk pasta', 70, 'vegetarisk', 800)
# ratt2 = maträtt('köttbullar', 69, 'kött', 580)

# lista = [ratt1, ratt2]

# print('dagens lunchmeny:')
# for i in lista :
#     print(i)


#......................................................................................................

# # uppgift 2 

# class person:
#     def __init__(self, age, name, adress, postnummer, postort):
#         self.age = None
#         self.name = None
#         self.adress = None
#         self.postnummer = None
#         self.postort = None
# property
# def name(self):
#     return self._name

# name.setter
# def name(self, name):
#     self._name = name

# property
# def adress(self):
#     return self._adress

# name.setter
# def adress(self, adress):
#     self._adress = adress

# property
# def postnummer(self):
#     return self._postnummer

# name.setter
# def postnummer(self, postnummer):
#     self._postnummer = postnummer

# property
# def postort(self):
#     return self._postort

# name.setter
# def postort(self, postort):
#     self._postort = postort
# def chanfeadress(self, newadress, newpostnummer, newpostort):
#     self.adress = newadress
#     self.postnummer = newpostnummer
#     self.postort = newpostort

#     def showinfo(self):
#         return f'person: {self.name}, födelsedatum: {self.fodelsedatum}, adress: {self.adress}, postnummer: {self.postnummer}, postort: {self.postort}'


# person1 = person('2000-01-10')
# person2 = person('2001-02-11')

# person1.name = 'abdulrahman'
# person2.name = 'ali'

# person1.adress ('södertälje gatan 23' '12345' 'stockholm')
# person2.adress ('stockholm gatan 12' '12365' 'stockholm')

# print(person1.showinfo())
# print(person2.showinfo())

#.......................................................................................................................................................................

# class point: 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'point(x = {self.x} and y = {self.y}) '

# point1 = point(4, 7)
# point2 = point(9, 11)

# print(point1)
# print(point2)

#.......................................................................................

# class a:
#     def __init__(self, value):
#         print(f'A.__init__ has value = {value}')
#         self.value = value 

# class B(a):
#     def __init__(self, value):
#         print(f'B.__init__ has value = {value}')
#         self.value = value

# b = B(10)
# print(b.value)

#...............................................................................................
# class car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def start(self):
#         return(f'{self.brand} {self.model} has started.')
    
#     def stop(self):
#         return(f'{self.brand} {self.model} has stopped.')
    
    
# car = car('toyota', 'camry', 2020)
# print(car.start)

#.......................................................................................................


    

