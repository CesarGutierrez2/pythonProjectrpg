# first i'm going to create a dictionary where i store all the morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.-',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '

}


# with this line of code i define a function that takes the text and converts to morse code
def text_to_morse(text):
    morse_code = ''
    for char in text: #starts a loop that checks through each character in the text
        if char.upper() in morse_code_dict: #checks to see if the character presented is in the morse code dictionary i made earlier
            morse_code += morse_code_dict[char.upper()] + ' ' #if characte is in the dictionary it'll put the corresponding code and add a space in the end
        else:
            morse_code += char + ' ' #if not then it'll just show up as a space
    return morse_code


# i'm just asking the user to enter the sentence they want converted

user_input = input("Please enter a sentence: ")

# this code will convert the input into morse code
morse_code = text_to_morse(user_input)

# prints the morse code
print("Morse code: " + morse_code)
