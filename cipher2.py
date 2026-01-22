#new version of the cipher that hopefully is mor accurate 
# to what MIT requests in their course

def encode (phrase, shift):
    cipher = ""
    #encode each letter in the message
    for char in phrase:
        #keep non letters the same in the message (Spaces, exclamations, numbers)
        if char.isalpha() == True:
            #Starting point depending on upper or lower letter
            start = ord("A") if char.isupper() else ord("a")
            #the real magic, took me quite a while to get this working
            new_letter = chr(start + (ord(char) - start + shift) %26)
            cipher = cipher + new_letter
        else:
            cipher = cipher + char
    return  cipher 

print ("This program will encript a phrase using simple cycle ciphering")
print("")

#asking user for parameters (phrase and shift value)
phrase = str(input("enter a phrase to encode: "))
shift = int(input ("Enter shift Value: ")) 
#show results
print("Encoded phrase is: ", encode(phrase, shift))
