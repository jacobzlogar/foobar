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
    total = xrange(len(l))
    start_index = 0

    for _ in (total - start_index):
        if start_index == 0:
            slice = l[:]
            print(xrange(len(slice)))
            for i in xrange(len(slice)):
                result = slice[:i+1]
                print(result)
                if sum(result) == target:
                    print('bing')
                if sum(result) > target:
                    break
            start_index += 1
        else:
            slice = l[start_index:]
            print(xrange(len(slice)))
            for i in xrange(len(slice)):
                print(slice[:i])
            start_index += 1

answer([4, 3, 10, 2, 8],12)

