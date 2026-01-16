# trying to implement a cyclic cipher 
new_phrase =""
print ("This program will encript a phrase using simple cycle ciphering")
print("")
phrase = str (input("enter a phrase to encode: "))
shift = int (input ("Enter shift Value: "))
for i in range (0 , len(phrase)):
    #converts a letter to ascii code
    ascii_code = ord(phrase[i])
    new_ascii = ascii_code + shift
    new_letter = chr(new_ascii)
    new_phrase = new_phrase + new_letter
print ("the new phrase is", new_phrase)

#I think this works better that I intended 
# (first version, it uses the whole ASCII table)
# it ciphers with a shift number (x) and deciphers with the negative (-x)





 