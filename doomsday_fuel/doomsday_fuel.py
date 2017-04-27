# Doomsday Fuel =======
# 
# Making fuel for the LAMBCHOP's reactor core is a tricky process because of the
# exotic matter involved.  It starts as raw ore, then during processing, begins
# randomly changing between forms, eventually reaching a stable form. There may
# be multiple stable forms that a sample could ultimately reach, not all of
# which are useful as fuel. 
# 
# Commander Lambda has tasked you to help the scientists increase fuel creation
# efficiency by predicting the end state of a given ore sample. You have
# carefully studied the different structures that the ore can take and which
# transitions it undergoes. It appears that, while random, the probability of
# each structure transforming is fixed. That is, each time the ore is in 1
# state, it has the same probabilities of entering the next state (which might
# be the same state).  You have recorded the observed transitions in a matrix.
# The others in the lab have hypothesized more exotic forms that the ore can
# become, but you haven't seen all of them.
# 
# Write a function answer(m) that takes an array of array of nonnegative ints
# representing how many times that state has gone to the next state and return
# an array of ints for each terminal state giving the exact probabilities of
# each terminal state, represented as the numerator for each state, then the
# denominator for all of them at the end and in simplest form.  The matrix is at
# most 10 by 10. It is guaranteed that no matter which state the ore is in,
# there is a path from that state to a terminal state. That is, the processing
# will always eventually end in a stable state. The ore starts in state 0.  The
# denominator will fit within a signed 32-bit integer during the calculation, as
# long as the fraction is simplified regularly. 
# 
# For example, consider the matrix m: [ [0,1,0,0,0,1],  # s0, the initial state,
# goes to s1 and s5 with equal probability [4,0,0,3,2,0],  # s1 can become s0,
# s3, or s4, but with different probabilities [0,0,0,0,0,0],  # s2 is terminal,
# and unreachable (never observed in practice) [0,0,0,0,0,0],  # s3 is terminal
# [0,0,0,0,0,0],  # s4 is terminal [0,0,0,0,0,0],  # s5 is terminal ] So, we can
# consider different paths to terminal states, such as: s0 -> s1 -> s3 s0 -> s1
# -> s0 -> s1 -> s0 -> s1 -> s4 s0 -> s1 -> s0 -> s5 Tracing the probabilities
# of each, we find that s2 has probability 0 s3 has probability 3/14 s4 has
# probability 1/7 s5 has probability 9/14 So, putting that together, and making
# a common denominator, gives an answer in the form of [s2.numerator,
# s3.numerator, s4.numerator, s5.numerator, denominator] which is [0, 3, 2, 9,
# 14].
# 
# Languages =========
# 
# To provide a Python solution, edit solution.py To provide a Java solution,
# edit solution.java
# 
# Test cases ==========
# 
# Inputs: (int) m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0,
# 0, 0, 0], [0, 0, 0, 0, 0]]
# Output: (int list) [7, 6, 8, 21]
# 
# Inputs: (int) m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] 
# Output: (int list) [0, 3, 2, 9, 14]
def answer(m):
    
    height = len(m)
    width = len(m[0])
    matrix = list(m)
    
    sums = [sum(i) for i in matrix]
    terms = [i for i, value in enumerate(sums) if value == 0]
    not_terms = list((set(range(height)) - set(terms)))
    nt_length = len(not_terms)

    for key, value in enumerate(m):
        value[key] = 0
        
    for i in xrange(0, nt_length - 1):
        x = not_terms[nt_length - i - 1]
        for j in xrange(0, nt_length - 1):
            y = not_terms[j]        
            matrix[y] = back(matrix[y], y, matrix[x] , x)
            
    result = []
    
    for i in terms:
        result.append(matrix[0][i])
        
    total = sum(result)
    result.append(total)
    
    if total == 0:
        result = [1 for i in terms]
        result.append(len(terms))
        
    return result

def back(value1, i1, value2, i2):

    lenV = len(value1)
    indices = (set(range(lenV)) - {i1, i2})
    sum2 = sum(value2)
    output = [0 for i in value1]

    for i in indices:
        output[i]= sum2 * value1[i] + value1[i2] * value2[i]

    gcd = gcd_l(output)
    result = [int( i / gcd ) for i in output]

    return result
    
def greatest_common (x, y):

    if (y == 0):
        return x
    else:
        return greatest_common(y, x % y)
         
def gcd_l (l):

    L = len(l)
    result = 0

    for i in range(0, L):
        result = greatest_common(result, l[i])
    return result

print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))