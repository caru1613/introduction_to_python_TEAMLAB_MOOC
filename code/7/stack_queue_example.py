#word = input("Input a word: ")
#world_list = list(word)
#print(world_list)

#result = []
#for _ in range(len(world_list)):
#    result.append(world_list.pop())
#print(result)
#print(word[::-1])

word = input("Input a word: ")
print(word)

world_list_stack = list(word)
world_list_queue = list(word)
print(world_list_stack)
print(world_list_queue)

print("---------------------------")
result_stack = []
result_queue = []
for _ in range(len(world_list_stack)):
    result_stack.append(world_list_stack.pop())
for _ in range(len(world_list_queue)):
    result_queue.append(world_list_queue.pop(0))
print(world_list_stack)
print(world_list_queue)
print(result_stack)
print(result_queue)
print(word[::-1])

