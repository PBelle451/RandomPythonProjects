import random
import string

def get_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    print(result_str)

if __name__ == '__main__':
    num = int(input("Insert how many passwords you wanna work with: "))
    size = int(input("Insert the size of the password: "))
    print("Your passwords: ")
    for i in range(num):
        get_random_string(size)