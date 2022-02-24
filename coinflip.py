from random import choices
import random


# sides =[]
# for i in range(6000):
#     sides.extend(choices(['Side', 'Head', 'Tails'], weights=[1/6000, 2999.5/6000, 2999.5/6000]))
sides = choices(['Side', 'Head', 'Tails'], weights=[1/6000, 2999.5/6000, 2999.5/6000], k=6000)
    

print(f"Heads: {sides.count('Head')}")
print(f"Tails: {sides.count('Tails')}")
print(f"Sides: {sides.count('Side')}")

   



    

