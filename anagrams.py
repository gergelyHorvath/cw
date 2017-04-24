def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def same_char(word):
    result = []
    length = len(word)
    for char in word:
        word = word.replace(char, '')
        result.append(length - len(word))
        length = len(word)
    result = [i for i in result if i > 0]
    return result


def product(list_):
    result = 1
    for i in list_:
        result *= factorial(i)
    return result


def listPosition(word):
    sorted_word = ''.join(sorted(word))
    counter = 0
    for char in word:
        previous = ''
        for schar in sorted_word:
            if schar == previous:
                continue
            if schar == char:
                break
            divisor_list = same_char(word.replace(schar, '', 1))
            counter += factorial(len(word) - 1) / product(divisor_list)
            previous = schar
        word = word.replace(char, '', 1)
        sorted_word = sorted_word.replace(char, '', 1)
    return int(counter + 1)


def main():
    while True:
        word = input('\nEnter a word:')
        if word == 'x':
            exit()
        print(listPosition(word))


if __name__ == '__main__':
    main() 