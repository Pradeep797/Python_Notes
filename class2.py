
# or 
# variable are use to store the data
# or
# variable it is a container where we store the values/data
# variable:- it is a sort name of any values

# x = "INDIA"
# print(x)

# x = 45
# y =60

# 1. single variable

# x = 45
# y = 60

# 2. multipule variable

# x,y = 45,60
# print(x)
#comment :- it is a statement that we want to show but don't want to excute

# --------------------------------

# limitation of variable
# 1.variable should we start with alphabets
# 2.variable can be alphanumeric (x2)
# 3.variable case sencetive
# 4.here you can not insert any special charactore(@$%&*)
# 5.here you can use (_) under_score in variable

# A = "hello world" 
# print(A)

# b2 = 4561
# print(b2)

# name = "pradeep"
# print(name)

# country_name = "india"
# print(country_name)
#indentationerror = it is a extra space starting of code
# print("hello world!")
# x = 45
# y = 30

# print("addition:-",x+y)



# print("substraction:-",x-y)

# print("multiplication;-",x*y)

# print("devision;-",x/y)


#print the sum of three number that given below
# x = 45
# y = 60
# z = 80

# add = x + y + z
# print(add)

#print the multication of four number
# a,b,c,d = 5,4,8,9

# mul = a*b*c*d
# print(mul)

#print your name with variable

# name = "pradeep"
# print(name)

# x = 10
# y = 20

# m = x*y
# print(m)
'''
data type:
-------------------------------------------------------
1. numerical data :- 1. integer int 2. floot 3. complex 21j
2. text data      :- string str  "" double quatation


   string :-string are written in dual or single quatation.

3. sequence data :- list[] , tuple () , range()

4. mapping :- dictionary {}
           :- dictionary are written in curly bracket and pair
            of key and values.
5. set :- set {}
       :- set are written in curly bracket{}
6. boolen data :- True , False
7. none :- none
------------------------------------------------------------

x = {key : values}

list :- list always written in square bracket

x = ["data","science",343,45,55]

tuple :-tuple are written in round bracket.

range() :- it is used to print the number in a sequence
range(starting,ending,step_size)
range(1,100)
'''

# numerical data

#x = 45

# how to chek the data type
#t = type(x)
#print(t)

 # or

#print(type(x))

 # x = 789
 # y = 456.89
 # z = 21j
 # a = "pradeep" 
# x = 789
# print(x)
# print(type(x))

# y = 456.89
# print(y)
# print(type(y))

# z = 21j
# print(z)
# print(type(z))

# a = "pradeep"
# print(a)
# print(type(a))
#x = "data science"
# how to find the lenth of the text
#len()

#print(x)
#print(len(x))


# x = "12000"
# print(len(x))
# x = 10
# y = 20
# print(x+y)

# x = "data"
# y = "science"
# print(x+y)


# forecasting of data :- 

# it is use to change the data type.

# x = 456
# #print(type(x))

# y = str(x)  # change into string
# print(type(y))

# print(x*5)

#x = "125"

#change into float
#change into complex
#change in list
#change in int

#f = float(x)
#print(type(f))

#c = complex(x)
#print(type(c))

#l = list(x)
#print(type(l))

#i = int(x)
#print(type(i))

#x = 456789
#print(x)
# x = "100"
# y = "200"

# a = int(x)
# b = float(y)
# print(x+y)

# x = "data"
# y = list(x)
# print(y)

#print(12/12)

# x = 12 
# y = 12
# z = x/y
# print(type(z))


#x = 120.789
#print(type(x)) {kis type ki value h pta krne ke lie print(type)}
#print(len(x))
'''
types of operatores:-
-------------------------------------------------------

1. arithmatic operatores
2. assignment operatores
3. comperision operatores
4. logical operatores
5. identity operatores
6. membership operatores
7. bitwise operatores

--------------------------------------------------------

1. arithmatic operatores
+ : addition
- : substraction
* : multication
/ : division
% : modules :- modules show reminder
** : exponentation :-it is used to add the power on number
// : floor division :-it is show the value before the decimal
'''
'''
x = 45
y = 20
print("modules:-",x%y)

#print("the reminder of",x,"and",y,"is :",x%y)

print("the reminder of" ,x, "and" ,y, "is", x%y)
'''

#x = 5  # exponentation(no. ko power me add krta h)
#y = 3

#print(x*y)
#print(x**y)

#x = 19
#y = 5
#print(x//y)

#print(19%4)
#print(1.3//1)

#print(45//8.5)

#x = 100
#y = 7
#z = x//y
#print(z)

#x = 2
#print(x**4)

#print(3**3)

#---------------------------------------------------
'''
2. assignment operatores
= : assignment   
== : equal to
!= : not equal to
+= :      (or)  x = x+1
-= :       (or) x = x-1
*= :     (or)   x = x*1
/= :      (or)  x = x/1
'''
# x = 45
# y = 45
# print(x==y)  # equal

#not equal to

#x = 100
#y = 200
#print(x==y)
#print(x!=y)

#plus equal to (+ = or x = x+1 )
'''
x = 50
#x = x+5
x+=5
x+=10         # or  x = x + 10
print(x)
'''

# x = 45
# y = 10
# print(x>y)
# print(x<y)


# x = 100
# y = 100
# print(x==y)
# print(x<=y)

# if___else statement

# if else :- it is used to divide
# the data in different diffrent
# category

#write a python program to show the number
#if number is greater than 10 then print
#yes else print no

# x = 15
# if x>10:
# 	print("yes")
# else:
# 	print("no")

# x = 100
# if x>50:

# 	print("yes it is greater than 50")
# else:
# 	print("it is not greater than 50")

#write a python program to chek the number is even or odd

#x = 19
#if x>10:
	#print("yes it is greater than 10")
#else:
	#print("it is not greater than 10")

#if x%2==1:
	#print("odd number", x)


# chek the number is divisible of 9 or not

# x = 81
# x = 75
# x = 45

# if x%9==0:
# 	print("divisible of", 9)


#user input :- it is a input where you enter the values in output screen

# x = int(input("enter any number:-"))
# if x%2==0:
# 	print("even number")
# else:
# 	print("odd number")


#write a python program with the help of user input and show the number is greater than 200 then print "yes greater than 200"
#else print"less than 200"


# x = int(input("200"))
# if x>200:
# 	print("greater than", 200)
# else:
# 	print("less than", 200)


# chek the text is equal to
# delhi then print yes else print no

#x = str(input)("enter ant text :-")
# = if x==("delhi":
# print("yes")

#else:
#print("no")

#write a python program to show the
#state and capitalaccording to user input

# x = str(input("enter the state name :-"))
# if x== "bihar":
# 	print("patna")
# else:
# 	print("other")

# # logical operator
# and :- it return true when condition are true
# or :- it return true at least one condition is true
# not :- its reserve the output of   (and or)


# x = 15
# y = 10

# #print(x>10 or y>15)
               
# if x>10 and y>5:
# 	print("both condition are true")
# else:
# 	print("wrong condition")

#write a python progam to show to chek the number it b/w 20 to 30
#then print "yes"
#else then print "no"

# x = 25
# if x>20 and x<30 :
# 	print("yes")
# else:
# 	print("no")

#write a python program to chek if number is divisible
#of 10 or 5 then print "yes" else print "no"

# x = 8
# if x>10:
# 	print("yes")
# 	else:
# 		print("no")

# x = 100

# if x>50:
# 	print("yes it is greater than 50")
# else:
# 	print("it is not greater than 50")


#write a python program to chek the number is even or odd

# x = 11
# #print (x%2==0)

# if x%2==0:
# 	print("even number")
# else:
# 	print("odd number")

#write a python program to check number is odd

# x = 19
# if x%3==0:
# 	print("even number")
# else:
# 	print("odd number")

#check the number is divisible of 9 or not
#x = 81
# x = 75
# #x = 40

# if x%9==0:
# 	print("print divisible of 9")


# x = int(input("enter number:-"))

# if x>200:
# 	print("greater than 200")
# else:
# 	print("less than 200")

#chek the text is equal to delhi then print yes else print no

# x = str(input("enter any text :-"))

# if x=="delhi":
# 	print("yes")
# 	print("no")

#write a python to show the capital according to user input

# x = "bihar"
# x = str(input("bihar :-"))
# if x=="bihar":
# 	print("patna")
# else:
# 	print("lucknow")

# logical operatores
# and :- it return true when both condition are true
# or :- it return true when at least one condition is true
# not :- its reverse the output of  (and  or)

# x = 15
# y = 10
# #print(x>10 or y>15)


# if x>10 and y>5:
# 	print("both condition are true")
# else:
# 	print("wrong condition")


#write a python program to chek the number is b/w 20 to 30 than print "yes"
#else print "no"

# x = 25

# if x>20 and x<30:
# 	print("yes")
# else:
# 	print("no")


# write a python program to check if number is divisible of 10 or 5 then print yes else print n

# x = int(input("enter number :-"))

# if x%5==0 or x%10==0:
# 	print("yes")
# else:
# 	print("no")


#write a python program to check and compare two who is greatest
#number

# x = 45
# y = 13

# x = int(input("enter first number :-"))
# y = int(input("enter second number :-"))
# if x>y:
# 	print(x,"is greater than",y)
# else:
# 	print(y,"is greater than",x)
	




 #write a python program to check the number is divisible of 5 and 10
# x = int(input("enter number :-"))
# if x%5==0 and x%10==0:
#  	print("divisible of 10 and 5")
 
# else:
#  	print("not divisible")
 


#write a python program to print the last digit of any number 
#if number is odd
# x = int(input("enter number"))
# if x%2==1:
# 	print(x%10)




# write a python program with the help of user input to check
# if password is equal the print "correct password"
# else print "wrong password"

# p = 1234
# x = int(input("enter your pin :-"))

# if x==p:
# 	print("correct password")
# else:
# 	print("wrong password")


# write a python program to print the discount and
# discounted amount if amount is less 5000 than 20%
# else 30%
# amount = float(input(" discount amount"))
# if amount<5000:
# 	print(amount-amount*0.2)
# else:
# 	print(amount-amount*0.3)

#              or


# amount = float(input("enter amount:-"))  
# if amount<5000:

# 	d = amount*0.2
# 	a = amount-d

# else:
# 	d = amount*0.3
# 	a = amount-d

# print("discount:-",d) 
# print("after discount:-",a)  

#---------------------------------------------------
# 1,10 - first
# 10,20 - second
# 20,30 - third
# 30,40 - forth
# --------------------------------------------------

#x = int(input("enter number:-"))

# if x>=1 and x<10:
# 	print("first")

# elif x>=10 and x<20:
# 	print("second")

# elif x>=20 and x<30:
# 	print("third")

# elif x>30 and x<40:
# 	print("forth")

#x = int(input("enter number":-))

#------------------------------------------------
# swapping in python
# membership operatores
# identity operatores

#1. what is swapping in python
#in when we exchange the values to other variable
#that is called swapping in python.


# x = 45
# y = 10

# print("x :-",x)
# print("y :-",y)

# print("after the update")

# x,y = y,x

# print("x :-",x)
# print("y :-",y)


# x = 20
# y = 30
# z = 40

# x,y,z = z,x,y
# print(x)
# print(y)
# print(z)

# x,y,z = 45,78,100

# x = y
# y = x
# print(z)
# print(x)
# print(y)

# x = 100
# y = 200
# z = 300

# x,y = z,x   # x = 300 y = 200

# z = y
# print


# x,y,z = 10,20,30
# x,z,x = z,x,y
# y=z
# print(x)

# x,y = "59"
# z = 12

# x,y = z,x
# z,x = z,y
# x = y
# print(x)
# print(y)
# print(z)


# x = "science"

# print("i" in x)
# print("I" in x)
# print("z" not in x )
# print("s" not in x)

# x = [23,4,5,6,7,8,10]

# check 24 in list or not
# check 10 in list

# 1. write a python program with the help of user input to print
# if name contain a or i then print "yes"
# else print "no"
 # x = int(input("name :-"))
 # if ("name",a) or ("name",i):
 # 	print("yes")
 # else:
 # 	print("no")
     
#--------------------------------------------------------------

 #   x = ["sunday","monday","tuesday","wednesday"]
  # if sunday in x then print present
  # else print not present.


 # x = str(input("enter name"))
 # if ("a" in x) or ("i" in x):
 # 	print("present")
 # else:
 # 	print("not present")

#write a python program to show the grade
# if number is greater than 90 then print "a+" 
# if number is greater than 80 then  print "a"
# if number is irs greater than 70 then print "b+" 
# if number is greater than 60 then print "b"  
# if number is greater than 50 then print "c" 
# else print "d"  

# x = int(input("enter number:-"))
# if x>50:
# 	print("c")
# else:
# 	print("d")


#------------------------------------------------------------------ 

#1. write a program to check whether the given input number is
#divisible by 3 or else show a message "number is not divisible by 3"

# num = int(input("enter number:-"))
# # divisibility check
# if num%3==0:
# 	print("the number", num , "is divisible by 3:-")
# else:
# 	print("the number", num , "is not divisible by 3")


#2. write a program that check whether the given input is an even
# number or an odd number
# num = int(input("enter number"))
# if num%2==0:
# 	print("0" "is even", num)
# else:
# 	print("0" "is odd" , num)


#3. write if/else statement with the following condition:
# if the variable is greater than 18, output "old enough",
# other wise output "too young"

# age = int(input("enter age:-"))
# if age>18:
# 	print("old enough")
# else:
# 	print("too young")

#5.
# year = int(input("enter year:-"))
# if year%400==0 and year%100==0:
# 	print("0 is a leap year", year)
# else:
# 	print("0 is not a leap year", year)



#7. write a program that takes input a number from user and state
 # whether the number is possitive, negative or zero

# num = int(input("20"))
# if num>0:
# 	print("positive number")
# else:
# 	print("negative number" or "zero number")

	

# #11. 
# x = int(input("enter time in hole number:-"))
# if x<1200:
# 	print("good morning")

# elif





#----------------------------------------------------------
# x = "data type"
# # show the data type of x
# # show the lenth of the x

# a = len(x)
# print("lenth of x:-",a)

# b = type(x)

# print("data type of x:-",b)


# print("phone pay:-")
# print("_"*50)
#---------------------------------------------------------------
# pin = 1234
# u = 5678

# x = int(input("enter pin:-"))
# y = int(input("enter upi pin:-"))

# if x==pin:
# 	if y==u:
# 		print("unclock")

# 	else:
# 		print("upi pin is wrong")

# else:
# 	print:("wrong pin")

#------------------------------------------------------------
# x = str(input("name of board:-"))

# if x =="bseb":
# 	print("welcome to bihar board")
# 	cl = int(input("enter class number:-"))
# 	if cl == 9:
# 		print("welcome to class 9th")
# 	elif cl == 10:
# 		print("welcome to class 10th")



# elif x == "cbse":
# 	print("welcome to central board")
# 	cl = int(input("enter class number"))
# 	if cl == 11:
# 		print("welcome to class 11th")
# 	elif cl == 12:
# 		print("welcome to class 12th")

# else:
# 	print("you enter wrong board")

#----------------------------------------------------------
# x = str(input("name of board:-"))

# if x =="bseb":
# 	print("welcome to bihar board")
# 	cl = int(input("enter class number:-"))
# 	if cl == 9:
# 		print("welcome to class 9th")
# 	elif cl ==10:
# 		print("welcome to class 10th")



# elif x == "cbse":
# 	print("welcomre to central board")
# 	cl = int("enter class number")
# 	if cl == 11:
# 		print("welcome to class 11th")
# 	elif cl == 12:
# 		print("welcome to class 12th")
#------------------------------------------------------------------			
#write a program that takes input a number from other and state
#whether the number is possitive, negative or zero

# x = int(input("enter the number"))
# if x>0:
# 	print("positve number")
# else:
# 	print("negative number")
#--------------------------------------------------------------------
# 11.write a program take a character (i,e string og leanth 1)
#and return true if it is a vowel,false otherwise

# x = str(input("enter any alphabets:-"))
# if x in ("a","e","i","o","u"):
# 	print("vowels")
# else:
# 	print("consonents")

#----------------------------------------------------------
	
# x = int(input("inter score of india:-", 345))
# y = int(input("inter score of australia:-", 340))

# if ind>aus:
# 	winner = "india"
# 	m = ind - aus
# else:
# 	winner = "australia"
# 	m = aus - ind
# 	print("winner is :-",w)
# 	print(w,"won by:",m,"runs")

                                                                                                                                         
# pak = int(input("enter score og pakistan:-",250))
# eng = int(input("enter score og england:-", 240))

# if pakistan >eng:
# 	w2 = "pakistan"
# 	m2 = pak - eng
# else:
# 	w2 = "england"
# 	m2 = eng - pak
# 	print("winner is :-"w)
# 	print(w,"won by:",m,"runs")


# 	print("winner is:-")
#----------------------------------------------------------
# find the area of circle:
# x = 7
# pie = 22/7
# area = pie*x*x
# print("area of circle",area)


#show the average of first five number
# x = 1+2+3+4+5
# average = x/5
# print("average of ",x)

#---------------------------------------------------------


#string:- it is always written dual quation or single quation

# x = "pradeep"
# print(x)

# print(type(x))

# print(len(x))
		


#x = "data science"

#---------------------------------------------------------
# string function
#-------------------------------------------------------

# x = "3456"
# print(type(x))
# print(len())






# upper :- it is used to convert the text in capital letter
# lower :- it is used to convert the text in small letter
# title:- it is used to capatalized the first alphabets of text
# capitalize:-convert first alphabets in capital letter

 # upper
# x = "patna"
# x = x.upper(x)
# print(x)

# # lower
# x = "DELHI"
# x = x.lower()
# print(x)

# title

# x = x.title()
# print(x)


# x = "pradeep kumar"
# y = x.title()
# z = x.capitalize()

# print("title:-",y)
# print("title:-",z)

# write a python program to check the text is equal or not
# x = "science"
# y = "scIENCE"
# y = y.lower()  # or
# if x == y:     # or y.lower()
# 	
# 	y = x.upper()
# 	print("yes")
# else:
# 	print("no")

#---------------------------------------------------------

# x = str(input("enter any name:-"))
# x = x.title()
# if x == "Rohit":
# 	print("Yes")

# elif x == "Ranjan":
# 	print("yes")

# else:
# 	print("NO")

#-----------------------------------------------------------

# swapecase :- convert small to capital and capital to small

# x = "SCIence"
# x = x.swapcase()
# print(x)

#----------------------------------------------

#indexing :- it show the position of each alphabet
#slicing :-

#indexing :- it is used to extract the single alphabet from the text
#slicing :- it is used to extract the range of character from the text


# x = "D  E  L  H  I"
#      0  1  2  3  4  :- positive indexing
#      -5 -4 -3 -2 -1  :- negative indexing


# x = "himachal"  with indexing method

# # extract "m" form text
# print(x[2])
# print(x[4])

#x = "Arunachal pradesh"
# 
# print(x[1])
# print(x[4])
# print(x[0])
# print(x[9])
# print(x[6])

# positive indexing
# r
# a
# A
# p
# h

# negative indexing

#e
#s
#d
#p

# print(x[-3])
# print(x[-2])
# print(x[-4])
# print(x[-7])

# x = "arithmatic"     with slicing method
# slicing
# x [starting position : ending position : step_size]
# print(x[0:3])
# mat
# print(x[5:8])
# print(x[0::1])

#x = "himachal pradesh"

# mach
# desh
# him
# mac
# rade

# print(x[2:6])
# print(x[11:0])
# print(x[0:3])
# print(x[2:5])
# print(x[9:13])

# step size
#mca
#hmca
#aap
# print(x[2:7:2])
# print(x[0:7:2])
# print(x[3:10:3])


#negative size

#x = "haryana"

# rya
# na
# arya
# hary

# print(x[-5:-2])
# print(x[-2:])
# print(x[-6:-1])
# print(x[-7:-3])

# x = "I want to become a data scientist"
# lenth = x
# print(x) 

#x = int(input("inter the number:-",1))

		
#x = "Arunachal"

#nac
#rac
#Aaa

#print (x[3:6])
#print(x[1:5:6])


#x = "Delhi"

#output :- ihled

# reverse the text with the help of slicing

#print(x[-1::-1])
       

# x = "Arunachal pradesh"

#  arun x[0:4]
#  anu  x[4:1:-1]
# nac x[3:6]

# can x [5:2:-1]
# pradesh x [-7]

# hsedarp x[-1:-8:-1]
# runa x[1:5]
# Anh x[0:8:3]
# hna x[6::3]
# desh x[-4] .upper()


#---------------------------------------------------------------


# x = "data analyst"
 

# # show the indes of space

# # index() :- it is used to show the position or index of alphabets
# #find()   :- same defination

# a = x.index (" ")
# print("index of space :",a)
# print(f"index of space :{a}")

# x = 10
# y = 20
# z = 30

# x = "data analyst"


# y = x.index("a")
# print("first a :-",y)
# a2 = x.index("a",y+1)
# print("second a :-",a2)
# a3 = x.index("a",a2+1)
# print("third a :-",a3)
# a4 = x.index("a",a3+1)
# print("forth a :-",a4)

#----------------------------------------------------------

#x = "india"

# second value of i

#i2 = x.find("i",x.find("i")+1)
#print(i2)

# x = "data analyst"

# # count total number of the text.

# # count() :-it is used to count the particular
# #alphabet from the text.

# y = x.count("a")
# print("total number of a:-",y)



# x = "Arunachal"
# #1 count total number of a
# y = x.lower()  # arunachal
# print(y.count("a"))

# x = "python is a programming language"

# #2 count total lenth without space
# a = len(x)-x.count(" ")
# print("lenth without space:",a)


# x = "python is a programming language"
# # y = len(x)-x.count(" ")
# # print("lenth without space:-",y)

# #  #3 count total number of a and p

# x = x.upper()
# a = x.count("A") + x.count("p")
# print("total number of a and p:-",a)


# #4 extract the first five alphabet from the text.
# x = x[0:5]
# print("first five alphabet:",a)

# #5 extract the last 3 alphbet from the text.
# b = x[-3:]
# print("last three alphabet:",b)
#-----------------------------------------------------------
#replace :- it is used to replace the value
#         from old text or alphabet to new text or alphabet.

# # split :- it is used to convert the string to list base of 
#   a delimiter

# x = "python is a programming language"
# y = x.split("a")
# print(y)
# print(type(y))


# join :- it is used to convert the list to string



# x = ['python is ', ' a programming language']
# print(x)
# print(type(x))
# print("-"*60)
# y = " ,".join(x)
# print(y)
# print(type(y))



#strip :- it is used to delete the extra space from starting to
#        ending of the text.

# x = "    data science          "
# print(x)
# y = x.strip() # strip ka use krte h extra dot ko htane ke liye
# print(y)



# format :-
# x = "hello {}"
# y = x.format("good morning")
# print(y)


# x ="hii {} my name is {} i am {} old"
# y = x.format("good morning","pradeep",27)
# print(y)

# startswith :- it is used to check the first alphabet from
#               the text

# x = "pradeep"
# y = x.startswith("P")
# print(y)

# x = input()
# if x.startswith("p"):
# 	print("yes")
# else:
# 	print("no")



# write a python program to check if name endswith r and a
# then print the name else print "not found"

# x = str(input("enter any name:-"))
# if x.endswith("r") or x.endswith("a"):
# 	print("x")
# else:
# 	print("not found")



# isupper
# islower
# islower
# isdigit
# x = "10"
# print(x.isdigit())
# # isdecimal

#isalpha()
# x = "pradeep1234"
# print(x.isalpha())

#  isalnum()
# x = "1234"
# print(x.isalnum())

# isspace()
# x = " "
# print(x.isspace())

#  istitle()
# x = "pradeep kumar"
# print(x.istitle())
 
# x = "Data"
# y = x.isupper()
# print(y)

#isdecimal
# x = "1"
# print(x.isdecimal())

#capitalize the first and last alphabet in capital letter.

# x = "india"

# x = x.title()
# print(x)
# a = x[0:-1]	
# b = x[-1] .upper()
# print(a+b)

# x = "brillica"

# # reverse the string
# print(x[-1::-1])

# # print first and last alphabet from the text
#print(x[0]+x[-1])


# # count total number "i"

# y = x.count("i")
# print("total number of i:-",y)


#find the lenth of the text without "i"

# replace    # len

# y = x.replace("i","")
# print(len(y))


#x = "python is an object oriented programming language"


# # reverse this text
# #expected output:-
# #language programming oriented object an is python
#x = x.split(" ")
# a =(x[-1::-1])
# a = " ".join(a)
# print(a)


#write a python program with help of user input to check the text is in capital or not

# x = str(input("enter text:-"))
# print(x)
#write a python program with help of user input to print yes
# if first alphabet of name is upper else print no


# writ a python program with the help of user input to print the first 3 alphabet in
# capital letter
# if lenth of text is greater than 5



# x = str(input("enter text:-"))
# if len(x)>5:
# 	print(x[0:3].upper())



# create a program to print the data type of text or number
#if input is digital then print number
#if input is space then print space
#if input is text then print text
#if input is special charactor then print special charactore 
#    else print none

# x = str(input("enter any text:-"))
# if x.isdigit():
# 	print("number")


# elif x.isspace():
# 	print("space,x")


# elif x.isalpha():
# 	print("Text",x)

# elif x.isalnum():
# 	print("text or number or both",x)
# else:
# 	print("special charactor")


# #2 x = str(input("enter text:-"))
# if x.isupper():
# 	print("yes")
# else:
# 	print("not")
 

# loop :- loop are use to run set of statement.
#      :- block of code



# types of loop

# 1. while loop
# 2. for loop
# 3. nested loop

# while loop :- it is use to iterate the set of statement
#               for infinite time.


# x = 20
# while x>1:
# 	print("hello world")
# 	print(x)
# 	x-=1

#print the name 10 times
# x = 10
# while x>0:
# 	print("pradeep")
# 	x-=1



# x = 10
# y = 0
# while x>y:
# 	print("hello world",y)
# 	y = y+1  # or y+=1

# 1. print the counting from 1 to 50 with the help of while loop

# x = 1
# y = 51
# while x<y:
# 	print(x)
# 	x+=1

# 2. print counting from 10 to 40
# x = 10
# y = 41
# while x<y:
# 	print(x)
# 	x+=1

# 3. print backward counting from 30 to 1
# x = 30
# y = 0
# while x>y:
# 	print(x)
# 	x-=1

# 4. print counting with the help of user input to print the 
#  counting
#x = str(input("enter any number:-"))
# x = 10
# y = 41
# while x<y:
# 	print(x)
# 	x+=1


# print table of 5
# x = 5
# y = 51
# while x<y:
# 	print(x)
# 	x+=5


# x = int(input("enter table name:-")) #10
# y = 1

# while y<11:
# 	print(y*x)
# 	y+=1



# x = int(input("enter table name:-"))
# y = 1
# while y<11:
# 	print(f"{x} x {y} = {x*y}")
# 	y+=1

# 1. print hello world 15 times

# x = 15
# while x>0:
# 	print("hello world")
# 	x-=1


# 2. print counting from 40 to 50
# x = 40
# y = 51
# while x<y:
# 	print(x)
# 	x+=1


# 3. print backward counting from 60 to 40
# x = 60
# y = 40
# while x>y:
# 	print(x)
# 	x-=1

# print 1 to 20 even number

# x = 0
# y = 20
# while x<y:
# 	print("even number:-",x)
# 	x+=2

# 1. even number 30 to 50
# x = 30
# y = 50
# while x<y:
# 	print("even number:-",x)
# 	x+=2

# 2. print all number b/w 1 to 30
# x = 1
# y = 30
# while x<y:
# 	print("all number:-",x)
# 	x+=1

# 3. print all number from 58 to 89 is divisible of 7

# x = 58
# y = 89
# while x<y:
# 	if x%7==0:
# 		print("all number:-",x)
# 	x+=1	


#1 print all number from 1 to 100 who is divisible of 5 and 8
# x = 1
# y = 100
# while x<y:
# 	if x%5==0 and x%8==0:
# 		print("all number:-",x)
# 	x+=1	

#2 print all number from 100 to 200 who is divisible of 10 or 5
 
# x = 100
# y = 200
# while x<y:
#  	if x%10==0 and x%5==0:
#  		print("all number:-",x)
#  	x+=1	
 
#3 print square value from 1 to 10

# x = 1
# y = 11
# while x<y:
# 	print(x,"square:-",x**2)
# 	x+=1

#4 print all even number from 340 to 300

# x = 340
# y = 300
# while x>y:
# 	print("even number:-",x)
# 	x-=2

#------------------------------------------------------------

#1 find the sum of first 10 number 1 to 10
# x = 1
# y = 10
# z = 0
# while x<=y:
# 	z+=1
# 	x+=1
# print("number of sum:-",z)	

#2 find the average of first 5 number
# x = 5
# y = 1
# z = 0
# while x>=y:
# 	z = z+y
# 	y+=1
# avg = z/x
# print("average of first five number:-",avg)	


#3 count total number of even number from 1 to 25
# x = 1
# y = 26
# z = 0
# while x<y:
# 	if x%2==0:
# 		z+=1
# 	x+=1
# print("even number:-",z)

#4 count total number of odd number from 20 to 36
# x = 20
# y = 37
# z = 0
# while x<y:
# 	if x%2==0:
# 		z+=1
# 	x+=1
# print(" total odd number:-",z)


#5 count total number who is divisible of 7 from 1 to 80
# x = 1
# y = 80
# z = 0
# while x<y:
# 	if x%7==0:
# 		z+=1
# 	y+=1	
# print("divisible of 7:-",z)		


# statement

#break:- break statement are use to break the loop
#      according condition
#continue:- it is used to skip the number of text accoording 
#        to condition


# x = 20
# y = 40
# while x>y:
# 	if y==30:
# 		break
# 	print(y)
# 	y+=1

# continue

# x = 10
# y = 1
# while x>=y:
# 	y+=1
# 	if y==4 or y==7:
# 		continue
# 	else:
# 		print(y)


#print number from 50 to 80 and skip 60 to 70

# x = 80
# y = 49
# while x>y:
# 	y+=1
# 	if y>=60 and y<=70:
# 		continue
# 	else:
# 		print(y)
		



 
# for loop:-it is use to run the set of statement.
               # or
#it is use to iterate the block of code

# for variable in range(10):
#print(variable)

# 1 to 20
# for a in range(1,21):
# 	print(a)

#1. print number from 100 to 140
# for a in range(100,141):
# 	print(a)

#2. print backward counting from 20 to 10
# for a in range(-20,-9):
# 	print("backward counting:-",a)

#3. print all even number from 1 to 15
# for a in range(1,15):
# 	if a%2==0:
# 		print("even number:-",a)
	

#4. print all odd number from 25 to 40
# for a in range(25,40):
# 	if a%2==1:
# 		print("odd number:-",a)

#5. print all leap year from 1947 to 2024
# for a in range(1947,2025):
# 	if a%4==0:
# 		print("leap year:",a)


#-------------------------------------------------------------------------------
# for a in range(20,31,2):
# 	print(a)



# x = range(100,49,-1)
# for i in x:
# 	print(i)



# print the number from 10 to 80
#step size should be 5

# for i in range(10,80,5):
# 	print(i)


# count total number of odd number from 1 to 15

# for i in range(1,16):
# 	if i%2==1:
# 		print(i)

# or

# c = 0
# for i in range(1,16):
# 	if i%2==1:
# 		c+=1
# print("total odd number:-",c)		

# write a python program to print the number from 100 to 50 who is divisible of 3 or 7
# and number should even

# for a in range(100,49,-1):
# 	if a%3==0 or a%7==0:
# 		print(a)
				

# for a in range(100,49,-1):
# 	if a%3==0 or a%7==0:
# 		if a%2==0:
# 			print(a)


#       or

# for i in range(100,49,-1):
# 	if (i%3==0 or i%7==0) and i%2==0:
# 		print(i)

#------------------------------------
#text in loop
#--------------------------------

# for i in range(10):
# 	print("hello world")


# x = "Pradeep"
# for i in x:
# 	print(i)

# import time
# x = "pradeep"
# for i in x:
# 	print(i)
# 	time.sleep(1)



# x = "pradeep"
# y = len(x)
# for i in range(y):
# 	print(x[i])


# x = "pradeep"
# z = len(x)
# y = 0
# while z>y:
# 	print(x[y])
# 	y+=1


#print the number from 20 to 40 and break number when number is 30
              
# x = 20
# y = 40
# while x<y:
# 	if x==30:
# 		break
# 	print(x)
# 	x+=1

#      or

# for i in range(20,40):
# 	print(i)
# 	if i==30:
# 		break
	


# print counting from 1 to 10
#but print the number in horizontally.

# for i in range(1,11):
# 	print(i,end="--")

# to print the horizontally

# x = "pradeep"
# for i in x:
# 	print(x)  


# show the each alphabet from the text
# x = "rohit sharma"
# for i in range(len(x)):
# 	print(x[i]," : ",i)


# show the index number of each alphabet from the text in
# negative index
# x = "rohit sharma"
# y = len(x)
# for i in range(y):
# 	print(x[i]," negative index :  ",i-y)


#             or 
# while loop

# x = "rohit sharma"
# y = len(x)
# z = 0
# while y>z:
# 	print(x[z]," : ",z-y)
# 	z+=1  

# x = "programming123"
# extract all number from text
# extract all alphabet from the text

# isdigit()
# for i in x:
# 	if i.isdigit():
# 		print(i)

# isalpha()
# for a in x:
# 	if a.isalpha():
# 		print(a)


# x = "programming123"
# y = ""
# for i in x:
# 	if i.isdigit():
# 		print(i)
# 		y = y+i

# print(y)
# print(type(y))
# y = int(y)
# print(y)
# print(type(y))


# x = "prog3r4a5m6ming123"
# y = 0
# for i in x:
# 	if i.isdigit():
# 		y = y+1
# print(y)		


# x ="prog3r4a5m6ming123" #(show the total number of digit)
# y = 0
# for a in x:
# 	if a.isdigit():
# 		y = y+1
# print(y)		



# x ="prog3r4a5m6ming123" #(show the total number of alphabet)
# y = 0
# for a in x:
# 	if a.isalpha():
# 		y = y+1
# print(y)		



# find the factorial with the help of user input

# x = int(input("enter any number:-"))
# fact = 1
# for a in range(1,x+1):
# 	fact = fact*a
# print(f"factorial of {x} is :{fact}",)	


# while loop

# x = int(input("enter any number:-"))
# fact = 1
# y = 1
# while x>=y:
# 	fact*=y
# 	y+=1
# print("factorial :",fact)	


# reverse the text with the help of while loop
# x = "Brillica"
# y = len(x)-1  #8
# while y>=0:
# 	print(x[y],end=" ")
# 	y-=1


# for loop
# x = "Brillica"
# y = len(x)-1
# for a in range(y,-1,-1,):
# 	print(x[a])

#x = "princekr301@gmail.com"
     
#count total number of alphabet
# c = 0
# for a in x:
# 	c+=1
# print(c)
	

# print all special charactor
# for a in x:
# 	if a.isalnum():
# 		continue
# 	else:
# 		print(a)
		
# extract all alphabet from the text
# for a in x:
# 	if a.isalpha():
# 		print(a)
	
#print all alphabet before the g
# for a in x:
# 	if a.isalpha():
# 		if a=="g":
# 			break
# 		else:
# 			print(a)
		
					
#count all special charactor
# c= 0
# for a in x:
# 	if a.isalnum():
# 		continue
# 	else:
# 		c+=1
# print("total number of special charactor:",c)		
		
#--------------------------------------------------------------
#x = "ramayana"
# ptint all "a" from the text
# for a in x:
# 	if a=="a":
# 		print(a)



#count total number of a
# c = 0
# for a in x:
# 	c+=1
# print(c)	

# print A and R from the text

# for a in x:
# 	if a=="a" or a=="r":
# 		print(a)

#x = "programming"
#1 extraxt all vowel alphabet
# a= {"a","e","i","o","u" }
# for a in x:
# 	if a in "aeiou":
# 		print(i)

# print all repeated words
# x = "programming"
# for a in x:
# 	if x.count(a)>1:
# 		print(a)

# print all even index of value from text

# x = "programming"
# y = len(x)
# for a in range(y):
# 	if a%2==0:
# 		print(x[a],end = " ")



# print the only capital letter
# x = "PrinceKR"
# for a in x:
# 	if a.isupper():
# 		print(a)



# 1 to 20 square
# for a in range(1,21):
# 	print(a,"square: ",a*a)


#1 to 20 cube
# for a in range(1,21):
# 	print(a,"cube:",a**3)


# find the average of first 10 number
# s = 0
# for a in range(1,11):
# 	s = s+1
# print("sum:-",s)
# avg = s/a
# print("sum of 10 number:-",s)
# print("total number:",a)
# print("average:-",avg)

# find the number of first 10 number
# s = 0
# for a in range(1,11):
# 	s +=1
# print("sum:-",s)
# print("sum of 10 number:-",s)
# print("total number:-", a)

# find the average of first 10 number
# s = 0
# for a in (1,11):
# 	s+=1
# 	avg = s/a
# 	print("average:-",avg)
	
# x = "p34ert345j4j34534j"   # find the total sum
# s = 0
# for a in x:
# 	if a.isdigit():
# 		a = int(a)
# 		s = s + a
# print(s)
		
		


# a = 343453454
# b = "prderer"

# x = "p34ert345j4j34534j"
# a = ""
# b = ""
# for i in x:
# 	if i.isdigit():
# 		a = a+i
# 	elif i.isalpha():
# 		b = b+i	
# print(a)
# print(b)			

#         OR

# x = "p34ert345j4j34534j"
# a = ""
# b = ""
# for i in x:
# 	if i.isdigit():
# 		a = a+i
# 	else:
# 		i.isalpha()
# 		b = b+i
# print(a)
# print(b)		



#-------------------------------------------------------
#-------------list ----------------------------------
#------------------------------------------------------

# list "sequence data" type me aata h


# list: list always written in square bracket
#              or
# list are used to store the multiple value in a single variable.

# main uses of list

# 1.list are ordered.
# 2. list are changable or mutable.
# 3. list are indexed( show position).
# 4. list allow duplicate value.
# 5. list written square bracket.
# 6. here u can store the multiple type of data.

#--------------------------------------------------------------------

# x = [100,"friday",78.23,45j,True,None,200,855]
# print("list:",x)
# print("data type:",type(x))
# print("lenth of list:",len(x))


# string the dublicate value
# x = [45,45,45,45,45,45,]
# print(x)


# list manipulation
# x = ["sunday" ,"monday","tuesday","wednesday","thursday","friday","saturday"]
# print(x)

# 1. pop :- it is used to delete the value from the list with the
#            the help of indexing and by default delete the last
#            value from the list.

# x.pop()         # delete the last value
# x.pop(2)
# print(x)

# 2. remove: its delete the value from the list.
# x.remove("sunday")
# print(x)

# x = ["sunday" ,"monday","tuesday","wednesday","thursday","friday","saturday"]
# x.remove("sunday")
# print(x)


# x = [12,45,78,12,55,45]
# x.remove(12)  # delete 12 from list
# print(x)


# 3.clear :- its delete all values from the list
# x = ["pradeep",78,456,56,38,89,23,]
# print("before----------")
# print(x)
# x.clear()
# # print("after----------")
# print(x)


# 4.del : del is a keyword that is used to delete the value according
#          to index and variable.

# x = [45,78,89,56,23,23]
# del x[-1]      # indexing
# del x[0:3]      # slicing  [with step size method]
# print(x)


#---------------------------------------------------------


# x = [12,45,78,"fri",89,8,"thu",56,62,3,32,"sun"]

# 1. delete the last value with the help of pop
# x.pop()
# print(x)

# 2. delete "Fri" with remove
# x.remove("fri")
# print(x)

# 3. delete first three elements
# x.remove(12)
# x.remove(45)
# x.remove(78)
# print(x)

# 4. delete  all values from list
# x.remove(12)
# x.remove(45)
# x.remove(78)
# x.remove(89)
# x.remove(8)
# x.remove(56)
# x.remove(62)
# x.remove(3)
# x.remove(32)
# print(x)

# 5. delete variabel of list 
# x.remove("fri")
# x.remove("thu")
# x.remove("sun")
# print(x)
#----------------------------------------------------------
# how to add the value

# 1. insert :- it is use to add the value according to index number
# 2. append :- it is use to add the value
# 3. extend :- it is use to add the multiple value in a list

# x =[12,45,78,89,23,23]
# x.insert(2,"pradeep")
# x.insert(0,250)
# print(x)



# x =[12,45,78,89,23,23]
# x.append("ram")
# x.append(4564)
# print(x)



# x = [1,2,3,4,5]
# y = [4,5,6,7,8]
# x.extend(y)
# print(x)

# x = ["virat","rohit","anikul","rakesh"]
# # create a new list and add all value of x and convert
#   in capital letter
# y = []
# for a in x:
# 	print(a.upper())
# 	y.append(a)
# print(y)	

# y = []
# for a in range(1,11):
# 	y.append(a)
# print(y)	

#------------------------------------------------------------


# x = [45,78,89,56,12,25,47,69,10]
# 1. delete third value
# x.remove(56)
# print(x)

# 2. add 200 in 2nd value
# x.insert(2,200)
# print(x)

# 3. add 500 in last of list
# y = x.append(500)
# print(x)

# 4 . delete 4th and 5 th position of value
# x.remove(12)
# x.remove(25)
# print(x)

# 5. add[1,1,1] in list
# y = x.append([1,1,1])
# print(x)

# 6. add "python" last of list
# y = x.append("python")
# print(x)

# 7. delete 89 from list
# x.remove(89)
# print(x)

#---------------------------------------------------------


#x = [45,78,89,56,253,23] # extract the value with the help of slicing

#1. 253
#2. [45,78]
#3. [23,253]
#4. [89,78,45]
#5. [56,89]

#1.print(x[-2])

#2.print(x[0:2])
#3.print(x[-1:-3:-1])
#4.print(x[2::-1])
#5.print(x[3:1:-1])

#x = [45,78,89,56,23,20,100]

# output = [20,23,45,56,78,89,100]
#-------------------------------------------------------
# sort() :- it is use to arrange the data in ascending or
#           decending order.


# sorted:-it is use to arrange the data in ascending or
#           decending order.


#x = [45,78,89,56,23,20,100]

# ascending order:-

# x.sort()
# print(x)


# descending order:-

# x.sort(reverse=True)
# print(x)

#x = [45,78,89,56,23,20,100]

# ascending order
# y = sorted(x)
# print(y)



# descending order
# y = sorted(x,reverse=True)
# print(y)

# x = [45,89,56,25,41,10,96,35,78]


#1.arrange the data in ascending order
# x.sort()
# print(x)

#2.extract maxium value  from the list
#x.sor()
#print(x[-1])

#3. extract the minimum value from the list.
#x.sort()
#print(x[0])

#4. find the second highest value from the list.
#x.sort()
#print(x[-2])

#5. show the second lowest value from the list.
# x.sort()
# print(x[1])

#6 show the top 3 value from the list
# x.sort()
# print(x[-1:-4:-1])

#7 show the bottom 3 number from the list
# x.sort(reverse=True)
# print(x[-3:])

#x = [45,89,56,25,41,10,96,35,78]

# max:- its extract maximum value from the list.
#print(max(x))

# min:- its extract minimum value from the list.
#print(min(x))


#-------------------------------------------------------------

# reverse
# count
# index
# copy


# x = ["sunday","monday","tuesday","wednesday","thursday","friday","saturady","sunday"]
# x.sort()
# print(x)



# reverse:- it is use to reverse the list.

# x = [12,85,20,100]
# x.reverse()
# print(x)

# count:- it is use to count the value from the list.

#Q. count total number of 12
# x = [12,45,78,89,56,12,45,12]
# a =  x.count(12)
# print(a)

# index:- it is show the index number of any value in list.
# b =  x.index(78)
# print(b)


# copy:- it is use to copy the list.

# x = [12,45,78,89,23]
# y = x.copy()
# x.clear()
# print(y)
# print(x)


x = [12,45,78,89, 65,23,10]

# 1. extract all even value from the list.
for a in x:
	if a%2==0:
		print(a)

#2. extract all odd number from the list.
# for a in x:
# 	if a%2==1:
# 		print(a)

#3. create a blank list and add all even number from x
# y = []
# for a in x:
# 	if a%2==0:
# 		y.append(a)
# print(y)

#4. create a blank list and all odd number from x
# y = []
# for a in x:
# 	if a%2==1:
# 		y.append(a)
# print(y)

# x = [12,45,78,12,12,12]
#1. delete from the list
# for a in x:
# 	if a==12:
# 		x.remove(a)
# print(x)


# while 12 in x:
# 	x.remove(12)
# print(x)

#2. delete even number from the list.
# for a in x:
# 	if a%2==0:

#3. delete odd number from the list.


#--------------------------------------------------------------


#nested list:-when one list use inside the another list
#              it is called nested list.

# x = [12,45,78,[1,2,3],100,200]
# print(x)
# print(type(x))
# print(len(x))


# x = [[1,2,3],[4,5,6],[7,8,9]]
#print(len(x))

# indeexing
#2
# print(x[0][1])
#1
# print(x[0][0])
#5
# print(x[1][1])
#9
# print(x[2][2])
#7
# print(x[2][0])
#8
# print(x[2][1])


# x = [[12,45,78,[100,200,300]]]
# print(len(x))

#1.Extract 
# 300
#2. print(x[0][3][-1])
# 78

#3. print(x[0][2])
# 12

#4. print(x[0][0])
# 45

#. print(x[0][1])

#5. 200

# print(x[0][3][-2])


