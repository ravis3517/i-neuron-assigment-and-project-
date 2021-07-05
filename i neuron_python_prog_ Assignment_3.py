#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero

# In[25]:



num = float(input("Enter a number: "))

if num >0:
    print("positive")
        
elif num <0 : 
    print("negative")
    
else: 
    print(" number is zero")
        
        


# 2. Write a Python Program to Check if a Number is Odd or Even?

# In[26]:


num=int(input("enter the number:\n"))

if (num %2==0): 
    print("The number is even")
else: 
    print("the number is odd")


# 3.Write a Python Program to Check Leap Year?

# A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400

# In[27]:


# To enter year by user 

year=int(input("Enter the year:\n"))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
    
        


# Write a Python Program to Check Prime Number?

# In[28]:



#test all divisors from 2 through n-1 (Skip 1 and n since prime number is divided by 1 and n )

num=10

for i in range(2,num): ## it will test till n-1 i.e till 9 
    if num % i == 0:
        print( num , " is Not prime")
        break
    
else :
    print( num ," is a prime")


# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[29]:


# Python program to print all
# prime number in an interval
# number should be greater than 1
first_number  = 1
last_number = 10000

for i in range(first_number  ,last_number +1):
    
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break            
        else:
            print(i)
  
    
    
    
 

