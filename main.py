import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.ascii_letters

    while True:
        try:
            n = int(input('How many passwords do you want? '))
            break
        except ValueError:
            print('Please enter a number.')
    while True:
        try:
            plen = int(input("Enter Password Length: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    for p in range(n):
        print("Your " + str(p+1) + " password is: ")
        print("".join(random.sample(s1 + s2 + s3 + s4 + s5, plen)))
