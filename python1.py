#MULTIPLY A NUMBER WITH 32 WITHOUT USING ANY ARITHMETIC

a = int(input('enter a number : '))
a = a<<5
print(a)

#MULTIPLY A NUMBER WITH 33 WITHOUT USING MULTIPLICATION OPERATOR

a = int(input('enter a number : '))
print((a<<5)+a)

#SWAP TWO VALUES 

#1. USING A THIRD VARIABLE

a = int(input('enter first number'))
b = int(input('enter the second number'))
temp = a
a = b
b = temp
print ('after swappin' , a , b)

#2.WITHOUT USING THIRD VARIABLE , USE ARITHMETIC VARIABLE ONLY

num1 = int(input('1st number : '))
num2 = int(input('2nd number : '))


num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2


print('after swapping' , num1 , num2)

#3. WITHOUT USING THIRD VARIABLE OR ARITHEMETIC VARIABLE

a = int(input())
b = int(input())

a = a^b
b = a^b
a = a^b

print ('after swapping' , a ,b )
