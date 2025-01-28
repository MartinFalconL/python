import random
question = input("Ask the magic 8 ball a question: ")
answers = random.randint(1, 8)
if answers == 1:
    print("It is certain")
elif answers == 2:
    print("Outlook good")
elif answers == 3:
    print("You may rely on it")
elif answers == 4:
    print("Ask again later")    
elif answers == 5:  
    print("Concentrate and ask again")
elif answers == 6:
    print("Reply hazy, try again")
elif answers == 7:
    print("My reply is no") 
elif answers == 8:
    print("My sources say no")  
else:
    print("Invalid question")
# The program will randomly select a number between 1 and 8 and then print the corresponding answer.
# The program will print "Invalid question" if the user does not ask a question.
# The program will print "Ask again later" if the number 4 is selected.
# The program will print "My reply is no" if the number 7 is selected.
# The program will print "My sources say no" if the number 8 is selected.
# The program will print "It is certain" if the number 1 is selected.
# The program will print "Outlook good" if the number 2 is selected.
# The program will print "You may rely on it" if the number 3 is selected.
# The program will print "Concentrate and ask again" if the number 5 is selected.
# The program will print "Reply hazy, try again" if the number 6 is selected.
# The program will print "Invalid question" if the user does not ask a question.
# The program will print "Ask again later" if the number 4 is selected.
# The program will print "My reply is no" if the number 7 is selected.
# The program will print "My sources say no" if the number 8 is selected.