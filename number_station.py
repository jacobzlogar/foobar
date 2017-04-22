# Given a non-empty list of positive integers l and a target positive integer t, write a function answer(l, t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).
# 
# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function answer(l, t) would return the list [0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function answer(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15. To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards:
# 
# Each list l will contain at least 1 element but never more than 100.
# Each element of l will be between 1 and 100.
# t will be a positive integer, not exceeding 250.
# The first element of the list l has index 0.
# For the list returned by answer(l, t), the start index must be equal or smaller than the end index.
# Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist of a number broadcast that can be summed up to the key. You know that the message will always be hidden in the first sublist that sums up to the key, so answer(l, t) should only return that sublist.
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
