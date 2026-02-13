#------Practice IF ELSE:
gen = input("Enter your gender : M/F: ")
if gen == 'M' or gen =='m':
  print("Good morning SIR")
elif gen =='F' or gen =='f':
  print("Good morning MAM")

else:
  print("Unidentified gender")

#-----Loops Concept

# lets print a table of 5
for i in range(5,51,5):
  print(i)

#------Sum of Numbers
n = int(input("Enter the number:"))
sum = 0

for i in range(1,n+1):
  sum = sum + i
  
print(f"Your sum is {sum}")

#---------Factorial of a number

n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
  fact=fact*i
print(f"The factorial is: {fact}")

# --------Sum of even and odd numbers

n=int(input('Enter your number:'))
even=0
odd=0
for i in range(1,n+1):
  if i%2 == 0:
    even=even+i
  else:
    odd=odd+i

# print(f"your even and odd sum are {even}, {odd}")


#---------Print all the factors of the number

n=int(input("Enter your number"))
fact=1
for i in range(1,n+1):
  if n%i == 0:
   print(i)

sum=0
n=int(input("Enter your number is perfect or not :-"))
for i in range(1,n):
  if n%i == 0:
    sum=sum+i

if sum == n:
  print("Your number is perfect")
  
else:
  print("not a perfect number")


    


