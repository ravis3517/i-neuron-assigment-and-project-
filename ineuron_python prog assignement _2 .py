#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to convert kilometers to miles?

# In[6]:


#Conversion logic:
## Miles = kilometer * 0.62137 or Kilometer = Miles / 0.62137

#  create a variable km to take user input 

km = float(input(" Enter the unit in km :\n"))

# Store conversion factor as vaule in variable 

conversion_ratio = km*0.621371 


# convert km into miles using conversion factor 

miles =km* conversion_ratio

print("The speed value in Miles:\n", miles) 

   


# 2. Write a Python program to convert Celsius  to fahrenheit?

# In[8]:


# Formula : 
##Teamperature in FaHrenheit =(temperature in celsius *18)+32


# Take user input in celsius 

Celsius=float(input("Enter temperature in celsius:\n"))

# conversion formula 

fahrenheit = (Celsius * 1.8) + 32

# printing the result 

print("The temperature in farhenhiet :\n ",fahrenheit)


# 3. Write a Python program to display calander ? 

# In[11]:


# To display calendar of# given month of the year

# import  calander module


import calendar

yy = 2040
mm = 8

# display the calendar


print(calendar.month(yy, mm))


# 4. Write a Python program to display calander ? 

# 
#  For the quadratic equation ax² + bx + c = 0, if we denote the discriminant as d, then their roots
# 
# #If d>1 then the roots are real and different
#  root1 = (-b + √d)/2a
#  root2 = (-b – √d)/2a
# 
# If d=0 then both roots are -b/2a
# 
# If d<1 then roots are complex and different
# root1 = -b/2a + i (√d/2a)
# root2 = -b/2a – i (√d/2a)
# 

# In[ ]:


# Python program to find roots of quadratic equation


#importing math-module

import math 


# Take user input : 


a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))


# calculate discriminant
D = (b**2) - (4*a*c)

# checking condition for discriminant


if(D > 0):
    root1 = (-b + math.sqrt(D) / (2 * a))
    root2 = (-b - math.sqrt(D) / (2 * a))
    print("Two distinct real roots are %.2f and %.2f" %(root1, root2))

elif(D == 0):
    root1 = root2 = -b / (2 * a)
    print("Two equal and real roots are %.2f and %.2f" %(root1, root2))

elif(D< 0):
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-D) / (2 * a)
    print("Two distinct complex roots are %.2f+%.2f and %.2f-%.2f" 
                          %(root1, imaginary, root2, imaginary))


# In[ ]:


5. Write a Python program to swap two varibales without temp variable ? 


# In[2]:


## 1st method 
# Take user input 

x=int(input("Enter value of first variable: "))
y=int(input("Enter value of second variable: "))


x=x+y
y=x-y
x=x-y

#printing result after swapping 

print("Value of First Varibale and second variable  x and y is:",x ,y)


# In[3]:


## Second method to swap two variable without using temp variable 

a=5
b=10

a,b=b,a # the right side will be solved first , this goes into stack then it reverse 
        ## This works only for single line of code 
print(a,b)


# In[ ]:




