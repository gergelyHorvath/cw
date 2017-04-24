import re


def is_valid_coordinates(coordinates):
    pattern = r"-?0*([0-8]?[0-9](\.\d*)?|90)(,( )?-?0*(([0-9]|[0-9][0-9]|1[0-7][0-9])(\.\d*)?|180))?$"
    answer = bool(re.match(pattern, coordinates))
    return answer
