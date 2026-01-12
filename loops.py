# learning about loops
# prints the result of 1/i from 1 to 10

#for i in range (1, 11):
#    x = 1/ i 
#    print (f'1/ {i} =' , x)

#--------------------------------------
# prints countdown from a given number up to zero

#countdown = int(input("type a staring countdown number:"))
#while (countdown < 0):
#    countdown = int(input("please type a number over zero:"))
#for i in range (countdown, -1, -1):
#       print (i)

#----------------------------------------
#another way 
#countdown = int(input("type a staring countdown number:"))
#while (countdown < 0):
#    countdown = int(input("please type a number over zero:"))
#while (countdown > -1):
#    print (countdown)
#    countdown -= 1

#----------------------------------------
#calculate exponentials using "for" (no validations, trusting user)
#base = int(input("enter base number:"))
#exp = int(input("enter exponential:"))
#x = base
#if (exp != 0):
#    for i in range (1, exp):
#        x = x * base
#    print ("the result is", x)
#else: print("the result is 1")

#----------------------------------------
#ask for a number and keep asking until the number is divisible by 2

num = int (input ("Enter a number:"))
while (num % 2 != 0):
        num = int (input ("Enter a CORRECT number:"))
print ("Good work!! You finally got it! :p")
