# First Version (before learning countdown was available)
#bottles = 99
#for i in range (99):
#  print(f'{bottles-i} bottles of beer on the wall')
#  print(f'{bottles-i} bottles of beer')
#  print('Take one down, pass it around')
#  print(f'{bottles-(i+1)} bottles of beer on the wall')
#---------------------------------------------------------

# now with the whole information: 

for i in range(99, 0, -1):
    print(f'{i} Bottles of beer on the wall')
    print(f'{i} Bottels of beer')
    print('Take one down, pass it around')
    print(f'{i-1} Bottles of beer on the wall')