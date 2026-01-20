# trying to implement a cyclic cipher 
new_phrase ="" #initializes as string
print ("This program will encript a phrase using simple cycle ciphering")
print("")

#asking user for parameters (phrase and shift value)
phrase = str (input("enter a phrase to encode: "))
shift = int (input ("Enter shift Value: "))

for i in range (0 , len(phrase)):

    #converts a letter to ascii code
    ascii_code = ord(phrase[i])

    #shifts the caracter with the shifting value given
    new_ascii = ascii_code + shift

    #converts back to characters
    new_letter = chr(new_ascii)

    #creates new phrase
    new_phrase = new_phrase + new_letter
#prints result    
print ("the new phrase is", new_phrase)

#I think this works better that I intended 
# (first version, it uses the whole ASCII table)
# it ciphers with a shift number (x) and deciphers with the negative (-x)





 