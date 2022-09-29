#IMPORTANT: USE ONE TYPE OF VARIABLE IN LIST
# list = [1, 2, 3, 4]
# list_animal = ['Dog', 'Cat', 'Fish']

#
# print (list)#Thats not correctly to show list
# print(list[1])# I show position one in list
#
# #Using for loop to show list line by line
# for x in list:
#     print(x)
#
# #Calculate using for loop with list
# sum = 0 #I need to declare a variable sum
# for x in list:
#     print(x)
#     sum += x
# print('A soma das variaveis dentro do list é: {} \n' .format(sum))
#
# #I can use another function to sum the list values, it's too easy, just use the function sum
# # sum = sum(list)
# # print(sum)
#
# #Print the max value or variables according to the alphabet
# print('-----Max-----')
# print(max(list))
# print(max(list_animal))
# # print('\n')
#
# print('-----Min-----')
# print(min(list))
# print(min(list_animal))
#

#Example using IF
# animal = input('Insert an animal: ')
#
# if animal in list_animal:
#     print('Exist animal on list')
# else:
#     print('Doesnt exist animal on list')

# #Example using WHILE
# x = 0
# while x == 0:
#     animal = input('Insert an animal: ')
#     if animal in list_animal:
#         x += 1
#     else:
#         print('Doesnt exist animal on list')
#
# print('Exist animal on list')

# x = 0
# while x == 0:
#     animal = input('Insert an animal: ')
#     if animal in list_animal:
#         print('Exist animal on list!!!')
#         confirm = input('Do you want continue? (Y=yes or N=no)')
#         if confirm == 'Y' or 'y' in confirm:
#             x = 0
#         else:
#             x += 1
#     else:
#         print('Doesnt exist animal on list')
#
# print('Process finished')

# pop = list_animal.pop() #Show last value on list
# print(pop)

print("LIST []")

thislist = ["apple", "banana", "cherry"]

print('#Access Items')
print(thislist[1])#Print the second item of the list - Initial position is 0
print(thislist)
print('\n')

print('#Change Item Value')
thislist[1] = "blackcurrant" #Change the second item
print(thislist)
print('\n')

print('#Append/Extend Items')
thislist.append("Orange") #Using the append() method to append an item
thislist.extend("Orange") #Using the extendend() method to extend an item
print(thislist)
print('\n')

print('#Remove Specified Item')
thislist.remove("blackcurrant") #The remove() method removes the specified item
print(thislist)
print('\n')

print('#Print all items in the list, one by one')
for x in thislist:
    print(x)
print('\n')

print('Make a copy of a list with the copy() method')
mylist = thislist.copy()
print(mylist)
print('\n')

print('List objects have a sort() '
      'method that will sort the list alphanumerically, ascending, by default')
mylist.sort()
print(mylist)
print('\n')

print('TUPLE ()')
print('A tuple is a collection witch is a ordered and unchangeable')
print('\n')

print('Dictionaries {}')
print('A dictionary is a collection witch is ordered (Version 3.7),'
      'changeable and do not allow duplicates')
print('Example')
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)
print(thisdict["brand"])#Case sensitive
print(thisdict["model"])
print(thisdict["year"])
print('\n')

print('Set')
print('Sets are written with curly brackets {}')
thisdict.setdefault('year', 1964)
thisdict.setdefault('year', 1965)
thisdict.setdefault('color', 'Red')
print(thisdict)
print(thisdict["brand"])#Case sensitive
print(thisdict["model"])
print(thisdict["year"])
print(thisdict["color"])





