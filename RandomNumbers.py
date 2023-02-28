import random
size = int(input("Insert how many numbers do you want to work with: "))
for i in range(size):
    num = random.randint(1, 100)
    print(num)