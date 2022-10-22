from collections import Counter
counter1 =  Counter({'x': 5, 'y': 3, 'z': -7})

counter2 = Counter({'x1': -16, 'y': 7, 'z':9 })

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