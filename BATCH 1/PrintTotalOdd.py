#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
number =[int(input("Enter a number: "))for i in range (10)]
odd count= sum(1 for num in number if num %2!=0)
