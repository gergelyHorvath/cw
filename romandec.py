def solution(roman):
    _sum = roman.count('M') * 1000 + roman.count('D') * 500 + roman.count('C') * 100 + roman.count('L') * 50 + roman.count('X') * 10 + roman.count('V') * 5 + roman.count('I') * 1
    _sum -= roman.count('CM') * 200 + roman.count('CD') * 200 + roman.count('XC') * 20 + roman.count('XL') * 20 + roman.count('IX') * 2 + roman.count('IV') * 2
    return _sum

print(solution('MMMCM'))
