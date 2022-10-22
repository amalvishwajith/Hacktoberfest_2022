from collections import Counter
counter1 =  Counter({'x': 4, 'y': 2, 'z': -2})

counter2 = Counter({'x1': -12, 'y': 5, 'z':4 })

#Addition
counter3 = counter1 + counter2
# only the values that are positive will be returned.

print(counter3)

#Subtraction
counter4 = counter1 - counter2
# all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output

print(counter4)

#Intersection
counter5 = counter1 & counter2
# it will give all common positive minimum values from counter1 and counter2

print(counter5)

#Union
counter6 = counter1 | counter2
# it will give positive max values from counter1 and counter2

print(counter6)