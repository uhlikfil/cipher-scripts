import sys
import enchant

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


def is_text_english(text):
    d = enchant.Dict('en_US')
    word_length = 5
    check_coefficient = 30
    counter = 0
    text_length = len(text)
    for i in range(text_length - word_length):
        if d.check(text[i:i+word_length]):
            counter += 1
    return counter > text_length / check_coefficient


out_name = 'results.txt'

if (sys.argv[2] == '-s'):
    with open(out_name, 'w') as output_file:
        for result in get_all_transpos(sys.argv[1]):
            if (len(sys.argv) > 3 and sys.argv[3] == '-f'):
                if is_text_english(result[1]):
                    output_file.write(f'{result[0]}\n{result[1]}\n')
            else:
                output_file.write(f'{result[0]}\n{result[1]}\n')
elif (sys.argv[2] == '-d'):
    with open(out_name, 'w') as output_file:
        for result in double_transpo(sys.argv[1]):
            if (len(sys.argv) > 3 and sys.argv[3] == '-f'):
                if is_text_english(result[1]):
                    output_file.write(f'{result[0]}\n{result[1]}\n{result[2]}\n')
            else:
                output_file.write(f'{result[0]}\n{result[1]}\n{result[2]}\n')