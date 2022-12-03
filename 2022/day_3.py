from day_3_inputs import input
import string

alphabet = [*string.ascii_lowercase + string.ascii_uppercase]

def solution1():
    beg = input.strip('\n').split('\n')
    solution = sum([alphabet.index(b[0]) + 1 for b in [[*set([a for a in [*x[:int(len(x)/2)]] if a in [*x[int(len(x)/2):]]])] for x in beg]])
    print(solution)

solution1()

def solution2():
    beg = input.strip('\n').split('\n')
    solution = sum([alphabet.index(b[0]) + 1 for b in[[*set([a for a in x[0] if a in x[1] and a in x[2]])] for x in [beg[i:i+3] for i in range(0, len(beg), 3)]]])
    print(solution)

solution2()