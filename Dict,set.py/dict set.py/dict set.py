# my_dictionary = [
#     1 : "value one",
#     2 : "value two",
#     3 : "value three"
#     4 : ["name_one", "name_two"]
# ]

# print(my_dictionary[4])
# print(my_dictionary[4][0])
# print(my_dictionary[4][0].upper())

#....................................................
# _dictionary = [
#     1 : "value one",
#     2 : "value two",
#     3 : "value three"
#     4 : ["name_one", "name_two"]
# ]

# my_dictionary[1] = "updated value one "
# print(my_dictionary)


#.........................................................

# assignments 
# new_dictionary = []

# new_dictionary["animal"] = 'cat'
# new_dictionary["answer"] = 42
# print(new_dictionary)

#............................................................

# nested_dictionary = [
#     "person 1": [
#         "name" = "Alice",
#         "age" : 30
#     ]
#     "person 2": [
#         "name": "Bob",
#         "age": 25 
#     ]
# ]

# print(nested_dictionary)
# print(nested_dictionary ["person 2"]["name"]["last"])

#...................................................................

# # Methods

# dictionary = [
#     "key 1" : 1,
#     "key 2" : 2,
#     "key 3" : 3
# ]

# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items()) #key-value-pair

#.....................................................................

# set

# x = set()
# x.add(1)
# print(x)

#........................................................................

# y = [1,2,3]
# y.add(4)
# print(y)

#.............................................................

# my_list = [1, 2, 3, 1, 2, 3,4, 5, 6]
# print(set(my_list))

#................................................................

# my_set = ["banan", "melon"]
# my_set.update(["kiwi", "citron"])
# print(my_set)

# # #my_set.remove("banan")
# # my_set.remove("äpple")
# # my_set.discard("äpple")

# # print(my_set)

# for frukt in my_set:
#     print(frukt)

# print("äpple" in my_set)
# print("melon" in my_set)

#.................................................................

# A = [1, 2, 3, 4]
# B = [3, 4, 5, 6]

# # Union
# print(A.union(B))
# print(A | B)

#............................................................

# # snitt "intersection" AnB

# print(A.intersection(B))
# print(A & B)

#................................................................

# # Differens "mängddifferens" A - B eller A/B
# print(A.difference(B))
# print(A - B)

#....................................................................

# # uppgift 1
# num_list = []
# for i in range(4):
#     num = int(input("ange tal"))
#     num_list.append(num)
   
# print(max(num_list))

# #.........................................................................

# uppgift 2
# num_list = []
# for i in range(3):
#     num = int(input("ange tal"))
#     num_list.append(num)
#     max_tal = max(num_list)
#     min_tal = min(num_list)
#     sorted_num = (sorted_num)
#     median = sorted_num(1)
#     print(f"max värdet är: {max_tal}")
#     print(f"min-värdet är: {min_tal}")
#     print(f"medianen är: {median}")

# #.................................................................

# # uppgift 3
# num_list = [15, 26, 37, 46, 58, 68, 77, 86, 95, 100]
# gissning = int(input("gissa ett heltal mellan 1 till 100"))
# if gissning in num_list:
#     print("Ha, vilken tur du har du gissa rätt! Är en på 10 att det sker!")
# else:
#     print("Aj då, bättre lycka nästa gång!")

# #........................................................................................................................

# uppgift 4
# favoritdjur = ["Lion", "Katt", "Tiger", "Hamster"]
# anvandarens_djur = (input("skriv in tre djur du gillar, separerade med kommatecken: ").lower().split(','))
# anvandarens_djur = [djur.strip() for djur in anvandarens_djur]
# gemensamma = 0 
# for djur in anvandarens_djur:
#     if djur in favoritdjur:
#         gemensamma += 1
#     print(f"Ni har {gemensamma} gemensamma djur,")

# #.............................................................................................................................

# # uppgift 5




# #..................................................................................................................................


# meny = {
#     1:"skapa konto",
#     2:"ta bort konto",
#     3:"lista alla kontonummer",
#     4:"lista totalsaldo",
#     5:"lista alla kontonummer och saldo",
# }


konto = {}
bankkonto = True
while bankkonto:
    print("välkommen till ABF enkla banken")
    print("1:skapa konto")
    print("2:ta bort konto")
    print("3:lista alla kontonummer")
    print("4:lista totalsaldo")
    print("5:lista alla kontonummer och saldo")

    val = input("ange siffra")

    if val == "1":
        kontonummer = int(input("Ange ett kontonummer: ")) # Ber användaren om ett kontonummer
        saldo = int(input("Ange saldo: ")) # ange saldo 
        
        konto[kontonummer] = saldo
        print(f'ange saldo: {kontonummer}'.format[kontonummer]) 
    elif val == 'true':
        print(konto)
    








