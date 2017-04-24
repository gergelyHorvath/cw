def get_pins(observed):
    the_dict = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '0', '5', '7', '9'],
        '9': ['9', '6', '8']
    }
    observed = list(observed)
    return recur(observed, the_dict, 0)


def recur(observed, the_dict, d=0):
    if d == len(observed):
        return [''.join(observed)]
    solution = []
    for i in the_dict[observed[d]]:
        observed[d] = i
        solution += recur(observed[:], the_dict, d+1)
    return solution


print(get_pins('11'))



