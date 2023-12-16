def StoredPasswords(): #putting the passwords in a tuple
    common_passwords = (
        "123456", "123456789", "12345", "qwerty", "password", "12345678", "111111", "123123",
        "1234567890", "1234567", "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123",
        "password1", "1234", "qwertyuiop", "123321", "password123", "1q2w3e4r5t", "iloveyou",
        "654321", "666666", "987654321", "123", "123456a", "qwe123", "1q2w3e4r", "7777777",
        "1qaz2wsx", "123qwe", "zxcvbnm", "121212", "asdasd", "a123456", "555555", "dragon",
        "112233", "123123123", "monkey", "11111111", "gazwsx", "159753", "asdfghjkl",
        "222222", "1234qwer", "123654", "123abc"
    )
    return common_passwords #naming the list of common passwords


def getUserPass():
    user_name = input("Please enter a username: ")
    user_password = input("Enter your password please: ")
    common_passwords = StoredPasswords()

    if user_password in common_passwords: #we check if the password the user inputs is in the common_passwords list
        print(f"Your password is too common. Please enter another: ")
        index = common_passwords.index(user_password)  #this code we find out where the common password is.
        print(f"Found at index {index}")
    else:
        print("You have a strong password!")


if __name__ == '__main__':
    getUserPass()
