# Height and mone checker for a rollercoaster

print("Ojo que tenes que se mayor a 137 cms de altura y tener mas de 10 creditos")
altura = int(input("Ingrese altura: "))
credito = int(input("cuantos creditos?: "))

if altura >= 137 and credito >= 10:
    print("pase nomas")
elif altura < 137 and credito >= 10:
    print("te alcanza pero sos petiso")
elif altura >= 137 and credito < 10:
    print ("sos alto pero pobre")
else: print("sos petiso y necima pobre")