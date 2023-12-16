# module 9 dictionaries lecture
import json

# grade_book = {'Gina': [100,90,10], 'Tina': [45,50,48], 'Rob': [78,84,82]}

# finding value in a dictionary
# student_name = input("Enter the students name to see their respective grades: ")

# if student_name in grade_book:
#   print(grade_book[student_name])

# works like ELSE, but actually searches through the dictionary
# if student_name not in grade_book:
#   print("She doesn't even go here!")

# changing the value of the index
# if student_name in grade_book:
# grade_change = int(input("which grade do you want to change?: "))
# grade_change = grade_change - 1
# new_value = int(input("Enter your new grade: "))

#    for key in grade_book:
#       grade_book[student_name][grade_change] = new_value
#  print(grade_book)

# using a for loop to iterate through the dictionary
# for key, value in grade_book.items():
#    file.write('%s:%s\n' % (key,value))

# file.write(json.dumps(grade_book))

# w/o json and dumps
# file.write(str(grade_book))

# file.close()


phonebook = {'Karl': 555 - 8998, 'Tim': 908 - 7467, 'Nelly': 987 - 8938}
print(phonebook)
phonebook['Karl'] = '954-8998'
phonebook['Terrance'] = '305-5565'
print(phonebook)

# deleting
del phonebook['Terrance']
print(phonebook)

# length of dictionary
len(phonebook)
print(phonebook)

# forloop
for key in phonebook:
    print(key, phonebook[key])

# 2 dimensional array
# tw_dim[2][3] means to create 2 rows and 3 columns

# using clear method
phonebook.clear()
print(phonebook)

# squaring numbers
numbers = [1, 2, 3, 4]
squares = {item: item ** 2 for item in numbers}
#or
# empty = {}
#for item in squares:
#   empty = squares[item][item**2]
print(squares)


#sets
mySet = set()
mySet = 'abc'
print(mySet)

#using sets
set1 = set([1,5,19,8])
set2 = set([7,6,19,4,1,11])
set3 = set1.union(set2)
print(set3)

#intersection of sets, commonity
set4 = set1.intersection(set2)
print(set4)

#difference of sets
set5 = set1.difference(set2)
print(set5)

#symmetric difference - whats unique to each set
set6 = set2.symmetric_difference(set1)
print(set6)




