# for, while
#continue, break

# value = 0

# while value < 10:
#     if value == 5:
#        value = value + 1
#        continue
#     print(value)
#     value = value + 1

sample = ["server1", "server2", "server3", "server4", 123]

# idx = 0

# while idx < len(sample):
#     print(sample[idx])
#     idx = idx + 1

## in membership operator (check if a value is present in a list or not)
# print("1" in sample) # False
# print("server1" in sample) # True

## idx -> is Iterator variable
## sample -> is Iteratorable variable
# for ele in sample:
#     print(ele)
# print("ele")

## Access elements inside the list using index using for loop
## range -> enumerate
# print(list(range(5))) # 0,1,2,3,4

# for idx in range(len(sample)):
#     ele = sample[idx]
#     print(idx, ele)
print (enumerate(sample)) # <enumerate object at 0x7f8c8c8c8c8> 
for idx, val in enumerate(sample):
    print(idx,val)

## tuple unpacking
# a, b = (1, 2)
# print(a, b)