def answer(l, t):

    result = []
    target = int(t)
    
    for key, value in enumerate(l):
        # first loop, use the whole list here
        if key == 0:
            # loop list n times where n = length of the list
            for index, value in enumerate(l):
                slice = l[:index+1]
                # if the sum of the slice is equal to our target append index values to result and return
                if sum(slice) == target:
                    length = len(slice)
                    result.append(key)
                    result.append(key + length - 1)
                    return result
                # otherwise break out of the loop
                elif sum(slice) > target:
                    break
                    
        # slice the list from the key to the end
        else:
            list_slice = l[key:]
            # loop list n times where n = length of the list_slice
            for index, value in enumerate(list_slice):
                slice = list_slice[:index+1]
                if sum(slice) == target:
                    length = len(slice)
                    result.append(key)
                    result.append(key + length - 1)
                    return result
                elif sum(slice) > target:
                    break

    if not result:
        index = [-1, -1]
        return index

print(answer([1, 3, 1, 2, 15, 3], 15))
