def divide_the_cake(string):
    result = []
    for index in range(len(string)):
        substr = string[0:index+1]
        count = string.count(substr)
        value = substr * count
        if value == string:
            result.append(count)
    if len(result) > 1:
        output = max(result)
        return output
    # 
    elif len(result) == 0:
        output = result[0]
        return
    else:
        return

def answer(s):
    if s and len(s) < 200:
        return divide_the_cake(s)
    else:
        return

# print(answer('abcabcabcabc'))
