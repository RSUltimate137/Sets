#a set is a collection of unique items
fruits = {"apple","banana","grapes","apple"}
print(fruits)

a = {1,2,3,4}
b = {2,4,6,8}

# print(A | B)   # union
# print(A & B)   # intersection
# print(A - B)   # difference
# print(A ^ B)   # symmetric difference

#union
combine = a.union(b)
print(combine)

#intersection
common = a.intersection(b)
print(common)

#difference
unique = a.difference(b)
print(unique)
unique1 = b.difference(a)
print(unique1)

#symetric_difference
unique2 = a.symmetric_difference(b)
print(unique2)
unique3 = b.symmetric_difference(a)
print(unique3)