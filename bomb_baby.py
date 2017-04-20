# Bomb, Baby!
# ===========
# 
# You're so close to destroying the LAMBCHOP doomsday device you can taste it!
# But in order to do so, you need to deploy special self-replicating bombs designed
# for you by the brightest scientists on Bunny Planet. 
# There are two types: Mach bombs (M) and Facula bombs (F). 
# The bombs, once released into the LAMBCHOP's inner workings, 
# will automatically deploy to all the strategic points you've identified and destroy them at the same time. 
# 
# But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
# 
# For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 
# 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. 
# The replication process can be changed each cycle. 
# 
# Second, you need to ensure that you have exactly the right number
# of Mach and Facula bombs to destroy the LAMBCHOP device.
# Too few, and the device might survive.
# Too many, and you might overload the mass capacitors 
# and create a singularity at the heart of the space station - not good! 
# 
# And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - 
# aboard the ship when you arrived, so that's all you have to start with. 
# (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, 
# but that's not going to stop you from trying!) 
# 
# You need to know how many replication cycles (generations) it will take to generate the correct amount 
# of bombs to destroy the LAMBCHOP.
# Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. 
# Return the fewest number of generations (as a string) that need to pass 
# before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, 
# or the string "impossible" if this can't be done!
# M and F will be string representations of positive integers no larger than 10^50.
# For example, if M = "2" and F = "1", one generation would need to pass,
# so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.
# 
# 
# 
# Test cases
# ==========
# 
# Inputs:
#     (string) M = "2"
#     (string) F = "1"
# Output:
#     (string) "1"
# 
# Inputs:
#     (string) M = "4"
#     (string) F = "7"
# Output:
#     (string) "4"
# 
def answer(M, F):
    mach = int(M)
    facula = int(F)

    if mach > facula:
        result = calc(1, mach - facula, facula)
    else:
        result = calc(1, mach, facula - mach)

    if not result:
        return "impossible"
    return result


def calc(count, m, f):

    if m == f:
        if m != 1:
            return -1
        return str(count)
        
    if m == 1 or f == 1 and count > 1:
        if m == 1 and f - (m * f) == 0:
            return str(count + (f - m))
        if f == 1 and m - (f * m) == 0:
            return str(count + (m - f))
        return

    elif any(x <= 0 for x in [m, f]):
        return

    # see if we can find a ratio here; multiply our count by that ratio to save iterations
    if f > 10^20 or m > 10^20:
        if m > f:
            multiplier = int(round(m/f))
            m1 = int(m - f * multiplier)
            return calc(count + multiplier, m1, f)

        elif f > m:
            multiplier = int(round(f/m))
            f1 = int(f - m * multiplier)
            return calc(count + multiplier, m, f1)

    facula = calc(count + 1, m, f - m)
    mach = calc(count + 1, m - f, f)

    if mach == -1:
        return facula
    if facula == -1:
        return mach
    if mach > facula:
        return mach
    else:
        return facula        
print(answer('400000', '7'))
