ex_1 = [1,2,3,4,5]
ex_2 = [2,4,6,8,10]

f = lambda x, y: x+y
print(list(map(f,ex_1,ex_2)))

result = map(lambda x: x**2 if x % 2 == 0 else x, ex_1)

print(type(result))
print(result)

result = list(result)
print(type(result))
print(result)

print("-------------------")
f = lambda x : x**2

print(map(f, ex_1))

for i in map(f, ex_1):
    print(i, end=" ")
print("")
result = map(f, ex_1)
print(result)
print(next(result))
