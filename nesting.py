def same_structure_as(original, other):
    if not (isinstance(original, list) and isinstance(other, list)):
        return bool(isinstance(original, list) == isinstance(other, list))
    if len(original) != len(other):
        return False
    for i in range(len(other)):
        if isinstance(original[i], list) != isinstance(other[i], list):
            return False
        if isinstance(original[i], list):
            if not same_structure_as(original[i], other[i]):
                return False
    return True


print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ]))

