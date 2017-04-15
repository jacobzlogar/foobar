# Int List l, Int t
# Int List
# answer(l, t)
# find values where l == t
# find a contiguous substr where values of l == t
# if more than one , return value with lowest lexicographically sorted indices
# i.e. of the following substr indice values " [3,6], [0,2], [1,4] [0,1] " [0,1] would be returned 
# since [0+1] < any of the other combinations of indice values
# HOWEVER indice values that have a greater starting value than ending value will be discarded
# i.e [2, 0]
# if none exist return Int List [-1, -1]

# l always >= 1 never > 100
# elements of l consist of 1:100
# t positive int, never > 250
# first element of l will have index 0 ?



def answer(l, t):
    result = []
    target = int(t)
    for x in range(len(l)):
        slice = l[:x+1]
        if sum(slice) == target:
            end_index = x + len(slice) - 1 
            result.append(x)
            result.append(end_index)
            result.append(slice)
        elif sum(slice) >= t:
            return
        for y in range(len(l)):
            slice = l[x+1:]
            print(slice)

answer([4,3,5,7,8],12)

