# Program to implement sequential search

target = int(input("Enter a number ")

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
     if target == numbers[i]:
        print("Found {}".format(i))
        break

