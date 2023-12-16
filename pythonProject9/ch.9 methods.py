# adding key/value in an empty dictionary
# phonebook = {}
##phonebook['Chris'] = '555-1234'
# phonebook['Jess'] = '263-8987'
# phonebook['John'] = '275-6574'
# print(phonebook)
# for key in phonebook:  # this line will print out the keys that are in the dictionary
#   print(key, phonebook[key])
    # clear- clears the contents of a dictionary
    # get- gets the value associated with a sepcified key.
    # items- returns all they keys in a dictionary and their values
    # keys- returns all keys in dictionary as a sequence of tuples
    # pop- returns value associated witht he specified key and removes that key-value pair from the dictionary.
    # pop item- returns as tuple, they key value pair that was last added to the dictionary.
    # values- returns all values in the dictionary as a sequence of tuples.
movies = {
    1: 'Horror', 2: 'Fantasy', 3: 'Romance', 4: 'Action', 5: 'Comedy'
}
#for key in movies:
   # print(movies[key])

# clearing the dictionary
# movies.clear()

# the get method gets a value from the dictionary
#value = movies.get(4, 'Entry not found')
#print(value)

#the item method returns all the dictionaries keys and their associated values
#returned as a special type of sequence known as dictionary view
#for key, value in movies.items():
 #   print(key, value)

#the keys method returns all the dictionary keys as a dictionary view, which is a type of sequence.
#each element in the dictionary view is a key from the dictionary.
#for key in movies.keys():
 #   print(key)


#the pop method returns the value associated with a specified key and removes that key value
#pair from the dictionary. If key is not found, it returns a default value.
#movie_num = movies.pop(1, 'Entry not found')
#print(movie_num)
#print(movies)


#the popitem method performs 2 actions 1. removes the key value pair that was last added to the dictionary
#2. returns that key value pair as a tuple.
# k, v = dictionary.popitem()
#print(key, value)
key, value = movies.popitem()
print(key, value)
print(movies)


#the values method returns all a dictionary's values (w/o their keys)
#as a dictionary view, which is a type of sequence.
#Each element in the dictionary view is a value from the dictionary.
#for val in movies.values():
 #   print(val)


