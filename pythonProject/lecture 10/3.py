import random


def write_to_file_random(loops):

    file = open(input("Enter the path to the file: "), "w")
    for i in range(0, loops):
        number = random.randint(0, 501)
        file.write(str(number))
        file.write("\n")
def main():
    try:
        number_of_loops = int(input("How many random numbers do you want: "))
        write_to_file_random(number_of_loops)
    except ValueError:
        input("You cant put this")

def __name__ = "__main__"