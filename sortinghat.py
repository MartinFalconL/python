# Harry Potter's Sorting Hat
Ravenclaw = 0
Gryffindor = 0
Hufflepuff = 0
Slytherin = 0

name = str(input("What is your name Little one?: "))

print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
ans = int(input("Enter your Answer"))

if ans == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif ans == 2:
  Hufflepuff += 1
  Slytherin += 1
else: 
  print ("Wrong Answer")

print("Q2) Which kind of instrument you like?")
print("1) Violin")
print("2) Trumpet")
print("3) Piano")
print("4) Drums")
ans = int(input("What is your answer? "))

if ans == 1:
   Slytherin += 4
elif ans == 2:
  Hufflepuff += 4
elif ans == 3:
  Ravenclaw += 4
elif ans == 4:
  Gryffindor += 4
else:
  print ("Wrong Answer")

print("Q3) When dead, you want to be remembered as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
ans = int(input("What is your answer? "))

if ans == 1:
   Hufflepuff += 2
elif ans == 2:
  Slytherin += 2
elif ans == 3:
  Ravenclaw += 2
elif ans == 4:
  Gryffindor += 2
else:
  print ("Wrong Answer")

print (name), print("Your score for each house is: ")
print ("Gryffindor:"), print(Gryffindor)
print ("Hufflepuff:"), print(Hufflepuff)
print ("Ravenclaw:"), print (Ravenclaw)
print ("Slytherin:"), print (Slytherin)