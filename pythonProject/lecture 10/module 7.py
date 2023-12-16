#lists
my_list = [9, 8, 18, 0, -4, 12, 15] #indexes are  counted from 0 to N - 1
my_text_list = ["Orange", "Bananas", "Fruits"] #for list we use brackets # list can be changed
my_combo_list = ["Orange", 8, 3.45, "Cars"]
my_tuple = (4, 5, 8, 9) #tuples are the same, they use parenthesis #tuples cannot be changed
empty_list = []
#empty tuple = ()
print(my_combo_list)
#indexes are mutables, tuples are inmutable
length = len(my_combo_list)
print(length)

for elem in my_combo_list:
    print(elem)


#adding something to a list
my_list.append(6)
print(my_list)

#inserting value
my_list.insert(2, 10)
#print(my_list)

#replacing a number in a list
my_list[2] = 10 #finding location to replace
print(my_list)


#remove from list
try:
    my_list.remove(5)
    print(my_list)
except ValueError:
    print("That element is not on the list") #the try and except function keep program from crashing if 5 is not found


my_list.pop(3)
print(my_list)

del my_list[1]
print(my_list)

#printing value in a specific index
print(my_combo_list[3])
print(my_combo_list.index("Cars"))

#reversing or flipping the list
#my_list.reverse()
#print(my_list)

#sorting the list sets it to ascending order only, lowest to greatest
#my_list.sort()
#print(my_list)

#my_list.reverse()
#print(my_list)

#using sort and then reverse will put it in descending order
#adding grades in gradebook
grade_book = []
how_many_grades = int(input("How many grades: "))
for i in range(0, how_many_grades):
    grade = int(input("Enter the first 10 grades: "))
    grade_book.append(grade)
    #grade_book[i] = grade
print(grade_book)

total = sum(grade_book)
length = len(grade_book)
print(total / length) #gives us the mean

grade_book[2] = 100 #replacing the 2nd index with 100
print(grade_book)

index = grade_book.index("troubador") #grabbing the location of this value
print(index)

grade_book[index] = 75
print(grade_book) #replacing troubador with the 75

