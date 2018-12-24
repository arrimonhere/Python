# Calculator With Function
# Code By Ar Rimon Ahmed

# Function For Addition

def Addition(x,y) :
  return x+y

# Function For Substraction

def Substraction(x,y) :
  return x-y

# Function For Multliplication

def Multliplication(x,y) :
  return x*y

# Function For Division 

def Division(x,y) :
  return x/y

# Function For Square 

def Square(x) :
  return x**2

# Function For Cube 

def Cube(x) :
  return x**3

print("For Addition Enter : +\nFor Substraction : -\nFor Multliplication : *\nFor Division : /\n For Square : ^\nAnd For Cube : @")

Choose=input("\nEnter Your Choice (+,-,* or /) : ")

# Condition For Addition

if Choose=="+" :
  print("\nWelcome \nYou Decided To Do Addition Of Two Number.\n")
  num1=int(input("Enter First Number : "))
  num2=int(input("Enter Second Number : "))

  print("\nThe Addition Of Two Number Is : ",num1,"+",num2,"=", Addition(num1,num2))


# Condition For Substraction

elif Choose=="-" :
  print("\nWelcome \nYou Decided To Do Substraction Of Two Number.\n")
  num1=int(input("Enter First Number : "))
  num2=int(input("Enter Second Number : "))

  print("\nThe Substraction Of Two Number Is : ",num1,"-",num2,"=", Substraction(num1,num2))


# Condition For Multliplication

elif Choose=="*" :
  print("\nWelcome \nYou Decided To Do Multliplication Of Two Number.\n")
  num1=int(input("Enter First Number : "))
  num2=int(input("Enter Second Number : "))

  print("\nThe Multliplication Of Two Number Is : ",num1,"*",num2,"=", Multliplication(num1,num2))


# Condition For Division

elif Choose=="/" :
  print("\nWelcome \nYou Decided To Do Division Of Two Number.\n")
  num1=int(input("Enter First Number : "))
  num2=int(input("Enter Second Number : "))

  print("\nThe Substraction Of Two Number Is : ",num1,"/",num2,"=", Division(num1,num2))


# Condition For Square

elif Choose=="^" :
  print("\nWelcome \nYou Decided To Do Square Of A Number.\n")
  num1=int(input("Enter Any Number : "))

  print("\nThe Square Of Your Number Is : ",num1,"*",num1,"=", Square(num1))


# Condition For Cube

elif Choose=="@" :
  print("\nWelcome \nYou Decided To Do Cube Of A Number.\n")
  num1=int(input("Enter Any Number : "))

  print("\nThe Cube Of Your Number Is : ",num1,"*",num1,"*",num1,"=", Cube(num1))


# Condition If Don't Understand One Desicion

else :
  print("\nSorry \nWe Cannot Understand Your Desicion.\n")
  print("Please Try Again, With Correct Desicion.")