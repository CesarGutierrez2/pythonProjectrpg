# Create a tuple with 50 of the most common passwords
common_passwords = (
    "123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123",
    "1234567890", "1234567", "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123",
    "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou",
    "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777",
    "1qaz2wsx", "123qwe", "zxcvbnm", "121212", "asdasd", "a123456", "555555", "dragon",
    "112233", "123123123", "monkey", "11111111", "qazwsx", "159753", "asdfghjkl",
    "222222", "1234qwer", "qwerty1", "123654", "123abc"
)


# Function to check if a password is common
def StoredPasswords(checkPass):
    found = "Your password is too common. Please consider changing it."
    notFound = "You have a strong password."

    for index, password in enumerate(common_passwords):
        if checkPass == password:
            print(f"Password found at index {index}")
            return found

    return notFound


# Function to get user's password
def getUserPass():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return password


# Main function
def main():
    userPass = getUserPass()
    result = StoredPasswords(userPass)
    print(result)


if __name__ == '__main__':
    main()
