def answer(l, t):

    result = []
    target = int(t)

    for key, value in enumerate(l):
        if key == 0:
            slice = l[:]
            for index, value in enumerate(slice):
                output = slice[:index+1]
                if sum(output) == target:
                    result.append(output)
        else:
            slice = l[key:]
            for index, value in enumerate(slice):
                output = slice[:index+1]
                if sum(output) == target:
                    result.append(output)

    if result:
        index = []
        for x in result:
            for y in x:
                index.append(l.index(y))
        return index
    else:
        index = [-1,-1]
        return index

answer([4, 3, 10, 2, 8],12)

