
# squre = lambda x: x**2
# print(squre(5))

# add = lambda x,y: x+y
# print(add(50,20))

list1 = [1,2,3,4,5,6,7]
print(list(map(lambda x : x**2, list1)))

num = lambda x: "Even" if x%2==0 else "odd"
print(num(5))
print(list(map(lambda x: "Even" if x%2==0 else "odd", list1)))

print(list(filter(lambda x: x%2!=0, list1)))
