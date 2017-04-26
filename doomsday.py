def answer(matrix):

    m = {}

    for key, value in enumerate(matrix):
        m.setdefault((key), value)

    # find both our terminal(absorbing) and continuous states
    terminal = { k:v for k,v in m.items() if all([items == 0 for items in v]) }
    cont = { k:v for k,v in m.items() if any([items > 0 for items in v]) }

    print(term)
    # matrix for our terminal states
    identity_matrix = []

    # matrix representing 0 probability of continous->terminal state transition
    zero_matrix = {}

    # matrix representing continuous->continuous state transitions
    q_matrix = {}

    # matrix representing continuous->terminal state transitions
    r_matrix = {}

    return m

answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
