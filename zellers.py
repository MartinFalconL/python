#trying to implement Zellers algorithm to get the day given a sepcific date
dia = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
vorname = (input ("Enter your first name: "))
nachname = (input ("Enter your last name: "))
print ("enter your birth date (all in numbers please): ")
month = int (input ("Month?: "))
day = int (input ("day?: "))
jahre = int (input ("year?: "))
jahre = divmod (jahre, 100)
year =[jahre[0], jahre[1]]
month = (month - 2 )

# Only way I found at this point was to repeat al the calculations inside each "IF"

if (month == -1):
    year[1] = year[1] - 1
    month = 11
    w = ((13* month) - 1) // 5 
    x = (year[0] // 4) 
    y = (year[1] // 4) 
    z = w + x + y + day + year[1] - (year[0] * 2 )
    r =  z % 7
    print (vorname, nachname, "was born on ", dia[r])
elif (month == 0):
    year[1] = year[1] - 1
    month = 12
    w = ((13* month) - 1) // 5 
    x = (year[0] // 4) 
    y = (year[1] // 4) 
    z = w + x + y + day + year[1] - (year[0] * 2 )
    r =  z % 7
    print (vorname, nachname, "was born on ", dia[r])
else:    
    w = ((13* month) - 1) // 5 
    x = (year[0] // 4) 
    y = (year[1] // 4) 
    z = w + x + y + day + year[1] - (year[0] * 2 )
    r =  z % 7
    print (vorname, nachname, "was born on ", dia[r])
    