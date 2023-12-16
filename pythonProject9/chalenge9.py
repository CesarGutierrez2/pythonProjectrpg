# importing re module which is used for regulare expressions
import re

file_path = "Word Frequency.txt"
# opening and reading the text file
try:
    with open("Word Frequency.txt", "r", encoding="utf-8") as file:
        text = file.read()  # reads the contents of the file and stores it in the 'text' variable
except FileNotFoundError:
    print(f"Error: File '{'Word Frequency.txt'}' not found")  # error if file doesnt exist
    exit(1)  # exits the program

# tokenizes the text variable into words
# re.findall will find all word like substrings in the text and converts it into lower case wording
words = re.findall(r'\b\w+\b', text.lower())

# creating a dictionary that will store the word frequencies
word_freq = {}
# iterates through the list of words and counts the frequency for each word
# filling up the dictionary
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# showing the word frequency in a formatted table
max_word_length = max(len(word) for word in word_freq)
max_freq_length = len(str(max(word_freq.values())))

print("Word".ljust(max_word_length) + " Frequency")
print("-" * (max_word_length + 12))

# this for loop goes through the sorted items of the dictionary and prints
# each word wit the key and value
for word, freq in sorted(word_freq.items()):
    print(word.ljust(max_word_length) + f" {freq:{max_freq_length}}")
