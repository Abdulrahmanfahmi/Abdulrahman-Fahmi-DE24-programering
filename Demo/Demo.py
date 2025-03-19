# print(5+2)

# def adder(num1, num2):
#     return num1 + num2

# print(adder(5,2))
# print(adder(6,7))


# print(2*99)

#.....................................................

# x = 'hello'

# print(len(x))

#.........................................................

# func

# def length(x):
#     return length(x)

# # rör ej

# print(length('hello'))[5]

# print(x.upper())
# print(x.lower())
# print(x.split())
# print(x.split('l'))

#...........................................................................

# namn = 'Alice'
# ålder = 23

# print('Alice')
# print(23)

# ålder = ålder + 1
# ålder += 1

# print('uppdatera ålder:',ålder)

#.............................................................................................

# []

# a = 'hello world'

# print(a[0])
# print(a[1])
# print(a[1:])
# print(a[:3])
# print(a[:])
# print(a[-1])
# print(a[::2])

#...........................................................................................

# a = 'hello world'

# a[0] = 'H'

# a = a +'concatenate me'
# print(a)


#.............................................................................................

# name = 'alice'
# age = 25

# age = age + 1
# print(f'my name is {name}, and my age is {age} years old')

#..................................................................................................................

# if 1 < 2:
#     print('yes')
# else:
#     print('No')


#...............................................................................................................

# def campereror(num1, num2):
#     if num1 < num2:
#         return 'Yes'
#     else: return 'No'

# print(campereror[5,9])
# print(campereror[7,8])

#...............................................................................................................

# if 1== 2:
#     print('first')
# elif 3 == 3:
#     print('middle')
# else:
#     print('last')

#..................................................................................................................

# name = 'lisa'
# age = 55
# if age == 55 and name == 'lisa':
#     print('kom in')
# elif age == 55 or name == 'lisa':
#     print('något av kräven uppfylls ej')
# else:
#     print('inga krav uppfylls')

#...........................................................................................

# for i in range(100):
#     print(i)

# for i in range(2, 18, 3):
#     print(i)

#................................................................................................

# lista = [1, True, 'string', 2.3]

# for i in lista:
#     print(i)


# def lista(lista):
#     mylist = []
#     for i in lista:
#         mylist.append(i)
#         return mylist

# print(lister(1, True None, 'string', 2.6))


#.........................................................................................................

# for i in range(5):
#     if i == 4:
#         break
#     print(i)
# else:
#     print('loopen avslutad')


#.....................................................................................................

# guess = input('vilken är den populära pizza?/n')

# while guess != 'ost':
#     print('fel det är inte rätt topping.')
#     guess = input('vilken är den mest populära pizza?/n')

# print('rätt svar ost är den mest populära toppingen')

#............................................................................................................

# def gissa_topping(guess):
#     while guess!= 'ost':
#         return 'fel det är inte rätt toppingen.'
    
#     return 'rätt svar ost är den mest populära toppingen.'


# test1 = gissa_topping('skinka') ['fel det är inte rätt toppingen']
# print(test1)

# test2 = gissa_topping('ost') ['rätt svar ost är den mest populära toppingen']
# print(test2)


#......................................................................................................................

# lista = [1, 2, 3, 4, 5]
# lista.append('append me')
# lista.pop(0)
# print(lista)
# lista.remove('append me')
# print(lista)

#................................................................................................................

# my_dictionary = {
#     1 : 'value one',
#     2 : 'value two',
#     3 : 'value three'
# }

# # print(my_dictionary[2])

# # print(my_dictionary[3].upper())


# new_dict = {}

# new_dict['animal'] = 'cat'
# print(new_dict)

#.......................................................................................................................

# def createDict(new_dictionary, animal, typeanimal):
#     new_dictionary['animal'] = animal
#     return new_dictionary


# print(createDict({},'animal', 'cat'))

#......................................................................................................................

# dictionary = {
#     'keys1' : 1,
#     'key2' : 2,
#     'key3' : 3
# }

# print(dictionary.keys())

# print(dictionary.values())

# print(dictionary.items())

# for key in value in dictionary.items():
#     f('{key} : {value}')
#...............................................................................................

# myvarible  = 'my value'
# print(myvarible)


#............................................................
# loopar
# for i in range(100000):
#     print(i)


#...............................................................................
# string

# mystring = 'hello world'
# mystringtwo = 'my name is Abdulrahman'
# mystringthree = ', i am 25 years old and my hobby is to go to the gym'

# print(f'{mystring} {mystringtwo}{mystringthree}')

# mystringfour = '''first 
# second
# third
# fourth'''

# mystringfive = ''''hi
# hello
# world
# how are you?'''

# print(f'{mystringfour} {mystringfive}')


# indexing ( Acces single Item )

# mystring = 'i love python'
# print(mystring[0])
# print(mystring[9])
# print(mystring[-6])
# print( mystring[-1])
# print( mystring[::2])

# slicing ( Acces multiple Items )

# print(mystring[8:11]) # om jag skriver (mystring[8:11] då jag kommer få (yth))   yth
# print(mystring[3:5]) # om jag skriver (mystring[3:5] då jag kommer få (ov)
# print(mystring[:10]) # om jag skriver (mystring[:10]) då jag kommer få (I Love Pyt)
# print(mystring[5:]) # om jag skriver (mystring[5:] då jag kommer få (e python))
# print(mystring[:]) # om jag skriver (mystring[:] då jag kommer få ( I love python) hela meningen )
# print(mystring[0::1]) # om jag skriver (mystring[0::1] då jag kommmer få (I love python) hela meningen samma som förra här)
# print(mystring[::1]) # om jag skriver (mystring[::1] då kommer jag få som de senaste (I love python) alltså hela meningen igen)

# a = 'i love python'
# b = '    i love python   '
# print(len(a))
# print(len(b))

# a = 'i love python'
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# title()

# b = 'i love 2d graphics system'
# print(b.title())


# # capitalize()

# b = 'i love 2d graphics system'
# print(b.capitalize())

#zfill()
# c, d, e, k = '12', '33', '44', '455'
# print(c.zfill(5))
# print(c)
# print(d)
# print(e)
# print(k)


# upper()

# g = 'abdulrahman'
# print(g.upper())

# lower()

# g = 'abdulrahman'
# print(g.lower())

# split()  rsplit()

# a = 'i love python and php'
# print(a.split())

# a = 'i love python and-php'
# print(a.split('-'))

# c = 'i love python and php'
# print(c.rsplit('-', 2))

# d = 'abdulrahman '
# print(d.strip())

# #upper()

# e = 'abdulrahman'
# print(e.upper())

# # lower()
# e = 'abdulrahman'
# print(e.lower())

# c = 'i love you-and-i-am-a-student'
# print(c.rsplit())

# replace()

# a = 'i love python'
# print(a.replace('python','abdulrahman'))


#..............................................................................................

# tuple syntax and type test
# mytuple1 = ('abdulrahman', '23','fahmi is the last name')
# print(mytuple1)
# print(type(mytuple1))

# tuple indexing 
# mytuple3 = (1, 2, 3, 4, 5, 6,)
# print(mytuple3[4])
# print(mytuple3[-1])
# print(mytuple3[-3])
# print(mytuple3[:5])

# tuple assign values
# mytuple4 = (1, 3, 4, 5, 7, 8)


#...............................................................................................................

# while loop

# name = input('enter your name:')

# while name == 'abdulrahman':
#     print('you did not enter your name')
#     name = input('enter your name:')

# print('hello {abdulrahman}')

# food = input('enter a food you like (q to quite):')

# while food == 'q':
#     print(f'you like {food}')
#     food = input('enter another food you like (q to quite):')

# print('hejdå')



# num = int(input('enter a number between 1-10:'))
# while num < 1 or num > 10:
#     print(f'{num} is not valid')
#     num = int(input('enter a nummber between 1-10:'))

# print(f'your number is {num}')


#...................................................................................................

# a = 0 

# while a < 10:
#     print(a)

#     a += 1

# else:
#     print('loop is done')

# while False:
#     print('will not print')

# myf = ['af', 'kd', 'os', 'us', 'rs', 'ai']
# print(myf[0])
# print(myf[1])
# print(myf[2])
# print(myf[3])
# print(myf[4])
# print(myf[5])


#..........................................................................................................

