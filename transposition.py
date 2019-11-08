import sys

def get_divisors(number):
    result = []
    for i in range(2, number):
        if (number / i).is_integer():
            result.append(i)
    return result


def transpo(num_of_cols, text):
    result = ''
    for i in range(len(text) - 1):
        result += text[(i*num_of_cols) % (len(text) - 1)]
    return num_of_cols, result + text[len(text) - 1]


def get_all_transpos(text):
    result = []
    for cols in get_divisors(len(text)):
        result.append(transpo(cols, text))
    return result


def double_transpo(text):
    result = []
    for ct in get_all_transpos(text):
        second_transpos = get_all_transpos(ct[1])
        for ot in second_transpos:
            result.append((ct[0], ot[0], ot[1]))
    return result

with open('results.txt', 'w') as output_file:
   for result in double_transpo(sys.argv[1]):
        output_file.write(f'{result[0]}\n{result[1]}\n{result[2]}\n')

if (sys.argv[1] == '-s'):
    with open('results.txt', 'w') as output_file:
        for result in get_all_transpos(sys.argv[2]):
            output_file.write(f'{result[0]}\n{result[1]}\n')
else:
    with open('results.txt', 'w') as output_file:
        for result in double_transpo(sys.argv[1]):
            output_file.write(f'{result[0]}\n{result[1]}\n{result[2]}\n')
