#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?

# In[1]:


#print "Hello Python"

print("Hello world ")


# 2.	Write a Python program to do arithmetical operations addition and division.?
# 

# In[2]:


#arithmetical operations addition and division.

## To perform multiplication, we need to use the * character.
##To perform division, we use the / character


print("4+5")


print("26-9")


print("225/5")


print("6**3") 

print ("9*3")


# 3.	Write a Python program to find the area of a triangle?

# In[3]:


## Python program allows the user to enter three sides of the triangle.


a = float(input(' Enter the First side of a Triangle: '))
b = float(input(' Enter the Second side of a Triangle: '))
c = float(input('Enter the Third side of a Triangle: '))

# Now we will calculate the Perimeter
Perimeter = a + b + c

# Next step will be to calculate the semi-perimeter
s = (a + b + c) / 2

###  calculate the area

Area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("\n  Perimeter of Traiangle =  %.2f" % Perimeter);
print(" \n Semi Perimeter of Traiangle = %.2f" %s);
print(" \n  Area of a Triangle is %0.2f" %Area)


# 4.	Write a Python program to swap two variables?

# In[8]:


# two number to be swapped a=10 , b=5  we want to swap a=5 , b=10 
# two methods can be used to swap 


a=5
b=10 

## first method (using 3rd varibale to swap the numbers ) , that is used in most of other language 
## we cannot use a=b , th moment we will do that we will loss a=5 , we wanted to have 5 as well 
### for that reason we will create a teamp vailbale 

temp=a #(take the vaule of a and assign it to a temp varibale )

a=b 

b=temp
print(a)
print(b)

### limitation is we are wasting a varibale 


# In[11]:


## 2nd method to swap the varibale is 

a=5
b=10

a,b=b,a # the right side will be solved first , this goes into stack then it reverse 



print(a,b)


# 5.	Write a Python program to generate a random number?

# In[5]:


# Program to generate a random number between 0 and 9

# importing the random module
import random

number = random.randint(0,10)

print(number)

